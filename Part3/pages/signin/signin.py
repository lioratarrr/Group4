from flask import Blueprint, render_template, session, jsonify, request, redirect, url_for
from utilities.db.db_connector import *


signin = Blueprint(
  'signin',
  __name__,
  static_folder='static',
  static_url_path='/signin/static',
  template_folder='templates',
)

@signin.route('/signin', methods=['GET', 'POST'])
def sign_in_func():
    if request.method == "GET":
        return render_template('signin.html')

    # Check if the incoming request is JSON
    if request.is_json:
        data = request.get_json()  # Get the JSON data

        # Extract email and password from the JSON
        email = data.get('email')
        password = data.get('password')

        # Perform DB check
        if verify_user_login(email, password):
            session['email'] = email
            first_name = get_first_name(email)
            session ['first-name'] = first_name
            session['logged_in'] = True
            print(f"Logged in as {email}")
            return jsonify({
                'status': 'success',
                'message': 'הכניסה בוצעה בהצלחה',  # Login successful
                'redirect': '/'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'לא נמצא משתמש עם כתובת אימייל זו או שהסיסמא שגויה'  # Incorrect email or password
            }), 400
    else:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400


@signin.route('/logout')
def logout_func():
    session['logged_in'] = False
    session['email'] = None
    return redirect('/')
