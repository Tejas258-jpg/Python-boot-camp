N=int(input())
def check(num):
    num=str(num)
    twos=num.count('2')
    fours=num.count('4')
    eights=num.count('8')
    return twos==fours==eights and twos>0
def increment(N):
    count=0
    for num in range(1,N+1):
        if(check(num)):
            count+=1
    return count
print(increment(N))
