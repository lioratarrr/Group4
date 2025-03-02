from flask import Flask
from flask import session
from flask import request
app = Flask(__name__)
app.secret_key = '1234'
# Import and register blueprints for different pages
from pages.branches.branches import branches
app.register_blueprint(branches)
# Import and register the 'contact us' blueprint
from pages.contactus.contactsus import contactus
app.register_blueprint(contactus)

# Import and register the 'product' blueprint
from pages.product.product import product
app.register_blueprint(product)
# Import and register the 'sign in' blueprint
from pages.signin.signin import signin
app.register_blueprint(signin)
# Import and register the 'sign up' blueprint
from pages.signup.signup import signup
app.register_blueprint(signup)
# Import and register the 'sign up' blueprint
from pages.useraccount.useraccount import useraccount
app.register_blueprint(useraccount)
# Import and register the 'category' blueprint
from pages.category.category import category
app.register_blueprint(category)
# Import and register the 'post sign-up' blueprint
from pages.postsignup.postsignup import postsignup
app.register_blueprint(postsignup)

from db_functions import *

