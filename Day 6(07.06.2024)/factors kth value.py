'''i/p:12 (1,2,3,4,6,12)
       3
   o/p: 4
'''
n=int(input())
k=int(input())  #TC: o(1)
c=1
if k==1:
    print(n)
else:
    i=n//2
    while i>0:
        if n%i==0:
            c+=1
            if k==c:
                print(i)
                break
        i=i-1