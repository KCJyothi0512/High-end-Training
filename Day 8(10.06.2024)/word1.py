s="fans"
l=[['t','u','e','s'],['e','b','o','b'],['a','o','o','c'],['d','e','k','f']]

for i in range(len(l)):
    for j in range(len(l[i])) :
        if l[i][j]=='f':
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
            
              
        else :
            word(l,i+1,j,s,k)
            word(l,i,j-1,s,k)
            word(l,i-1,j,s,k)
            word(l,i,j+1,s,k)
        return k  
             
   
    
res=word(l,i2,j2,s,k)
print(res)
if res:
    print("yes")
else :
    print("no")