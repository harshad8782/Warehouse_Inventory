# Warehouse Inventory Management (Django)

A simple **warehouse inventory tracking system** built with Django.  
It tracks **products, stock transactions (IN/OUT), and inventory levels** and provides a **basic UI** for dashboard, transactions, and inventory summary.

---

## Features

- Manage products (`prodmast` table)
- Track stock transactions (`stckmain` and `stckdetail` tables)
- Dashboard showing current inventory per product
- Admin panel for adding/editing data
- Clean API structure (Django + Django REST Framework)
- Ready for deployment on **PythonAnywhere** or **Render**

---

## Project Structure

```
WAREHOUSE-INVENTORY/
├── inventory/               # App with models, views, serializers, URLs
│   ├── models.py            # Product, StockTransaction, StockDetail
│   ├── views.py             # Dashboard, transactions, inventory APIs
│   ├── serializers.py       # REST API serializers
│   ├── urls.py
│   └── admin.py
├── static/                  # Static assets (CSS, JS)
├── templates/               # HTML templates (dashboard, inventory, transactions)
├── warehouse_inventory/     # Main project folder (settings, WSGI)
├── db.sqlite3               # Local database
├── requirements.txt         # Dependencies
└── manage.py
```

---

## Installation & Setup (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Warehouse_Inventory.git
cd Warehouse_Inventory
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit the app at:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

Admin panel:
**[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## Usage

1. Log in to the admin panel to add products (`Product`) and stock transactions
2. Dashboard will display **current stock per product**
3. Transactions page shows all `IN` and `OUT` transactions

---

## License

MIT – Free to use.

---

## Demo Data Seeder (Optional)

Would you like me to add a short "Demo Data Seeder" so that after deployment, you can auto-create some products and stock movements to make your dashboard look populated? Or would you prefer to keep it completely empty so you can add products manually via the admin panel?
