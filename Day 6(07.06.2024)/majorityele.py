'''
i/p: [4,8,2,4,4,8,4]   i/p:[2,1,2,2]  i/p: [6,6,6,6,7]  i/p:[1,1,1,2,2,1]
o/p: 4                 o/p: 2         o/p: 6            o/p: 1  (more than half of the count)
'''
'''l=list(map(int,input().split()))
n=len(l)//2
a=[]
for i in range(len(l)):
    a.append(l.count(l[i]))
    if a[i]>n:
        print(l[i])
        break'''
'''max=0
for i in a:
    if (a.count(i)>max):
        max=a.count(i)
        p=i
print(p)'''
'''c=1  a[i]==w: c+=1 i+=1 a[i]!=w: c-=1 c=0 w.replace(a[i]) if c==0: c+=1
w=4'''
l=list(map(int,input().split()))
c=1
p=l[0]
for i in range(1,len(l)):
    if l[i]==p:
        c+=1
    else:
        c-=1
        if c==0:
            c+=1
            p=l[i]
print(p)
            