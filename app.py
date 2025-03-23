from flask import Flask, render_template
from projetos.projeto import projeto_blueprints
from dashboards.dashboard import dashboard_blueprints

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(dashboard_blueprints)
app.register_blueprint(projeto_blueprints)

if __name__ == '__main__':
    app.run(debug=True)