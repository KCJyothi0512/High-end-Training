''' i/p: 7
         0 5 3 6 7 2 1
    o/p: 4'''

n=int(input())
a=list(map(int,input().split()))
'''for i in range(len(b)):
    if i not in b:
        print(i)
        break'''

b=sum(a)
n=(n*(n+1))//2
print(n-b)