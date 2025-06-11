# Django Fundamentals Project

This is a basic Django web application demonstrating core concepts including:
- URL routing
- Models and migrations
- Admin interface
- Templates and views

## Features
- Product catalog with name, price, stock, and image
- Offers with discounts and codes

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- Virtualenv (recommended)

### Setup
```bash
git clone https://github.com/YOUR_USERNAME/srivatsa0411-basic-django-fundamental0411.git
cd srivatsa0411-basic-django-fundamental0411
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the server
```bash
python manage.py migrate
python manage.py runserver
```

### Admin Access
Create a superuser:
```bash
python manage.py createsuperuser
```

Then access `http://127.0.0.1:8000/admin`
