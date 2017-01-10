                #Averaging the values in a list

a = [1,2,5,10,255,3]
sum =0
for x in range(0,len(a)):
    sum = sum+a[x]
avg = sum/len(a)
print avg,"is the average of the list"
print sum, "is the sum of the list"
