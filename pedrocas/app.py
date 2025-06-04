from flask import flask, render_template

app = Flask(__name__)

@app.route('/redsenha')
def index():
    return render_template('senha.html')

@app.route('/dois_fatores')
def index():
    return render_template('dois_fatores.html')