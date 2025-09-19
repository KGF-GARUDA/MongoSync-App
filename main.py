from fastapi import FastAPI
from models import User

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing. For production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://kanishksingh026_db_user:Kanishk%40123@cluster-0.rqszap9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


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
        "message": "Teacher added successfully",
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
def delete_user(id: int):
    result = User_Collection.delete_one({"id": id})

    if result.deleted_count == 1:
        return {"message": f"user with id {id} deleted successfully"}
    else:
        return {"message": f"user with id {id} not found"}


"""

products_list = [
    Product(id=1,name="Kanishk"),
    Product(id=2,name="Singh"),
    Product(id=3,name="hello"),
    Product(id=4,name="world"),
    Product(id=10,name="Dad"),
]



@app.get("/product/{id}")
def get_product_by_id(id: int):
    for Product in products_list:
        if Product.id == id:
            return Product
    else:
        return "id not found"

@app.post("/product")
def create_product(product: Product):
    products_list.append(product)
    return product

@app.put("/product")
def update_product(id: int, product : Product):
    for i in range(len(products_list)):
        products_list[i].id == id
        products_list[i] = product
        return "Product Updated sucessfully"
    else:
        return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products_list)):
        products_list[i].id == id
        del products_list[i]
        return "Product Deleted sucessfully"
    else:
        return "Product not found" """