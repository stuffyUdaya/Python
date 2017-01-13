from flask import Flask,request,redirect,render_template,flash,url_for
app = Flask(__name__)
app.secret_key="Thisissecret"
@app.route('/')
def noninjas():
    x="No ninjas here"
    return render_template('index.html',x=x)
@app.route('/ninja')
def ninjaturtles():
    return render_template('ninjaturtles.html')
@app.route('/ninja/<ninja_color>')
def show_ninja(ninja_color):

        return render_template('index.html',ninja_color=ninja_color)
app.run(debug=True)
