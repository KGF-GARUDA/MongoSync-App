# MongoSync-App
MongoSync-App is a general-purpose Progressive Web Application (PWA) built with FastAPI (backend), MongoDB (database), and vanilla JavaScript + W3.CSS (frontend). The app demonstrates how to create a universal dashboard that works both offline and online, syncing data seamlessly once the user reconnects — similar to apps like YouTube, Instagram etc

Features<br>
  Cross-Platform PWA – works on desktop, tablet, and mobile.<br>
  Offline-First Approach – data is cached locally using LocalStorage + Service Worker.<br>
  MongoDB Integration – structured data storage in collections.<br>
  FastAPI Backend – lightweight APIs for CRUD operations.<br>
  Entity Management – customizable to handle Teachers, Students, Visitors, Products, etc.<br>
  Dynamic Views – Home, Registration, Visitor List, and Contact sections.<br>
  Modern UI – responsive design powered by W3.CSS and FontAwesome.<br>

Tech Stack<br>
  Frontend: HTML5, CSS3, JavaScript, W3.CSS, PWA (manifest + service worker)<br>
  Backend: FastAPI (Python)<br>
  Database: MongoDB Atlas (Cloud)<br>
  Offline Support: LocalStorage + Service Worker<br>

Project Structure

  MongoSync-App/<br>
  │── backend/<br>
  │ ├── main.py # FastAPI server<br>
  │ ├── requirements.txt # Python dependencies<br>
  │<br>
  │── frontend/<br>
  │ ├── index.html # Main UI<br>
  │ ├── app.js # Frontend logic<br>
  │ ├── manifest.json # PWA manifest<br>
  │ ├── service-worker.js # Offline caching<br>
  │ ├── styles.css # Styling<br>
  │<br>
  │── README.md<br>

Installation & Setup<br>
  Backend (FastAPI + MongoDB):<br>
    Clone the repo:<br>
    git clone https://github.com/your-username/MongoSync-App.git<br>
    
    cd MongoSync-App/backend
    
    Create a virtual environment and install dependencies:
    python -m venv .venv
    source .venv/bin/activate (On Windows: .venv\Scripts\activate)
    pip install -r requirements.txt
    
    Run FastAPI server:
    uvicorn main:app --reload
    API will run on: http://127.0.0.1:8000

  Frontend (PWA):<br>
    Open frontend/index.html in a browser.<br>
    The app will automatically connect to the FastAPI backend.<br>
    Add data → View in tables → Works offline → Syncs when online.<br>

Use Cases<br>
  School/College dashboards (Teachers, Students, Staff)<br>
  Business management (Products, Customers, Sales)<br>
  General CRUD apps (Inventory, Task Manager, Visitor Log)<br>
  Any data-driven app requiring offline + online sync<br>

Future Enhancements<br>
  User Authentication (Login/Signup)<br>
  Multi-collection dashboard (Teachers, Students, Products, etc.)<br>
  Cloud deployment on Heroku, Render, or AWS/GCP<br>
  Real-time updates with WebSockets<br>

Contributing<br>
  Fork the project<br>
  Create a feature branch (git checkout -b feature-name)<br>
  Commit changes (git commit -m "Added new feature")<br>
  Push to branch (git push origin feature-name)<br>
  Create a Pull Request<br>

License<br>
This project is licensed under the MIT License – feel free to use and modify it.<br>

