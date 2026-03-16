# ✨ GlitterApp - Inventory Management System

A beautiful and modern inventory management application built with Python, featuring a sleek dark-themed GUI and MySQL database integration.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-pink.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Technologies](#-technologies)
- [Installation](#-installation)
- [Database Setup](#-database-setup)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

**GlitterApp** is a fully-featured inventory management system designed for beauty and cosmetics businesses. It provides an intuitive graphical interface for managing products, categories, and stock levels with real-time database synchronization.

The application features a modern dark theme with pink and gold accents, making it both functional and visually appealing.

---

## ✨ Features

### Core Features
- ✅ **Product Management**: Add, update, delete, and search products
- 🔍 **Advanced Search**: Real-time search by product name
- 📊 **Category Filtering**: Filter products by category
- 📁 **CSV Export**: Export complete inventory to CSV format
- 🎨 **Modern UI**: Dark-themed interface with customizable colors
- 💾 **Database Integration**: MySQL backend for persistent data storage
- ⚡ **Real-time Updates**: Instant refresh of product listings

### Product Operations
- **Add Product**: Create new products with name, description, price, quantity, and category
- **Update Product**: Modify any product attribute (name, description, price, quantity)
- **Delete Product**: Remove products from inventory by ID
- **Search Product**: Find products instantly using partial name matching
- **Filter by Category**: View products from specific categories

---
## 📁 Project Structure

```
GlitterApp/
│
├── main.py                          # Application entry point
├── README.md                        # Project documentation
├── LICENSE                          # MIT License
├── products.csv                     # Exported product data
├── .gitignore                       # Root gitignore
│
├── src/                             # Source code directory
│   ├── __init__.py
│   ├── .gitignore
│   ├── Product.py                   # Product model & database operations
│   ├── Category.py                  # Category model & database operations
│   └── constant.py                  # UI theme constants (colors)
│
├── GraphicalInterface/              # GUI components
│   ├── __init__.py
│   ├── .gitignore
│   └── main_window.py               # Main application window & UI logic
│
└── database/                        # Database connection
    ├── __init__.py
    ├── .gitignore
    └── connection.py                # MySQL connection handler
```

---

## 🛠 Technologies

### Core Technologies
- **Python 3.8+**: Primary programming language
- **CustomTkinter**: Modern GUI framework for beautiful interfaces
- **MySQL 8.0+**: Relational database management system
- **mysql-connector-python**: MySQL driver for Python

### Python Libraries
```python
customtkinter==5.0+
mysql-connector-python==8.0+
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL Server 8.0 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/mahira-manico/runtrack-gestion_de_stock.git
cd GlitterApp
```
### Step 2: Install Dependencies
```bash
pip install customtkinter
pip install mysql-connector-python
```

---

## 💾 Database Setup

### Step 1: Create Database
Open MySQL and run:
```sql
CREATE DATABASE store;
USE store;
```

### Step 2: Create Tables

#### Category Table
```sql
CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

#### Product Table
```sql
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    id_category INT,
    FOREIGN KEY (id_category) REFERENCES category(id)
);
```

### Step 3: Insert Sample Categories
```sql
INSERT INTO category (name) VALUES 
    ('Makeup'),
    ('Skincare'),
    ('Fragrance'),
    ('Hair Care');
```

### Step 4: Configure Database Connection
Edit `database/connection.py` with your MySQL credentials:
```python
self.mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",      # Change this
    password="your_password",  # Change this
    database="store"
)
```

---

## 🎮 Usage

### Starting the Application
```bash
python main.py
```

### Adding a Product
1. Click **✦ Add Product** in the sidebar
2. Fill in the product details:
   - Name
   - Description
   - Price
   - Quantity
   - Category ID
3. Click **Save to Database**

### Searching for Products
1. Enter product name in the search bar
2. Click **Search**
3. Results appear instantly

### Filtering by Category
1. Select a category from the dropdown menu
2. Products are automatically filtered

### Updating a Product
1. Click **✦ Update Product** in the sidebar
2. Select the column to modify (name, description, price, quantity)
3. Enter the product ID
4. Enter the new value
5. Click **Save**

### Deleting a Product
1. Click **✦ Delete Product** in the sidebar
2. Enter the product ID
3. Click **Delete from Database**

### Exporting to CSV
1. Click **⬇ Export CSV** in the sidebar
2. File `products.csv` is created in the root directory

---

## 🏗 Architecture

### Design Pattern
The application follows the **MVC-inspired architecture**:

- **Model**: `Product.py`, `Category.py` (database operations)
- **View**: `main_window.py` (GUI components)
- **Controller**: Business logic integrated within view classes

### Class Structure

#### Product Class (`src/Product.py`)
Handles all product-related database operations:
- `get_all()`: Retrieve all products
- `get_product(letter)`: Search products by name
- `add(...)`: Insert new product
- `update(...)`: Modify existing product
- `delete(id)`: Remove product
- `get_category(name)`: Filter by category

#### Category Class (`src/Category.py`)
Manages product categories:
- `get_name()`: Retrieve all category names

#### Data Class (`database/connection.py`)
Manages MySQL connection:
- `cursor()`: Get database cursor
- `commit()`: Commit transactions
- `disconnect()`: Close connection

#### GUI Classes (`GraphicalInterface/main_window.py`)
- `GlitterApp`: Main application window
- `Dashboard`: Product listing and operations
- `Sidebar`: Navigation menu
- `AddProduct`: Modal for adding products
- `UpdateProduct`: Modal for updating products
- `DeleteProduct`: Modal for deleting products

### Database Schema

```
┌─────────────┐         ┌──────────────┐
│  category   │         │   product    │
├─────────────┤         ├──────────────┤
│ id (PK)     │◄────────│ id (PK)      │
│ name        │         │ name         │
└─────────────┘         │ description  │
                        │ price        │
                        │ quantity     │
                        │ id_category  │
                        └──────────────┘
```

---

## 🎨 UI Theme

The application uses a custom dark theme with the following color palette:

| Color Name    | Hex Code  | Usage                    |
|---------------|-----------|--------------------------|
| PINK          | `#E91E63` | Primary accent, buttons  |
| PINK_DARK     | `#C2185B` | Button hover states      |
| GOLD          | `#FFD700` | Headers, labels          |
| BG_DARK       | `#1A1A2E` | Main background          |
| BG_CARD       | `#16213E` | Card backgrounds         |
| BG_SIDEBAR    | `#0F3460` | Sidebar background       |
| TEXT          | `#FFFFFF` | Primary text             |
| TEXT_MUTED    | `#A0A0B0` | Secondary text           |

Colors can be customized in `src/constant.py`.

---

## 🔒 Security Notes

⚠️ **Important**: The current implementation stores database credentials in plain text in `connection.py`. For production use:

1. Use environment variables:
```python
import os
from dotenv import load_dotenv

load_dotenv()

self.mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
```

2. Add `.env` to `.gitignore`
3. Create `.env.example` with placeholder values
---

## 🚧 Future Enhancements

- [ ] User authentication and roles
- [ ] Low stock alerts
- [ ] Sales tracking and analytics
- [ ] Barcode scanning support
- [ ] Multi-currency support
- [ ] Dark/Light theme toggle
- [ ] Database backup functionality
- [ ] Advanced reporting (PDF export)
- [ ] Product images support
- [ ] Inventory history tracking

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Coding Standards
- Follow PEP 8 style guide
- Add docstrings to all functions
- Write meaningful commit messages
- Test thoroughly before submitting

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact

**Mahira Manico**

- GitHub: [@mahira-manico](https://github.com/mahira-manico)
- LinkedIn: [mahira-manico](https://www.linkedin.com/in/mahira-manico)
- Email: mahira.manico@laplateforme.io

---

## 🙏 Acknowledgments

- **CustomTkinter** - For the modern GUI framework
- **MySQL** - For robust database management
- **Python Community** - For excellent libraries and support
- **La Plateforme** - Educational institution

---

## 📊 Project Stats

- **Lines of Code**: ~500
- **Files**: 12
- **Classes**: 7
- **Database Tables**: 2
- **Features**: 8+

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/mahira-manico">Mahira Manico</a>
</p>

<p align="center">
  ⭐ Star this repository if you find it helpful!
</p>
