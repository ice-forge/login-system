from flask import Blueprint, render_template, session, redirect, url_for

api = Blueprint('api', __name__)

@api.route('/', methods = ['GET'])
def api_page():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template('api/api.html')
