from flask import Blueprint, render_template
from flask import request, session, redirect, url_for, jsonify
from db_functions import email_exists

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

@signup.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    if email_exists(email):  # Check if email already exists
        return jsonify({'exists': True})
    return jsonify({'exists': False})
