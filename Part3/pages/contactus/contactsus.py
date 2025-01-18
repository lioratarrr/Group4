from flask import Blueprint, render_template

contactus = Blueprint(
  'contactus',
  __name__,
  static_folder='static',
  static_url_path='/contactus/static',
  template_folder='templates',
)
@contactus.route('/contactus')
def contact_us_func ():
  return render_template('contactus.html')

