from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results',methods=['POST'])
def results():
    name=request.form['name']
    loc=request.form['loc']
    favlan=request.form['favlan']
    comment=request.form['comment']
    return render_template('results.html',name=name,loc=loc,favlan=favlan,comment=comment)
app.run(debug=True)
