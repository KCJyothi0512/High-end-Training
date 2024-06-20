'''
i/p: 4
     t u e d   if u r unable to bring out the value use global var,update it and bring out
     f b o w  # 79 - leetcode 
     
     
'''
'''def fun(i,j,k,t):
    if k==len(s):
        return 1
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]:
        return
    if a[i][j]==s[k]:
        a[i][j]=0
    t=fun
for i in range(n):
    for j in range(n):
        if (a[i][j]==s[0]):
            fun(i,j,1)'''
s="worx"
l=[['t','u','e','s'],['s','w','d','f'],['r','o','a','b'],['d','s','d','q']]
for i in range(len(l)):
    for j in range(len(l[i])) :
        if l[i][j]=='w':
            i2,j2=i,j
            break
k=0
def word(l,i,j,s,k):
    if i<0 or j<0 or i>=len(l) or j>=len(l)   or k>len(s)-1 or l[i][j]!=s[k]  :
        return  
    elif l[i][j]==s[k] :
        k+=1
        if k==len(s):
            print(k)
            return k  
              
        else :
            word(l,i+1,j,s,k)
            word(l,i,j-1,s,k)
            word(l,i-1,j,s,k)
            word(l,i,j+1,s,k)
             
   
    
res=word(l,i2,j2,s,k)
print(res)
if res:
    print("yes")
else :
    print("no")
    