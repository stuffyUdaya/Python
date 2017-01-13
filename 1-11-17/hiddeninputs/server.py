from flask import Flask,render_template,request,session
app = Flask(__name__)
@app.route('/',methods=['GET'])
def form():
        return render_template("index.html")
@app.route('/process',methods=['POST'])
def form1():
        print request.form['action']


        if request.form['action'] == 'register':
            name = request.form['first_name']
            return render_template("register.html",name=name)
        elif request.form['action'] == 'login':
            email = request.form['email']
            return render_template("login.html",email=email)
app.run(debug=True)
