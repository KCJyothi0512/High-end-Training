'''
 ip:
 4
 op:
 ----a----
 ---aba---
 --abcba--
 -abcdcba-
'''

n=int(input())
k=97
for i in range(n,0,-1):
    for j in range(i):
        print("_",end=" ")
        
    a=97
    for b in range(n-i):
        print(chr(a),end=" ")
        a=a+1
        
    print(chr(a),end=" ")
    
    for b in range(n-i):
        print(chr(a-1),end=" ")
        a=a-1
        
    for m in range(i):
        print("_",end=" ")
    print()
    
    