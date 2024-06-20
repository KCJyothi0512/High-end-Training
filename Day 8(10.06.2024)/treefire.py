'''
i/p: 6
     0 1 1 1 0 1
     0 1 0 1 0 0                        (i-1,j)          i<0,j<0,i>=n,j>=n
     1 0 1 1 0 0
     0 0 0 1 1 1                (i,j-1) (i,j) (i,j+1)
     1 1 0 0 0 1
     1 1 1 0 1 0                        (i+1,j)
     4 6
o/p: 8
'''
'''l=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
            fun(l,i,j,n)
def fun(l,i,j,n):
    if l[i][j]==1:
        l[i][j]=0
    if l[i][j]==0:
        return
    if j>0:
        fun(l,i,j+1,n)
    if j<n-1:
        fun(l,i,j-1,n)
    if i>0:
        fun(l,i-1,j,n)
    if i<n-1:
        fun(l,i+1,j,n)'''
'''def fun(i,j):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=1:
        return
    if a[i][j]==1:
        a[i][j]=2
    fun(i-1,j)
    fun(i,j-1)
    fun(i+1,j)
    fun(i,j+1)
    return
fun(i,j)
c=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            c+=1'''
'''
ip:
  1->trees
  0->land
  6
  0 1 1 1 0 1                               (i-1,j)
  0 1 0 1 0 0                                
  1 0 1 1 0 0                        (i,j-1)  (i,j)   (i,j+1)
  0 0 0 1 1 1
  1 1 0 0 0 1                                (i+1,j)
  1 1 1 0 1 0
  
  4 6-->4th row 5th col
  fire does not catch diagonally
  op:8

'''

def fun(arr,n,r,c):
    if r<0 or c<0 or r>=n or c>=n or arr[r][c]!=1:
        return

    if arr[r][c]==1:
        arr[r][c]=2
        fun(arr,n,r-1,c)#top
        fun(arr,n,r,c-1)#left
        fun(arr,n,r,c+1)#right
        fun(arr,n,r+1,c)#bottom
        
        
n=int(input())
arr=[]
for i in range(n):
    col=[]
    for j in range(n):
        val=int(input())
        col.append(val)
    arr.append(col)
print(arr)
r=int(input())
c=int(input())

fun(arr,n,r,c)
print(arr)

ct=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            ct+=1
print(ct)