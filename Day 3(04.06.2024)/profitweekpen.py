'''
   ip:
   max profit you get
    list
     5 3 2 7  8  4
     m t w th f  s
    price of pen increases/decre
    you can buy and sell any day-->if you buy this week you should sell in this week
    so you cant sell monday buy on sat
    op:
       6-->buy wed sell friday
       
       
 o(n*n)
 o(n)
 o(n logn)
 
ip:5 4 2 9 7 1    9 8 7 6 5 4     5 3 2 7 8 4      15 3 2 7 8 4         5 4 2 9 1 1
op:7              0               6                 6                    7
'''

l=list(map(int,input().split()))
pr=0
b=l[0]
for i in (1,len(l)):
    if b>i:
        b=i
    else:
        if pr<b-i:
            pr=b-i
print(pr)


'''mn=min(l)
#print(mn)

mi=l.index(mn)
#print(mi)

if mi==len(l)-1:
    mn=min(l[:mi])
    mi=l.index(mn)

maxn=max(l[mi:])
#print(maxn)

profit=maxn-mn
print(profit)'''



'''
brute-force approach-->time waste
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]<a[j] and a[j]-a[i]>pr):
            pr=a[j]-a[i]
            
print(pr)'''







