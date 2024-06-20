'''
ip:4-->2n-1=7
op:

  1 1 1 1 1 1 1
  1 2 2 2 2 2 1
  1 2 3 3 3 2 1
  1 2 3 4 3 2 1
  1 2 3 3 3 2 1
  1 2 2 2 2 2 1
  1 1 1 1 1 1 1
'''
n=int(input())
m=2*n-1
k=2
for i in range(m):
    for j in range(m):
        if i==0 or i==m-1 or j==0 or j==m-1:
            print("1",end=" ")
        else:
            print(n-k,end=" ")
    k=k+1
        
    print()
        
        
    
    