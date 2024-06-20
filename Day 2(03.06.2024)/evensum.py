'''def fac(x):
    if(x==1):
        return 1
    return x * fac(x-1)#return fac(x-1) o/p 1 it will come check by tracing it
n=int(input())
print(fac(n))'''

'''ip:10
   op:sum of even numbers using recursion'''

def even_sum(x):
    if (x==0):
        return 0
    return x+even_sum(x-2)

n=13
if(n%2==0):
    print(even_sum(n))
else:
    print(even_sum(n-1))