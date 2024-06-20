#path and cost
'''def dfs(d,x,s):
    l.append(x)
    if x==2:
        print(l,s)
        #return          
    for i,j in d[x]:
        if(i not in l):
            dfs(d,i,s=s+j)
    l.pop() 
d={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,6),(2,3)],8:[(3,5),(4,6),(2,2)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,2)]}
l=[]
dfs(d,5,0)'''

def dfs(d,x,e,c):
    l.append(x)
    if x==e:
        print(l,c)
        l.pop()
        return c
    for i in d[x]:
        if(i[0]  not in l):
            dfs(d,i[0],e,c+i[1])
    l.pop()
d={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,6),(2,3)],8:[(3,5),(4,6),(2,2)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,2)]}
l=[]
print(dfs(d,5,2,0))

