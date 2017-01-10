arr = [3,5,7,8]
for x in range(len(arr)-1,0):
    arr[x] = arr[x+1]

    print arr

# def shift(arr):
#     arr.pop(0)
#     arr.append(0)
#     return arr
# print shift([1,2,3,4])
