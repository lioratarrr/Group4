from flask import Blueprint, render_template
from flask import request, session, redirect, url_for
postsignup = Blueprint(
  'postsignup',
  __name__,
  static_folder='static',
  static_url_path='/postsignup/static',
  template_folder='templates',
)
@postsignup.route('/postsignup', methods = ['GET', 'POST'])
def postsignup_func ():
  if request.method == 'GET':
    return render_template('postsignup.html')

  #   SAVE IN DB
  session['logged_in'] = True
  return redirect('/')


