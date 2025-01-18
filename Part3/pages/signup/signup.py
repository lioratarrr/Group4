from flask import Blueprint, render_template

signup = Blueprint(
  'signup',
  __name__,
  static_folder='static',
  static_url_path='/signup/static',
  template_folder='templates',
)
@signup.route('/signup')
def sign_up_func ():
  return render_template('signup.html')
