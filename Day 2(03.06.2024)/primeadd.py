'''a=int(input())
def digit_sum(a):
    sum=0
    while a!=0:
        rem=a%10
        num=a//10
        sum=sum+rem
    if sum>=10:
        return sum
    else:
        return digit_sum(a)
print(digit_sum(a))'''
'''
n=input()
m=sum(list(map(int,n)))
'''
'''n=543
   m=map(int,n)
print(m) map->returns object
but if you convert into list [4,5,3] m=list(map(int,n))

   
n=input()
m=sum(list(map(int,list(n))))
    '''
def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if (n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
while():
    
    if(n<10):
        m=pnp(n)
        
    else:
        while(1):
            n=add(n)
            if(n<10):
                break
        print(pnp(n))