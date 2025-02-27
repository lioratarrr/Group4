from flask import Blueprint, render_template, session
from db_functions import get_orders, get_info
useraccount = Blueprint(
  'useraccount',
  __name__,
  static_folder='static',
  static_url_path='/useraccount/static',
  template_folder='templates',
)
@useraccount.route('/useraccount')
def user_account_func ():
  email = session.get('email')
  user_orders = get_orders(email)
  info = get_info(email)
  return render_template('useraccount.html', orders=user_orders, info = info)
