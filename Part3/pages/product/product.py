from flask import Blueprint, render_template

product = Blueprint(
  'product',
  __name__,
  static_folder='static',
  static_url_path='/product/static',
  template_folder='templates',
)
# @product.route('/product')
# def product_func ():
#   return render_template('product.html')
@product.route('/product')
def product_func1():
  return render_template('product.html')

@product.route('/product/<product_id>')
def product_func(product_id):
    # Here, you would query the database for the product details based on product_id
    product_data = {
        'name': product_id,
        'description': 'This is a detailed description of the product.',
        'image': '/static/jewelery/example.png',
    }
    return render_template('product.html', product=product_data)
