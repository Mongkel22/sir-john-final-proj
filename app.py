from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Create a MySQL database connection
myconn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='healthcare'
)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/verify', methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        mycursor = myconn.cursor()
        sql = "SELECT * FROM healthcareusers WHERE userid=%s AND password=%s AND status=1"
        data = (userid, password)
        mycursor.execute(sql, data)
        myresult = mycursor.fetchall()

        if myresult:
            row = myresult[0]
            name = row[3]
            accesslevel = row[4]
            return render_template('admin_dashboard.html', userid=userid, name=name, accesslevel=accesslevel)
        else:

            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        name = request.form['name']
        mycursor = myconn.cursor()
        sql = "INSERT INTO healthcareusers (userid, password, name) VALUES (%s, %s, %s)"
        data = (userid, password, name)
        mycursor.execute(sql, data)
        myconn.commit()

        return redirect(url_for('users'))


@app.route('/users', methods=['GET'])
def users():
    mycursor = myconn.cursor()
    sql = "SELECT * FROM healthcareusers"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if myresult:
        return render_template('users.html', users=myresult)
    else:
        return render_template('admin_dashboard.html')

@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'GET':
        # Handle the user update logic here
        return "Update user with id: " + str(id)


@app.route("/main")
def main():
    return render_template("main.html")


healthy_people = ["Michael", "Ghio", "Dan", "Jello"]
unhealthy_people = ["John", "Alvin", "Mike", "Hannah"]


@app.route("/community")
def community():
    return render_template("community.html", healthy_people=healthy_people, unhealthy_people=unhealthy_people)


@app.route('/health')
def health():
    return render_template('health.html', health_status="")


@app.route('/track', methods=['POST'])
def track_health():
    # Retrieve user input from the form
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    blood_pressure = request.form.get('blood_pressure')
    blood_sugar = float(request.form.get('blood_sugar'))

    if (18.5 <= weight / ((height / 100) ** 2) <= 24.9) and (70 <= blood_sugar <= 130):
        health_status = "You are healthy!"
    else:
        health_status = "You may need to consult a healthcare professional."

    return render_template('health.html', health_status=health_status)

@app.route('/deleteuser/<id>')
def deleteuser(id):
    try:
        mycursor = myconn.cursor()
        sql = "DELETE FROM healthcareusers WHERE id=%s"
        data = (id,)
        mycursor.execute(sql, data)
        myconn.commit()

        mycursor1 = myconn.cursor()
        sql = "SELECT * FROM healthcareusers"
        mycursor1.execute(sql)
        myresult = mycursor1.fetchall()

        if myresult:
            return render_template('users.html', users=myresult)
        else:
            return render_template('users.html', users=[])  # Render with an empty list if no users exist
    except Exception as e:
        # Handle any exceptions that may occur during database operations
        return "An error occurred: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
