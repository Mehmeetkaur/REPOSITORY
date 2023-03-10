"""
1. Create a Class in Python using OOPS
    Customer
        id, name, phone, email, createdOn, remarks, points, type
2. Create a Table in MySQL using the attributes of your Object
3. Create a Class DataBaseHelper where you will create write and read operations for the table
4. Create a Flask Web App
    4.1 Create a Web Page which has fields to insert data
        Here, fields will be as per the number of attributes
        As per our project, id and createdOn is automatic
        Hence, 6 UI Web Elements must be thr
    4.2 Create a Web Page which has a table to display records
"""

from flask import *
from session19 import Customer
from DatabaseHelper import DataBaseHelper

app = Flask("CustomerManagementApp", template_folder="cms")
db_helper = DataBaseHelper()

@app.route("/")
def index():
    # return "Welcome to CMS App"
    return render_template("index.html")


@app.route("/add")
def add():
    # return "Welcome to CMS App"
    return render_template("add_customer.html")


@app.route("/view")
def view():
    # return "Welcome to CMS App"
    cref = Customer()
    sql = cref.select_sql()
    rows = db_helper.read(sql)
    return render_template("view_customers.html", result=rows)


@app.route("/delete/<id>")
def delete_customer_from_db(id):
    cref = Customer(id=id)
    sql = cref.delete_sql()
    db_helper.write(sql)

    return render_template("success.html", message="Customer with ID "+id+" Deleted Successfully..")


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    cref = Customer(name=request.form["name"],
                    phone=request.form["phone"],
                    email=request.form["email"],
                    remarks=request.form["remarks"])

    if len(cref.name) == 0:
        return render_template("error.html", message="Name cannot be Empty...")

    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)

    # return cref.name+" Inserted Successfully..."
    return render_template("success.html", message=cref.name+" Inserted Successfully...")


@app.route("/update_customer")
def update_customer():
    return render_template("update_customer.html")


def main():
    app.run()


if __name__ == "__main__":
    main()