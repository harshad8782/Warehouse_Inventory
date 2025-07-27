
Here’s a **complete README.md** (Markdown) you can drop into your project root.
It explains everything — **setup, running locally, deploying to PythonAnywhere, usage, and admin setup**.

---

```markdown
# Warehouse Inventory Management (Django)

A simple **warehouse inventory tracking system** built with Django.  
It tracks **products, stock transactions (IN/OUT), and inventory levels** and provides a **basic UI** for dashboard, transactions, and inventory summary.

---

## Features
- Manage products (`prodmast` table).
- Track stock transactions (`stckmain` and `stckdetail` tables).
- Dashboard showing current inventory per product.
- Admin panel for adding/editing data.
- Clean API structure (Django + Django REST Framework).
- Ready for deployment on **PythonAnywhere** or **Render**.

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
├── warehouse\_inventory/     # Main project folder (settings, WSGI)
├── db.sqlite3               # Local database
├── requirements.txt         # Dependencies
└── manage.py

````

---

## Installation & Setup (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Warehouse_Inventory.git
cd Warehouse_Inventory
````

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

## Deployment on PythonAnywhere

1. **Clone Project on PythonAnywhere**

```bash
git clone https://github.com/<your-username>/Warehouse_Inventory.git
cd Warehouse_Inventory
```

2. **Create Virtual Environment & Install Dependencies**

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. **Run Migrations & Create Superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. **Configure PythonAnywhere Web App**

* Go to **Web → Add a New Web App**.
* Select **Manual Configuration (Python 3.10)**.
* Set project directory to where `manage.py` is.
* Set virtualenv path to:

  ```
  /home/<your-username>/Warehouse_Inventory/venv
  ```
* Edit your WSGI file to:

  ```python
  import os
  import sys

  path = '/home/<your-username>/Warehouse_Inventory'
  if path not in sys.path:
      sys.path.append(path)

  os.environ['DJANGO_SETTINGS_MODULE'] = 'warehouse_inventory.settings'

  from django.core.wsgi import get_wsgi_application
  application = get_wsgi_application()
  ```

5. **Set Environment Variables** (Web → Environment Variables):

```
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-username.pythonanywhere.com
```

6. **Reload Your Web App** from the Web tab.

Your site is now live:
**[https://your-username.pythonanywhere.com/](https://your-username.pythonanywhere.com/)**

---

## Usage

1. Log in to the admin panel to add products (`Product`) and stock transactions.
2. Dashboard will display **current stock per product**.
3. Transactions page shows all `IN` and `OUT` transactions.

---

## API Endpoints (Optional)

If you use the Django REST Framework views:

* `/api/products/` – List and manage products.
* `/api/transactions/` – List and manage stock transactions.
* `/api/inventory/` – Get inventory summary.

---

## Notes

* Static folder warning (`staticfiles.W004`) can be fixed by creating the folder:

  ```bash
  mkdir static
  ```
* Ensure `ALLOWED_HOSTS` is configured in `settings.py`:

  ```python
  import os
  DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
  ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
  ```

---

## License

MIT – Free to use.

```

---

Do you also want me to **add a short "Demo Data Seeder"** (so after deployment, you can auto-create some products and stock movements to make your dashboard look full)?  
Or keep it **completely empty so you add products manually via admin**? Which do you prefer?
```
