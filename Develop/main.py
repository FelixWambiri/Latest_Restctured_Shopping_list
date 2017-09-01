from flask import Flask, render_template, request, redirect, url_for

from Develop.ClassModels.user import User
from Develop.ClassModels.user_accounts import UsersAccountList

app = Flask(__name__)
account = UsersAccountList()


@app.route('/', methods=['Get', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user_name']
        password = request.form['password']
        if account.view_users(username):
            if account.view_users(username).password == password:
                return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['password']
        username = request.form['user_name']
        myuser = User(username, email, password)
        account.create_users(myuser)

        return redirect(url_for('dashboard'))
        """" Hi " + account.view_users(username).username + " Welcome to \My Shoppinglist App"""
    return render_template('register.html')


@app.route('/dashboard', methods=['Get', 'POST'])
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
