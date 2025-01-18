from flask import Blueprint, render_template
from flask import redirect, url_for

signin = Blueprint(
  'signin',
  __name__,
  static_folder='static',
  static_url_path='/signin/static',
  template_folder='templates',
)
@signin.route('/signin')
def sign_in_func ():
  return render_template('signin.html')
