from flask import Flask,request,render_template,redirect,session,url_for
app = Flask(__name__)
app.secret_key='Thisissecret'
@app.route('/',methods=['GET'])
def incone():
            session['x'] = session['x']+1
            return render_template("index.html")
@app.route('/one',methods=['POST'])
def inctwo():
    if request.form['submit'] == 'two':
            session['x'] = session['x']+1
            return redirect(url_for('incone'))
    elif request.form['submit'] =='reset':
                session['x'] =0
                return redirect(url_for('incone'))
app.run(debug=True)


# @app.route('/reset',methods=['POST'])
# def reset():
#     if request.form['submit'] == 'reset':
#             session['x'] = 1
#             return render_template("index.html")


# def index():
#     session['x'] = session['x']+1
#     return render_template("index.html")
# @app.route('/',methods=['POST'])
# def results():
#     session['x'] = sesion['x']+2
#     return render_template("index.html")
    # if request.method == "POST" :
    #     session['x'] = session['x']+2
    #     return render_template("index.html",x = x)
    #
    # else:


    # if request.form['button'] =='two':
    #     session['x'] = session['x']+2
    # # return redirect(url_for('index'))
    #     return render_template("index.html")
    # else:
        # session['x'] = session['x']+1
        # return render_template("index.html")
        # if request.form['button'] =='two':
        #     session['x'] = session['x']+2
        #     return render_template("index.html")
        # else:
        #     return render_template("index.html")
# @app.route('/ninjas',methods = ['GET'])
# def ninjas():
#     session['x'] = session['x']+1
#     return render_template("index.html")
#     if request.form['button'] =
# @app.route('/show')
# def show():
#
    # return redirect('/')
