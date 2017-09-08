from flask import Flask, render_template, redirect, url_for, flash, session
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from Develop.ClassModels.LoginFormClass import LoginFormManager
from Develop.ClassModels.RegistrationFormClass import RegistrationForm
from Develop.ClassModels.additemform import AddItemsManager
from Develop.ClassModels.deleteitemform import DeleteItemsManager
from Develop.ClassModels.items import Item
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
    if form.validate_on_submit():

        if account.view_users(form.username.data):
            if form.password.data == account.view_users(form.username.data).password:
                login_user(account.view_users(form.username.data))
                flash("You have logged in sucessfully, welcome")
                return redirect(url_for('dashboard'))
            flash("Invalid credentials 1")
        print(form.errors)

    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(username):
    return account.view_users(username)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        try:
            account.create_users(user)
        except KeyError:
            flash("User name is already taken")
        return redirect(url_for('login'))

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
    if form.validate_on_submit():
        current_user.create_shopping_list(ShoppingList(form.name.data, form.description.data))
        print(len(current_user.shopping_lists))
        return render_template("create_shopping_list.html")
    return render_template("create_shopping_list.html")


@app.route('/deleteShoppingList', methods=['GET', 'POST'])
def deleteshoppinglist():
    form = DeleteItemsManager()
    current_user.delete_shopping_list(form.name.data)

    return render_template("delete_item_view.html", form=form)


@app.route("/add_item/<shopping_list_name>", methods=['GET', 'POST'])
def add_item(shopping_list_name):
    form = AddItemsManager()
    if form.validate_on_submit():

        item = Item(form.item_name.data, form.item_price.data,
                    form.item_quantity.data)

        shopping_list = current_user.view_shopping_list(shopping_list_name)
        shopping_list.add_item(item)
        current_user.update_shopping_list(shopping_list)
        flash(" " + item.name +
              " was added into Shopping List " +
              shopping_list_name)

        return redirect(url_for('dashboard'))

    else:
        return render_template("add_item.html", form=form,
                               shopping_list_name=shopping_list_name)


@app.route("/delete_item/<shopping_list_name>/<name>", methods=['GET', 'POST'])
def delete_item(shopping_list_name, name):
    if current_user.is_authenticated:
        current_user.get_shopping_list(shopping_list_name).remove_item(name)
        flash(name + " Deleted Successfully ", "success")

        return redirect(url_for('index'))


"""@app.route('/createItems', methods=['GET', 'POST'])
def CreateListofItems():
    form = CreateListofItems()
    if form.validate_on_submit():
        current_user.create_shopping_list(ShoppingList(form.name.data, form.description.data))
        print(len(current_user.shopping_lists))
        return redirect(url_for('dashboard'))
    return render_template("dashboard.html")"""

if __name__ == '__main__':
    app.run(debug=True)
