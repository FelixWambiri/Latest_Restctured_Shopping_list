from flask import Flask, render_template, request, redirect, url_for, flash

from Develop.ClassModels.user import User
from Develop.ClassModels.user_accounts import UsersAccountList
from Develop.templates.formClass import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wabdblabla'
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
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        print(form.errors)
        account.create_users(user)
        flash('You have registered successfully')
        return redirect(url_for('dashboard'))

    print(form.errors)
    return render_template('register.html', form=form)


@app.route('/dashboard', methods=['Get', 'POST'])
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
