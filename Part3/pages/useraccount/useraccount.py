from flask import Blueprint, render_template

useraccount = Blueprint(
  'useraccount',
  __name__,
  static_folder='static',
  static_url_path='/useraccount/static',
  template_folder='templates',
)
@useraccount.route('/useraccount')
def user_account_func ():
  return render_template('useraccount.html')
