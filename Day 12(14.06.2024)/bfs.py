'''def bfs(d,x):
     vis = [x]
     queue = [x]
     while len(queue) != 0:
       ele = queue.pop(0)
       print(ele, end=", ")
       for i in d[ele]:
          if i not in vis:
              vis.append(i)
              queue.append(i)
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
bfs(d,5)'''

'''def bfs(d,x):
    v=[]
    q=[x]
    while(len(q)!=0): 
        for i in d[q[0]]: 
            if i not in v and i not in q:
                q.append(i)
        v.append(q[0])  
        q.pop(0)        
    return v
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
print(bfs(d,5))'''

def bfs(d,n):
    v=[]
    q=[n]
    while(q):
        for i in d[q[0]]: #d[n]
            if(i not in q and i not in v):
                q.append(i)
        v.append(q.pop(0))
    print(v)
#d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
d={1:[2,5],2:[1,3],3:[2,4],4:[3,5,6,10],5:[1,4],6:[4,7,9],7:[6,8],8:[7],9:[6],10:[4,11],11:[10]}
bfs(d,1)