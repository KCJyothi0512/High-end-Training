'''i/p: 5
        0 1 0 0 1
        1 0 0 1 1     1-land, 0-water
        0 0 0 0 0
        1 0 0 0 0
        1 0 0 0 1
    o/p:
        5
'''
#l=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
'''def fun(i,j,c):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=1:
        return c
    a[i][j]=2
    c=fun(i,j-1,c)   
    c=fun(i,j+1,c)
    c=fun(i-1,j,c)
    c=fun(i+1,j,c)
a=[][]
cnt=0
n=5
m=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            k=fun(i,j,0)
            if k>m:
                m=k
            cnt+=1
print(cnt,m)'''

def fun(i, j, c):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return c
    a[i][j] = 2
    c += 1
    c = fun(i, j-1, c)
    c = fun(i, j+1, c)
    c = fun(i-1, j, c)
    c = fun(i+1, j, c)
    return c

a = [[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n = 5
co = 0
m = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            k = fun(i, j, 0)
            if k>m:
                m=k
            co+=1
print(co, m)