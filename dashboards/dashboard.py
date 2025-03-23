from flask import Blueprint, render_template

dashboard_blueprints = Blueprint('dashboard', __name__, template_folder='templates')



@dashboard_blueprints.route('/dashboard')
def projeto():
    return render_template('dashboard.html')