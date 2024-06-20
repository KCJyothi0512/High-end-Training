'''i/p: 4x3 (recursion)  (r,c)
   o/p:_ _ _ _
       _ _ _ _
       _ _ _ _                               
'''
'''def fun(i,j,c,k):
    if (i>0 or i>=n or j<0 or  j>=m or (i==k and j==l)): 
        return c
    if(i==m-1 amd j==n-1):
        c+=1 #path here only
        return c
    v.append((i,j))
    if((i-1,j)not in v):
        c=fun(i-1,j,c)
    if((i,j-1)not in v):
        c=fun(i,j-1,c)
    if((i+1,j)not in v):
        c=fun(i+1,j,c)
    if((i,j+1)not in v):
        c=fun(i,j+1,c)
    v.pop()
    return c
r=int(input())
c=int(input())
l=[]
for i in range(r):
    k=['_']*c
    l.append(k)
print(l)
print'''
def fun(i,j,n,m,c,vi):
    if i < 0 or j < 0 or i >= n or j >= m:
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,n,m,c,vi)#top
        
    if((i,j-1) not in vi):
        c=fun(i,j-1,n,m,c,vi)
        
    if((i,j+1) not in vi):
        c=fun(i,j+1,n,m,c,vi)
        
    if((i+1,j) not in vi):
        c=fun(i+1,j,n,m,c,vi)
    print(vi.pop(),end=" ")
    return c

r=int(input())
c=int(input())
l=[]
for i in range(r):
    k=['-']*c
    l.append(k)
    
print(l)
t=fun(0,0,r,c,0,[])
print()
print(t)