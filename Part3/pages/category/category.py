from flask import Blueprint, render_template

from Group4.Part3.db_functions import get_jewelry_by_category

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
        return render_template('category.html', category_title=category_data['title'], products=category_data['category'])
    else:
        return "Category not found", 404
@category.route('/')
def homepage_func():
  category_data = categories_data.get('homepage')
  return render_template('category.html', category_title=category_data['title'], products=category_data['category'])

