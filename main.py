from models import User
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# -------------------------------
# CONFIG
# -------------------------------
SECRET_KEY = "supersecretkey"   # change for production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# -------------------------------
# INIT APP
# -------------------------------
app = FastAPI()

# Enable CORS (allow frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")


# -------------------------------
# DATABASE
# -------------------------------
uri = ""
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["AdminDB"]
admins_collection = db["admins"]

# Insert default admin if not exists
if admins_collection.count_documents({"username": "admin"}) == 0:
    admins_collection.insert_one({"username": "admin", "password": "admin123"})

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)



database_name = client["Registration"]
User_Collection = database_name["User"]
User_Collection.create_index("id", unique=True)

# List all databases
print(client.list_database_names())

# List collections in the School database
print(database_name.list_collection_names())

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# -------------------------------
# ROUTES
# -------------------------------

@app.get("/databases")
def greet():
    return {
        "databases": client.list_database_names(),
        "collections": database_name.list_collection_names()
    }


@app.get("/users")
def get_user():
    user = list(User_Collection.find())
    return [serialize_doc(teacher) for teacher in user]


@app.post("/user")
def create_user(user: User):
    existing_user = User_Collection.find_one({"id": user.id})
    if existing_user:
        return {"error": f"user with id {user.id} already exists"}

    result = User_Collection.insert_one(user.dict())
    return {
        "message": "User added successfully",
        "inserted_id": str(result.inserted_id),
        "user": user
    }

@app.post("/user")
def create_user(user: User):
    existing_user = User_Collection.find_one({"id": user.id})
    if existing_user:
        return {"error": f"user with id {user.id} already exists"}

    result = User_Collection.insert_one(user.dict())
    return {
        "message": "user added successfully",
        "inserted_id": str(result.inserted_id),
        "user": user
    }

@app.get("/user/{id}")
def get_user_by_id(id: int):
    user = User_Collection.find_one({"id": id})

    if user:
        user["_id"] = str(user["_id"])  # serialize ObjectId
        return user
    else:
        return {"message": f"user with id {id} not found"}


@app.delete("/duser/{id}")
def delete_user(id: int, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    result = User_Collection.delete_one({"id": id})
    if result.deleted_count == 1:
        return {"message": f"user with id {id} deleted successfully"}
    else:
        return {"message": f"user with id {id} not found"}



@app.post("/admin/login")
def admin_login(form_data: OAuth2PasswordRequestForm = Depends()):
    admin = admins_collection.find_one({"username": form_data.username})
    if not admin or admin["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/admin/dashboard")
def admin_dashboard(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": f"Welcome {username}, this is the admin dashboard"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")

@app.get("/admin/verify")
def verify_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": "Token valid", "username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

