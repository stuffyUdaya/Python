# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.



def multiply(a,c):
    b=[ ]
    for x in range(0,len(a)):
        temp = a[x]*c
        b.append(temp)
    print b
multiply([2,4,10,16],5)













# arr = [2,3,4]
# arr1=[]
# for x in range(0,len(arr)):
#     temp =arr[x]*4
#     arr1.append(temp)
#     print arr1
