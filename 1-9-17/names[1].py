students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for x in range(0,len(students)):
    temp = students[x]
    fname = temp["first_name"]
    lname = temp["last_name"]
    print fname,lname
