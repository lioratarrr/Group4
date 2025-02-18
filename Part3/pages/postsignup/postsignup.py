from flask import Blueprint, render_template
from flask import request, session, redirect, url_for
from Group4.Part3.db_functions import insert_user_data
postsignup = Blueprint(
  'postsignup',
  __name__,
  static_folder='static',
  static_url_path='/postsignup/static',
  template_folder='templates',
)
@postsignup.route('/postsignup', methods = ['GET', 'POST'])
def postsignup_func ():
  if request.method == 'GET':
    return render_template('postsignup.html')
  #   SAVE IN DB
  print ("all good here")
  city = request.form['city']
  address = request.form['address']
  aptnum = request.form['aptnum']
  phonenum = request.form['phonenum']
  email = session.get('email')
  firstname = session.get('first-name')
  lastname = session.get('last-name')
  password = session.get('password')
  insert_user_data(firstname, lastname, email, password, city, address, aptnum, phonenum)


  session['logged_in'] = True
  return redirect('/')


