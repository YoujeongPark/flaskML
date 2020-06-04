from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def home():
    return render_template('test.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == "__main__":
    app.run(debug=True)