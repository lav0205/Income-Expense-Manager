from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from flask_mysqldb import MySQL
import pandas as pd
import pdfkit
import os

PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_default_key")
##app.config['SESSION_TYPE'] = 'null'

# MySQL Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'income_expense_db'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM stock")
    stocks = cursor.fetchall()
    cursor.close()
    return render_template('index.html', stocks=stocks)

# Route for managing stock purchases and sales
@app.route('/stock', methods=['GET', 'POST'])
def stock():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        vendor_name = request.form['vendor_name']
        stock_type = request.form['stock_type']  # Purchase or Sale
        quantity = request.form['quantity']
        price = request.form['price']
        cursor.execute("INSERT INTO stock (vendor_name, type, quantity, price) VALUES (%s, %s, %s, %s)",
                       (vendor_name, stock_type, quantity, price))
        mysql.connection.commit()  # Commit after insertion
        flash('Stock entry added successfully!', 'success')
        return redirect(url_for('stock'))
    
    # Make sure cursor is open when fetching records
    cursor.execute("SELECT * FROM stock")
    stocks = cursor.fetchall()
    cursor.close()  # Close the cursor after finishing database interaction
    return render_template('stock.html', stocks=stocks)

# Route for managing income and expenses
@app.route('/income_expense', methods=['GET', 'POST'])
def income_expense():
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        category = request.form['category']
        trans_type = request.form['trans_type']  # Income or Expense
        amount = request.form['amount']
        cursor.execute("INSERT INTO income_expense (category, type, amount) VALUES (%s, %s, %s)",
                       (category, trans_type, amount))
        mysql.connection.commit()  # Commit after insertion
        flash('Entry added successfully!', 'success')
        return redirect(url_for('income_expense'))
    
    # Make sure cursor is open when fetching records
    cursor.execute("SELECT * FROM income_expense")
    records = cursor.fetchall()
    cursor.close()  # Close the cursor after finishing database interaction
    return render_template('income_expense.html', records=records)

# Route for generating reports (PDF/Excel)
@app.route('/generate_report/<format>')
def generate_report(format):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM income_expense")
    data = cursor.fetchall()
    cursor.close()  # Close cursor after fetching the data
    df = pd.DataFrame(data, columns=['ID', 'Category', 'Type', 'Amount'])
    
    if format == 'pdf':
        pdf_file = 'report.pdf'
        df.to_html('templates/report.html')
        pdfkit.from_file('templates/report.html', pdf_file, configuration=PDFKIT_CONFIG)
        return send_file(pdf_file, as_attachment=True)
    elif format == 'excel':
        excel_file = 'report.xlsx'
        df.to_excel(excel_file, index=False)
        return send_file(excel_file, as_attachment=True)
    return "Invalid format"

# Route for invoice generation
@app.route('/invoice/<int:invoice_id>')
def invoice(invoice_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM stock WHERE id = %s", (invoice_id,))
    invoice_data = cursor.fetchone()
    cursor.close()  # Close cursor after fetching the data
    return render_template('invoice.html', invoice=invoice_data)

if __name__ == '__main__':
    app.run(debug=True)
