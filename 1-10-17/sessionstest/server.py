from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = "Thisissecret"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users',methods=['POST'])
def users():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['address'] = request.form['address']
    return redirect('/show')
@app.route('/show')
def show_user():
    return render_template("users.html",name=session['name'],email=session['email'],address=session['address'])
app.run(debug=True)
