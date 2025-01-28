from flask import Blueprint, render_template
from flask import redirect, url_for
from flask import session
from flask import request


signin = Blueprint(
  'signin',
  __name__,
  static_folder='static',
  static_url_path='/signin/static',
  template_folder='templates',
)
@signin.route('/signin', methods = ['GET','POST'])
def sign_in_func ():
  if request.method == "GET":
    return render_template('signin.html')

  email = request.form['email']
  password = request.form['password']

  #DB CHECK

  session['email'] = email
  session['logged_in'] = True
  print (email, password)
  return redirect('/')

@signin.route('/logout')
def logout_func():
  session['logged_in'] = False
  session['email'] = None
  return redirect('/')


