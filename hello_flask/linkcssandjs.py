from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def test():
    return render_template("test.html")
app.run(debug=True)
