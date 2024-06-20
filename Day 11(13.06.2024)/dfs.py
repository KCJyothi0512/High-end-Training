'''def dfs(d,l,x):
    l.append(x)
    #print(l)
    for i in d[x]:
        if(i not in l):
            dfs(d,l,i)
    return l
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
print(dfs(d,l,5))'''

def dfs(d,x):
    l.append(x)
    for i in d[x]:
        if(i not in l):
            dfs(d,i)
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
dfs(d,5)
print(l)