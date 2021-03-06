from flask import Flask,render_template,request,redirect,session,flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?!.*[^a-zA-Z0-9])(.{8,15})$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="ThisisSecret"
mysql = MySQLConnector(app,'walldb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=['POST'])
def create():
    flashMessage = False
    if len(request.form['first_name'])<1 or str.isalpha(str(request.form['first_name'])) == False:
        flash("required First Name")
        flashMessage = True
    elif len(request.form['last_name'])<1 or str.isalpha(str(request.form['last_name'])) == False:
        flash("required Last Name")
        flashMessage = True
    elif len(request.form['password'])<8:
        flash("password must be atleast 8 characters",'error')
        flashMessage = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("not a valid email address")
        flashMessage = True
    elif request.form['password']!=request.form['passwordconf']:
        flash("Password and Confirmation password are not matched")
        flashMessage = True
    elif not PWD_REGEX.match(request.form['password']):
        flash("Password must contain atleast one Uppercase and a number!!","error")
        flashMessage = True
    if flashMessage == True :
        return redirect('/')


    else:

        flash("successfully registered ")
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        print pw_hash
        query = 'insert into users(first_name,last_name,email,password,created_at,updated_at) values(:first_name,:last_name,:email,:pw_hash,now(),now())'
        data = {
                'first_name': first_name ,
                'last_name' : last_name,
                'email':email,
                'pw_hash':pw_hash


        }

        newreg = mysql.query_db(query,data)
        print 33333555555
        session['newfirst_name']=request.form['first_name']
        query1 = "select id from users where email=:email"
        query_data={'email':email}
        session['id'] = mysql.query_db(query1,query_data)
        print session['id']
        session['newid']= session['id'][0].get('id')
        print session['newid']

        return redirect('/showwall')

@app.route('/process',methods=['POST'])
def process():
    email = request.form['log_email']
    password = request.form['log_password']
    user_query = "SELECT * FROM users WHERE users.email = :email"
    query_data = { 'email': email }

    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    print user[0]
    if bcrypt.check_password_hash(user[0]['password'], password):
        query = "select first_name from users where email=:email"
        session['first_name'] = mysql.query_db(query,query_data)
        # query1 = "select id drom users where email=:email"
        # session['id'] = mysql.query_db(query1,query_data)
        print 33333
        print session['first_name']
        session['newfirst_name']=session['first_name'][0].get('first_name')
        print 333333333
        print session['newfirst_name']
        query = "select id from users where email=:email"
        session['id'] = mysql.query_db(query,query_data)
        print session['id']
        session['newid']= user[0].get('id')
        print session['newid']
        return redirect('/showwall')

    else:
        flash("incorrect credentials")
        return redirect('/')

@app.route('/wall')
def wall():
    return render_template('wall.html')
@app.route('/logout',methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/mymessage',methods=['POST','GET'])
def message():
    message=request.form['message']
    print message
    user_id = session['newid']
    query = 'insert into messages(message,created_at,updated_at,user_id) values(:message,now(),now(),:user_id)'
    data = {
            'message': message ,
            'user_id':user_id,
            }
    session['messages']=mysql.query_db(query,data)
    print session['messages']
    query1 = 'select id from messages where user_id=:user_id'
    query_data = {'user_id':user_id}
    session['messageid']=mysql.query_db(query1,query_data)
    # session['message_id']=session['messageid']
    # print session['message_id']


    return redirect('/showwall')
@app.route('/showwall')
def showwall():
    query = "select users.first_name as users_name,messages.message,messages.updated_at from messages join users on users.id=messages.user_id "
    messages = mysql.query_db(query)
    # query = "select message.id as message_id ,message.user_id as user_id from messages "
    # newmessages = mysql.query_db(query)
    # print newmessages

    # query="select comments.comment,comments.user_id from comments join messages on messages.id = comments.message_id join users "

    query = "select users.first_name as users_name,comments.comment,comments.updated_at from comments join users on users.id=comments.user_id join messages on messages.id = comments.message_id"
    comments = mysql.query_db(query)
    return render_template('wall.html',all_messages=messages,all_comments=comments)
# def showcomments():
    # query = "select users.first_name as users_name,comments.comment,comments.updated_at from comments join users on users.id=comments.user_id join messages on messages.id = comments.message_id"
    # comments = mysql.query_db(query)
    # return render_template('wall.html',all_comments=comments)



@app.route('/comments',methods=['POST'])
def comment():
        query = "select messages.id as message_id from messages "
        session['message_id']=mysql.query_db(query)
        message_id=session['message_id']
        user_id =session['newid']
        comment=request.form['comment']
        query = 'insert into comments(comment,created_at,updated_at,user_id,message_id) values(:comment,now(),now(),:user_id,:message_id)'
        data = {
                'comment':comment,
                'user_id':user_id,
                'message_id':message_id,

        }
        session['comments']=mysql.query_db(query,data)
        return redirect('/showwall')
app.run(debug=True)
