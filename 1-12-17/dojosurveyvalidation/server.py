from flask import Flask, render_template, request, redirect,flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def process():
    if len(request.form['name'])<1:
        flash("Name cannot be Empty!!!")
        return render_template("index.html")
    elif len(request.form['comment'])<1:
        flash("comments cannot be Empty!!!!")
        return render_template("index.html")
    elif len(request.form['comment'])>120:
            flash("Comments could not be more than 120 characters")
            return render_template("index.html")
    else:
            name=request.form['name']
            loc=request.form['loc']
            favlan=request.form['favlan']
            comment=request.form['comment']
            return render_template('results.html',name=name,loc=loc,favlan=favlan,comment=comment)
app.run(debug=True)
