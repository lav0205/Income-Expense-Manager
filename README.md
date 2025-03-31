# Income & Expense Manager

## 📌 Project Overview

This is a web-based **Income & Expense Manager** that helps users track their finances, manage stock, and generate reports in PDF and Excel formats. It includes features like invoice generation and stock tracking.

## 🚀 Features

- Stock Management
- Income & Expense Tracking
- Invoice Generation
- Report Generation (PDF & Excel)
- Interactive Stock Charts
- Responsive UI with Bootstrap
- Success Notification Popups

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask (Python)
- **Database**: MySQL
- **Report Generation**: Pandas, FPDF, openpyxl

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/income-expense-manager.git
cd income-expense-manager
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Configure MySQL Database

Update `config.py` with your database credentials:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "yourpassword"
DB_NAME = "income_expense_db"
```

### 4️⃣ Run the Application

```sh
flask run
```

Visit `http://127.0.0.1:5000/` in your browser.

## 📄 API Endpoints

| Route                           | Method | Description             |
| ------------------------------- | ------ | ----------------------- |
| `/`                             | GET    | Home Page               |
| `/stock`                        | GET    | Manage Stock            |
| `/income_expense`               | GET    | Track Income & Expenses |
| `/invoice/<invoice_id>`         | GET    | View Invoice            |
| `/generate_report?format=pdf`   | GET    | Download PDF Report     |
| `/generate_report?format=excel` | GET    | Download Excel Report   |

## 📊 Outputs & Screenshots

### 🔹 Dashboard



### 🔹 Invoice Page



## 📤 Uploading to GitHub

1. **Initialize Git** (if not already done):

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/lav0205/Income-Expense-Manager.git
git push -u origin main
```

2. **Push new changes**:

```sh
git add .
git commit -m "Updated ReadMe & Features"
git push origin main
```

## 🛠️ Author & Contributions

- **LAVANYA KARAMPURI**

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.
