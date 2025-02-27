from flask import Blueprint, render_template, session, request, jsonify
from db_functions import get_branches, save_order

product = Blueprint(
  'product',
  __name__,
  static_folder='static',
  static_url_path='/product/static',
  template_folder='templates',
)

@product.route('/product')
def product_func1():
  return render_template('product.html')

@product.route('/product/<product_id>')
def product_func(product_id):
    product_data = {
        'name': product_id,
        'description': 'This is a detailed description of the product.',
        'image': '/static/jewelery/example.png',
    }
    branchesdata = get_branches()
    return render_template('product.html', product=product_data,branches = branchesdata)

@product.route('/save_order', methods=['POST'])
def save_order_func():
  # Get JSON data from the request
  data = request.get_json()
  # Extract fields from the received data
  product_name = data.get('productName')
  color = data.get('color')
  quantity = data.get('quantity')
  branch = data.get('branch')
  pickup = data.get ('pickup')

  # Check if user is logged in (via session)
  if not session.get('logged_in'):
    return jsonify({'status': 'error', 'message': 'User not logged in'}), 401

  # Retrieve user email from session
  email = session['email']

  # Prepare order data
  order_data = {
    'email': email,
    'product_name': product_name,
    'color': color,
    'quantity': quantity,
    'branch': branch,
    'pickup': pickup,
    'status': 'reserved',  # Example status
  }

  # Try saving order data (replace with your actual DB function)
  try:
    if save_order(order_data):
      return jsonify({'status': 'success', 'message': 'Order saved successfully'})
    else:
      return jsonify({'status': 'error', 'message': 'Failed to save order'}), 500
  except Exception as e:
    return jsonify({'status': 'error', 'message': f'Error saving order: {str(e)}'}), 500
