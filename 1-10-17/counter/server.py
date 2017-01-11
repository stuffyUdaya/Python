from flask import Flask,request,render_template,redirect,session
app = Flask(__name__)
app.secret_key='Thisissecret'
@app.route('/',methods=['GET'])
def index():
    session['x']=0
    session['x'] = session['x']+1;

    return render_template("index.html")
# @app.route('/show')
# def show():
#
    # return redirect('/')

app.run(debug=True)
