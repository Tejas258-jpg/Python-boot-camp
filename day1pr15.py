#function within a funtion
def check(ele):           
    return ele%2==0
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
    return count
arr=[5,6,8,9,3,4,2]
print(increment(arr))
