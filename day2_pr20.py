#recursion example 34
def sum_of_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural(n-1)
n=int(input())
print(sum_of_natural(n))
