# Car Dealership Management System

This repository contains a full‑stack web application for managing a car dealership inventory, sales, and customer interactions.  
The backend is built with **Django** and **Django REST Framework**, providing a robust API for CRUD operations on vehicles, customers, and orders.  
The frontend is a **React** single‑page application that consumes the API and offers a modern, responsive user interface.

## Features
- **Vehicle inventory**: Add, edit, delete, and search vehicles with detailed specifications.
- **Customer management**: Store customer contact information and purchase history.
- **Order processing**: Create and track sales orders, generate invoices, and manage payments.
- **Authentication & Authorization**: Secure login with JWT tokens and role‑based access control.
- **Responsive UI**: Built with React, React Router, and Material‑UI for a seamless experience on desktop and mobile devices.
- **Docker support**: Containerized services for easy deployment.

## Getting Started

### Prerequisites
- Docker & Docker‑Compose
- Node.js (>=14) and npm
- Python 3.10+

### Development Setup
```bash
# Clone the repository
git clone https://github.com/your‑username/car‑dealership‑app.git
cd car-dealership-app

# Backend (Django)
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (React)
cd ../frontend
npm install
npm start
```

### Running with Docker
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000/api/` and the React app at `http://localhost:3000/`.

## Project Structure
```
car-dealership-app/
├── backend/                # Django project
│   ├── dealership/        # Core app
│   ├── manage.py
│   └── requirements.txt
├── frontend/               # React application
│   ├── src/
│   └── package.json
├── docker-compose.yml
└── README.md
```

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

*For more information, refer to the documentation in the `docs/` folder.*