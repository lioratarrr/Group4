from datetime import datetime
from flask import Blueprint, render_template, session, redirect,flash, url_for, request, jsonify
from utilities.db.db_connector import get_info,get_orders, mydatabase, delete_order_by_id, update_user_info, delete_order_by_id


useraccount = Blueprint(
  'useraccount',
  __name__,
  static_folder='static',
  static_url_path='/useraccount/static',
  template_folder='templates',
)
@useraccount.route('/useraccount')
def user_account_func():
    email = session.get('email')
    user_orders = get_orders(email)
    info = get_info(email)
    return render_template('useraccount.html', orders=user_orders, info=info)


@useraccount.route('/update_user', methods=['POST'])
def update_user():
    try:
        data = request.get_json()  # Get the JSON data from the request
        field = data.get('field')  # The field to update
        new_value = data.get('new_value')  # The new value to set

        email = session.get('email')  # Get the user's email from the session

        # Call the function to update the user info in the database
        result = update_user_info(email, field, new_value)

        if result and result.modified_count > 0:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Failed to update information'})

    except Exception as e:
        # Return a 500 error with the exception details
        return jsonify({'success': False, 'message': f"Error: {str(e)}"}), 500


from bson.objectid import ObjectId


@useraccount.route('/delete_order', methods=['POST'])
def delete_order():
  try:
    # Get the data from the incoming JSON request
    data = request.get_json()
    order_id = data.get("order_id")  # Get the order_id from the JSON body

    if not order_id:
      return jsonify({'success': False, 'message': 'Missing order ID'}), 400

    # Call the function to delete the order from the database
    success, message = delete_order_by_id(order_id)

    if success:
      return jsonify({'success': True, 'message': message})
    else:
      return jsonify({'success': False, 'message': message}), 404

  except Exception as e:
    return jsonify({'success': False, 'message': f"Error: {str(e)}"}), 500
