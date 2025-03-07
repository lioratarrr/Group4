from flask import Blueprint, render_template

from utilities.db.db_connector import get_branches

# Define a Flask blueprint for the branches page
branches = Blueprint(
  'branches',
  __name__,
  static_folder='static',
  static_url_path='/branches/static',
  template_folder='templates',
)
@branches.route('/branches')
def branches_func ():
  branchesdata = get_branches()
  return render_template('branches.html', branches = branchesdata)

