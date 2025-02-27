from flask import Blueprint, render_template
import random
from db_functions import get_jewelry_by_category, get_all_jewelries, get_branches
category = Blueprint(
  'category',
  __name__,
  static_folder='static',
  static_url_path='/category/static',
  template_folder='templates',
)

from flask import Flask, render_template

app = Flask(__name__)

@category.route('/category/<category_name>')
def category_func(category_name):
    # Check if the category exists in categories_data
    category_data = get_jewelry_by_category(category_name)
    if category_data['category']:
        branchesdata = get_branches()
        return render_template('category.html', category_title=category_data['title'], products=category_data['category'], branches = branchesdata)
    else:
        return "Category not found", 404
@category.route('/')
def homepage_func():
  all_jewelries = get_all_jewelries()
  # Select 5 random items from the fetched list
  random_jewelries = random.sample(all_jewelries, 5) if len(all_jewelries) >= 5 else all_jewelries
  # Render the homepage with random jewelry items
  branchesdata = get_branches()
  return render_template('category.html', products=random_jewelries, branches = branchesdata)

