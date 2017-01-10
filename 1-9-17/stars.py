def stars(x):
    for i in range(0,len(x)):

        if type(x[i])== int:
            print x[i]*"*"
        elif type(x[i])== str:

            temp =x[i].lower()
            length = len(temp)
            temp = temp[0]
            print temp * length

stars([2,3,4,"Tom","Developer"])
