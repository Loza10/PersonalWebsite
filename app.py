from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/vitae')
def vitae():
    return render_template('vitae.html')

@app.route('/walkabout')
def walkabout():
    return render_template('walkabout.html')

if __name__ == "__main__":
    app.run(debug=True)