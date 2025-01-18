from flask import Flask
from flask import redirect, url_for
from flask import render_template

app = Flask(__name__)

from pages.branches.branches import branches
app.register_blueprint(branches)

from pages.contactus.contactsus import contactus
app.register_blueprint(contactus)


from pages.product.product import product
app.register_blueprint(product)

from pages.signin.signin import signin
app.register_blueprint(signin)

from pages.signup.signup import signup
app.register_blueprint(signup)

from pages.useraccount.useraccount import useraccount
app.register_blueprint(useraccount)

from pages.category.category import category
app.register_blueprint(category)
