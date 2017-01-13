import random
import datetime
from flask import Flask,request,session,render_template,url_for
from datetime import datetime
app = Flask(__name__)
app.secret_key='Thisissecret'
@app.route('/',methods=['GET','POST'])
def gold():

    gold=0
    session['gold']=gold
    # session['farmg']=0
    # session['caveg']=0
    # session['houseg']=0
    # session['farmactivities']=[]
    # session['caveactivities']=[]
    # session['houseactivities']=[]
    # session['casinoactivities']=[]
    # session['farmnowactivities']=[]
    return render_template("index.html")
@app.route('/process_money',methods=['POST'])
def earngold():
    if request.form['building']=='farm':
            d={"earnedfarm":session['farmg'],"farmtime":session['farmnow']}
            session['d']==d
            print d
            session['farmg'] = random.randrange(9,21)
            session['farmnow'] = datetime.now()
            print session['farmnow']


            # session['farmactivities'].append(session['farmg'])
            session['gold'] = session['gold']+session['farmg']
            return render_template("index.html")
#     elif request.form['building']=='cave':
#             session['caveg'] = random.randrange(4,11)
#             session['caveactivities'].append(session['caveg'])
#             session['gold']=session['gold']+session['caveg']
#             return render_template("index.html")
#     elif request.form['building']=='house':
#             session['houseg'] = random.randrange(1,6)
#             session['houseactivities'].append(session['houseg'])
#             session['gold']=session['gold']+session['houseg']
#             return render_template("index.html")
#     elif request.form['building']=='casino':
#             session['casinog'] = random.randrange(0,51)
#             session['casinoactivities'].append(session['casinog'])
#             session['gold']=session['gold']+session['casinog']
#             return render_template("index.html")
#     # return render_template("index.html")
#
app.run(debug=True)
