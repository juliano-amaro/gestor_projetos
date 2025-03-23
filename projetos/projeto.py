from flask import Blueprint, render_template

projeto_blueprints = Blueprint('projetos', __name__, template_folder='templates')

@projeto_blueprints.route('/projeto')
def projeto():
    return render_template('index_projeto.html')