from flask import Blueprint, render_template
from flask import request, session, redirect, url_for

signup = Blueprint(
  'signup',
  __name__,
  static_folder='static',
  static_url_path='/signup/static',
  template_folder='templates',
)
@signup.route('/signup', methods = ['GET','POST'])
def sign_up_func ():
  if request.method == "GET":
    return render_template('signup.html')

  email = request.form['email']
  password = request.form['password']
  firstname = request.form['first-name']
  lastname = request.form['last-name']

  # DB CHECK

  session['email'] = email
  session['first-name'] = firstname
  session['last-name'] = lastname
  session['password'] = password
  return redirect('/postsignup')
