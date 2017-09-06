from flask import Flask, render_template, redirect, url_for, flash, session
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from Develop.ClassModels.LoginFormClass import LoginFormManager
from Develop.ClassModels.RegistrationFormClass import RegistrationForm
from Develop.ClassModels.my_shopping_list import ShoppingList
from Develop.ClassModels.shoppingListCreationForm import CreateShoppingList
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
                print("WTF")
                flash("You have logged in sucessfully, welcome")
                return redirect(url_for('dashboard'))
            print("Invalid credentials 1")
    else:
        print("Invalid credentials")
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


@app.route("/shopping_list_view", methods=['GET', 'POST'])
def shopping_list_view():
    print()
    return render_template("shopping_list_view.html", shoppinglist=ShoppingList("Back to school", "fSchool"))


@app.route('/createShoppingList', methods=['GET', 'POST'])
def createshoppingList():
    form = CreateShoppingList()
    print(len(current_user.shopping_lists))
    if form.validate_on_submit():
        current_user.create_shopping_list(ShoppingList(form.name.data, form.description.data))
        print(len(current_user.shopping_lists))
        return redirect(url_for('dashboard'))
    return render_template("dashboard.html")


@app.route('/deleteShoppingList')
def deleteshoppinglist(purchased_items=None):
    form = CreateShoppingList()
    current_user.delete_shopping_list(purchased_items.pop(ShoppingList(form.name.data)))

    return render_template("delete_item_view.html")


if __name__ == '__main__':
    app.run(debug=True)
