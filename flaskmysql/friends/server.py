from flask import Flask,render_template,request,redirect,session,flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

# for displaying results from the table friends
@app.route('/')
def index():
    query = 'select * from friends'
    friends = mysql.query_db(query)

    return render_template('index.html',all_friends = friends)

# for inserting records into table
@app.route('/friends',methods=['POST'])
def create():
    query = 'insert into friends (first_name,last_name,occupation,created_at,updated_at) values(:first_name,:last_name,:occupation,now(),now())'
    data = {
            'first_name': request.form['first_name'],
            'last_name' : request.form['last_name'],
            'occupation':request.form['occupation']
    }
    mysql.query_db(query,data)
    return redirect('/')
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    return redirect('/')

# for updating
@app.route('/friends/<friend_id>/update',methods=['POST'])

def update(friend_id):

    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends)


# delting friend
@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
