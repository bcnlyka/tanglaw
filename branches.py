from flask import Flask, render_template, url_for, redirect, request
import pymysql

app = Flask(__name__)

con = pymysql.connect("localhost", "root", "", "branches-tanglaw")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    if request.form['password'] == 'admin' and request.form['email'] == 'admin@tanglaw.com':
        return render_template('index/admin.html')

    if request.form['password'] == 'vp' and request.form['email'] == 'vp@tanglaw.com':
        return render_template('index/vp.html')

    if request.form['password'] == 'registrar' and request.form['email'] == 'registrar@tanglaw.com':
        return render_template('index/registrar.html')

    if request.form['password'] == 'registrar' and request.form['email'] == 'registrar@tanglaw.com':
        return render_template('index/registrar.html')

    else:
        return 'Invalid email or password'


if __name__ == '__main__':
    app.run(debug=True)
