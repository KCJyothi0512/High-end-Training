'''i/p: 2 5 7 9
     1 3 6 7 10 13
o/p:
[1, 2, 3, 5, 6, 7, 7, 9, 10, 13]'''

'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
arr=a+b
arr.sort()
print(arr)'''

a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=len(a)
n=len(b)
res=[]
i,j=0,0
while i<m and j<n:
    if a[i]<b[j]:
        res.append(a[i])
        i=i+1
    else:
        res.append(b[j])
        j=j+1
'''while j<len(b):
    res.append(b[j])
    j=j+1
while i<len(a):
    res.append(a[i])
    i=i+1'''
if j<len(b):
    res.extend(b[j:])
if i<len(a):
    res.extend(a[i:])
print(res)