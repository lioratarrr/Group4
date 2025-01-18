from flask import Blueprint, render_template

branches = Blueprint(
  'branches',
  __name__,
  static_folder='static',
  static_url_path='/branches/static',
  template_folder='templates',
)
@branches.route('/branches')
def branches_func ():
  return render_template('branches.html')

