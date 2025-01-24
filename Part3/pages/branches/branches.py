from flask import Blueprint, render_template

from Group4.Part3.db_functions import get_branches

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

