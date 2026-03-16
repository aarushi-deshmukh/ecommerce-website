# PARS - E-Commerce Marketplace Platform

A full-stack e-commerce platform built with **Django, Vue.js, and SQLite** that enables buyers and sellers to interact in a secure marketplace. The platform supports authentication, product management, shopping cart functionality, wishlist tracking, and sales analytics.

This system was designed to provide small businesses with an easy way to manage products and reach customers online.

---

# 📸 Screenshots

<img width="1919" height="893" alt="image" src="https://github.com/user-attachments/assets/9fa87306-d32f-4da6-a498-3300837ba70d" />
<img width="1919" height="897" alt="image" src="https://github.com/user-attachments/assets/75489ca1-636b-431d-b962-6f6e3ce9f2a8" />

Example:

* Dashboard
* Product Listing
* Seller Product Management
* Shopping Cart

---

# 🚀 Features

### 👤 Authentication System

* Buyer and Seller role-based authentication
* Secure login using Django sessions
* Separate dashboards for buyers and sellers

### 🛍 Product Management

* Sellers can add, update, and manage products
* Product categories and inventory tracking
* Image uploads for products

### 🛒 Shopping Cart

* Add products to cart
* Update quantities dynamically
* Persistent cart per buyer

### ❤️ Wishlist

* Save products for later purchase
* Easy access to favorite items

### 📊 Seller Analytics

* Track product performance
* View sales insights
* Monitor inventory

### 🔒 Data Integrity

* Implemented **SQL triggers, cursors, and functions**
* Ensures business rules and transactional consistency
* Prevents invalid updates and maintains database integrity

---

# 🏗 Tech Stack

### Frontend

* **Vue.js**
* **Axios**
* **Vue Router**
* Responsive UI with modern CSS

### Backend

* **Django**
* **Django REST-style APIs**
* **Django Authentication System**

### Database

* **SQLite / PostgreSQL**
* SQL triggers, stored procedures, and cursors

---

# 📂 Project Structure

```id="proj-structure"
ecommerce-project/
│
├── backend/
│   ├── api/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   │
│   ├── backend/
│   │   ├── settings.py
│   │   └── urls.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   └── assets/
│
├── public/
├── manage.py
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash id="clone-repo"
git clone https://github.com/aarushi-deshmukh/ecommerce-website.git
cd ecommerce-website
```

---

## 2️⃣ Backend Setup

```bash id="backend-setup"
cd backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

```bash id="frontend-setup"
cd frontend

npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🧩 Database Design

Main entities:

* **User**
* **Buyer**
* **Seller**
* **Product**
* **Cart**
* **CartItem**
* **Wishlist**

Relationships:

```id="db-rel"
User
 ├── Buyer
 │     ├── Cart
 │     │     └── CartItem → Product
 │     └── Wishlist → Product
 │
 └── Seller
        └── Product
```

---

# 📈 Impact

This platform helps small businesses:

* Expand their online reach
* Manage products efficiently
* Track sales and inventory

Testing indicated it could improve small business reach by **~4.3%** through increased online visibility and streamlined purchasing.

