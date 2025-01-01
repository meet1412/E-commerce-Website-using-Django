# E-commerce Website using Django

An e-commerce web application built with Django that allows users to browse products, add them to a cart, and proceed with checkout. This project demonstrates the use of Django for backend development and includes basic features for an online store.

---

## Features
- **Home Page**: Displays a list of products available for purchase.
- **Product Management**: Admin can manage products using the Django admin panel.
- **Cart Functionality**: Users can add/remove items from their shopping cart.
- **Checkout Page**: Users can proceed to purchase the items in their cart.
- **Responsive Design**: Basic CSS and JavaScript for styling and interactivity.

---

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Hosting**: Local Development Server

---

## Directory Structure

```
meet1412-E-commerce-Website-using-Django/
├── ecom/
│   ├── ecom/
│   │   ├── settings.py       # Django project settings
│   │   ├── __init__.py       # Package initialization
│   │   ├── urls.py           # Project-level URL configuration
│   │   ├── asgi.py           # ASGI config
│   │   └── wsgi.py           # WSGI config
│   ├── manage.py             # Django management script
│   ├── db.sqlite3            # SQLite database
│   ├── store/
│   │   ├── models.py         # Database models for the app
│   │   ├── __init__.py       # Package initialization
│   │   ├── urls.py           # App-level URL configuration
│   │   ├── tests.py          # Test cases
│   │   ├── apps.py           # App configuration
│   │   ├── migrations/       # Database migration files
│   │   ├── admin.py          # Admin panel configurations
│   │   ├── views.py          # Application views
│   │   └── templates/
│   │       └── store/        # HTML templates
│   │           ├── cart.html
│   │           ├── home.html
│   │           ├── checkout.html
│   │           └── main.html
│   └── static/
│       ├── images/           # Product images and other assets
│       ├── css/              # Stylesheets
│       │   └── main.css
│       └── js/               # JavaScript files
│           └── cart.js
└── README.md                 # Project documentation
```

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/meet1412-E-commerce-Website-using-Django.git
   cd meet1412-E-commerce-Website-using-Django
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`

---

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

