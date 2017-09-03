from flask import Flask, render_template, redirect, url_for, flash
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from Develop.ClassModels.LoginFormClass import LoginFormManager
from Develop.ClassModels.RegistrationFormClass import RegistrationForm
from Develop.ClassModels.user import User
from Develop.ClassModels.user_accounts import UsersAccountList

app = Flask(__name__)
app.config['SECRET_KEY'] = "wabdabwahh"
login_manager = LoginManager()
login_manager.init_app(app)

account = UsersAccountList()


@app.route('/', methods=['Get', 'POST'])
def login():
    form = LoginFormManager()
    error = None
    if form.validate_on_submit():

        if account.view_users(form.username.data):
            if form.password.data == account.view_users(form.username.data).password:
                login_user(account.view_users(form.username.data))
                flash("You have logged in sucessfully, welcome")
                return redirect(url_for('dashboard'))
    else:
        error = 'Invalid credentials'
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(usename):
    return account.view_users(usename)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        account.create_users(user)
        flash('You have registered successfully')
        return redirect(url_for('dashboard'))

    return render_template('register.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
