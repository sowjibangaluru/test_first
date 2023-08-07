from flask import Flask
from flask import render_template, url_for, request, redirect, flash, session
import pymysql
import secrets
from flask_mysqldb import MySQL
# from flask_wtf.csrf import csrf_exempt

app = Flask(__name__)
# csrf = CSRFProtect(app)

app.secret_key = "flash messages"  # Replace "your_secret_key_here" with your actual secret key
app.secret_key = secrets.token_hex(16)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']='Ammu1998@17'
app.config['MYSQL_DB']='crudapplication'
mysql = MySQL(app)


@app.route('/')
def main():
    return render_template('home.html')
@app.route('/auth')
def auth_user(first_name,password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT first_name from users where first_name=%s AND password=%s",(first_name,password,))
    result=cur.fetchone()
    cur.close()
    return result

@app.route('/dashboard')
def index():
    search_query = request.args.get('search_query', '')
    if search_query:
        # If a search query is provided, perform a search based on the query
        cur = mysql.connection.cursor()
        # Assuming 'fname' is the column in your database that stores the employee's first name
        cur.execute("SELECT * FROM EMPLOYEES WHERE fname LIKE %s", ('%' + search_query + '%',))
        data = cur.fetchall()
        cur.close()
    else:
        # If no search query, retrieve all employees as usual
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM EMPLOYEES")
        data = cur.fetchall()
        cur.close()

    return render_template('index.html', EMPLOYEES=data)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        user = auth_user(first_name, password)
        if not first_name or not password:
            msg = 'please provide first name and password'
            return render_template('login.html', error_msg=msg)
        if user:
            msg = 'user already exists please login with username and password'
            return render_template('login.html', error_msg=msg)

        # check for the user in database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, password))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful!', 'success')
        return redirect('login')
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=auth_user(username,password)
        print("HIIII INDEX")

        if user:
            session['username']=username
            return redirect(url_for('index'))
            print("IF CONDITION")
        else:
            msg='incorrect username/password.Try again'
            return render_template('login.html',error_msg=msg)
            print("ERROR MSG")
    else:
        return render_template('login.html')
        print("ELSE CONDITION")



@app.route('/insert',methods=['POST'])
def insert():
    flash("Data inserted successfully")
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        age=request.form['age']
        experience=request.form['experience']
        sal=request.form['sal']
        skils=request.form['skils']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO EMPLOYEES (fname,lname,age,experience,sal,skils) VALUES (%s,%s,%s,%s,%s,%s)",(fname,lname,age,experience,sal,skils))
        #flash("Data inserted successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))

def get_employee_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM EMPLOYEES WHERE id = %s", (id,))
    employee = cur.fetchone()
    cur.close()
    return employee

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    print("HIIIIIIIII")
    cursor = mysql.connection.cursor()

    # Fetch the employee details from the database using the employee id.
    cursor.execute(f"SELECT * FROM employees WHERE id = {id}")
    employee = cursor.fetchone()

    if employee is None:
        print("NONEEEEEE")
        return "Employee not found", 404

    if request.method == 'POST':
        print("FORMMM")
        data = request.form
        fname = data['fname']
        lname = data['lname']
        age = int(data['age'])
        experience = int(data['experience'])
        sal = float(data['sal'])
        skils = data['skils']

        # Update the employee details in the database using an SQL UPDATE query.
        sql = "UPDATE employees SET fname = %s, lname = %s, age = %s, experience = %s, sal = %s, skils = %s WHERE id = %s"
        values = (fname, lname, age, experience, sal, skils, id)
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()

        return redirect('/')

    return render_template('index.html', employee=employee)


@app.route('/delete/<int:id_data>', methods=['GET'])
def delete(id_data):
    print("HELLO")
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM EMPLOYEES WHERE id=%s", (id_data,))  # Corrected: Use the primary key (id) for deletion
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True,port=90)

