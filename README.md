# MongoSync-App
MongoSync-App is a general-purpose Progressive Web Application (PWA) built with FastAPI (backend), MongoDB (database), and vanilla JavaScript + W3.CSS (frontend). The app demonstrates how to create a universal dashboard that works both offline and online, syncing data seamlessly once the user reconnects — similar to apps like YouTube, Instagram etc

Features
  Cross-Platform PWA – works on desktop, tablet, and mobile.
  Offline-First Approach – data is cached locally using LocalStorage + Service Worker.
  MongoDB Integration – structured data storage in collections.
  FastAPI Backend – lightweight APIs for CRUD operations.
  Entity Management – customizable to handle Teachers, Students, Visitors, Products, etc.
  Dynamic Views – Home, Registration, Visitor List, and Contact sections.
  Modern UI – responsive design powered by W3.CSS and FontAwesome.

Tech Stack
  Frontend: HTML5, CSS3, JavaScript, W3.CSS, PWA (manifest + service worker)
  Backend: FastAPI (Python)
  Database: MongoDB Atlas (Cloud)
  Offline Support: LocalStorage + Service Worker

Project Structure

  MongoSync-App/
  │── backend/
  │ ├── main.py # FastAPI server
  │ ├── requirements.txt # Python dependencies
  │
  │── frontend/
  │ ├── index.html # Main UI
  │ ├── app.js # Frontend logic
  │ ├── manifest.json # PWA manifest
  │ ├── service-worker.js # Offline caching
  │ ├── styles.css # Styling
  │
  │── README.md

Installation & Setup
  Backend (FastAPI + MongoDB):
    Clone the repo:
    git clone https://github.com/your-username/MongoSync-App.git
    
    cd MongoSync-App/backend
    
    Create a virtual environment and install dependencies:
    python -m venv .venv
    source .venv/bin/activate (On Windows: .venv\Scripts\activate)
    pip install -r requirements.txt
    
    Run FastAPI server:
    uvicorn main:app --reload
    API will run on: http://127.0.0.1:8000

  Frontend (PWA):
    Open frontend/index.html in a browser.
    The app will automatically connect to the FastAPI backend.
    Add data → View in tables → Works offline → Syncs when online.

Use Cases
  School/College dashboards (Teachers, Students, Staff)
  Business management (Products, Customers, Sales)
  General CRUD apps (Inventory, Task Manager, Visitor Log)
  Any data-driven app requiring offline + online sync

Future Enhancements
  User Authentication (Login/Signup)
  Multi-collection dashboard (Teachers, Students, Products, etc.)
  Cloud deployment on Heroku, Render, or AWS/GCP
  Real-time updates with WebSockets

Contributing
  Fork the project
  Create a feature branch (git checkout -b feature-name)
  Commit changes (git commit -m "Added new feature")
  Push to branch (git push origin feature-name)
  Create a Pull Request

License
This project is licensed under the MIT License – feel free to use and modify it.

