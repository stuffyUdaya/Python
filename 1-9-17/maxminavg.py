arr = [3,4,9,8]
max = arr[0]
min = arr[0]
sum = 0
for x in range(0,len(arr)):
    if(arr[x] > max):
        max = arr[x]
    if(arr[x]<min):
        min = arr[x]
    sum = sum+arr[x]
    avg = sum/len(arr)
print max
print min
print sum
print avg
