# import random
# from flask import Flask,session,request,render_template
# app = Flask(__name__)
# app.secret_key='Thisissecret'
#
# @app.route('/',methods=['GET','POST'])
#
# def game():
#     z = random.randrange(0,101)
#     session['z'] = z
#     return render_template('index.html')
# @app.route('/process',methods=['POST'])
# def number():
#     if request.form['submit']=='submit':
#         session['x']= request.form['guess']
#         print session['x']
#         print session['z']
#         return render_template('index.html')
#         return redirect(url_for('/'))
#
#
# app.run(debug=True)

# import random
# from flask import Flask,request,session,render_template
# app =Flask(__name__)
# app.secret
import random
from flask import Flask,session,request,render_template
app = Flask(__name__)
app.secret_key='Thisissecret'

@app.route('/',methods=['GET','POST'])

def game():
    z = random.randrange(0,101)
    session['z'] = z
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def number():
    print type(session['x'])
    print type(session['z'])
    print session['x']
    print session['z']
    session['x']= request.form['guess']
    if request.form['submit']=='submit':
        if int(session['x']) == int(session['z']):
            print "Congrats"
            return render_template("equal.html")

        elif int(session['x']) > int(session['z']):
                print "too high"
                return render_template("index.html",y="toohigh")
        elif int(session['x']) < session['z']:
                print  "too low"
                return render_template("index.html",y="toolow")

    return render_template('index.html')
    return redirect(url_for('/'))


app.run(debug=True)
