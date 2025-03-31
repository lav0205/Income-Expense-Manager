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

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL (for storing income, expense, and stock data)
- **PDF Generation**: pdfkit for generating PDF reports
- **Excel Generation**: pandas library for generating Excel reports
- **Environment Variables**: For secret key management and configuration

## 📦 Required Packages
Install the following dependencies before running the project:
```sh
pip install flask flask-mysqldb pandas pdfkit openpyxl fpdf
```


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
DB_PASSWORD = "your_password"
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
![Screenshot (91)](https://github.com/user-attachments/assets/09bb0bf9-6ae6-4cc4-88ee-d62c776639d9)
![Screenshot (92)](https://github.com/user-attachments/assets/aba135cd-fa0f-4e54-846f-ae1c094fc82b)

- Stock Manager Management
![Screenshot (93)](https://github.com/user-attachments/assets/95d9f866-bbc9-4110-ba77-8b82e1f7a98f)

- Income & Expense Management
![Screenshot (94)](https://github.com/user-attachments/assets/3e4b7200-497a-44f2-9c99-e9bdd29f77a5)

- Download Reports
      * PDF Format-
      ![Screenshot (95)](https://github.com/user-attachments/assets/59593476-3fe4-43ec-8a34-8b206e72cf16)
      ![Screenshot (96)](https://github.com/user-attachments/assets/f7f13a01-2d3d-4b6a-87e5-75adac6f8803)
      [report.pdf](https://github.com/user-attachments/files/19541170/report.pdf)
      * EXCEL Format-
      ![Screenshot (97)](https://github.com/user-attachments/assets/0a026ad8-aa7e-4f5c-a8ee-89c16ecc4b35)
      ![Screenshot (98)](https://github.com/user-attachments/assets/91dc74af-6495-4bd6-82fc-c731d6e541b9)
      [report.xlsx](https://github.com/user-attachments/files/19541175/report.xlsx)

### 🔹 Invoice Page
![Screenshot (99)](https://github.com/user-attachments/assets/363827c4-f4f5-4988-8cf8-617d9cdc0f4d)
![Screenshot (100)](https://github.com/user-attachments/assets/4293b932-9c17-4c02-93d4-9bf6ff868295)


## 🛠️ Author & Contributions

- **LAVANYA KARAMPURI**

Contributions are welcome! Feel free to open an issue or submit a pull request.
