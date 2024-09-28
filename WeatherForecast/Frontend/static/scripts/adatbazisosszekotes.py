from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 's3cr3t'

# MySQL konfiguráció
app.config['MYSQL_HOST'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'weather'
app.config['MYSQL_DB'] = 'adatbazis'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Ellenőrizzük az adatbázisban
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM weather_forecast WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        flash('Sikeres bejelentkezés!')
        return redirect(url_for('index')) # Itt átirányítunk a index oldalra
    else:
        flash('Hibás felhasználónév vagy jelszó.')
        return redirect(url_for('home'))

@app.route('/index')
def weather_forecast():
    return render_template('weather_forecast.html')  # Ez a te HTML fájlod

if __name__ == '__main__':
    app.run(debug=True)
