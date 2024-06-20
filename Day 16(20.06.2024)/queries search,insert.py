'''
ip:7---->no:of queries                       op:                 ip:
   1 school                                      True              1 car
   1 world                                       False             1 cap
   1 word                                        True              2 ca
   1 scholar                                                       3 ca
   2 word                                                          1 can
   2 wood                                                          3 ca
   3 sch                                                           
   
   1--->insert the word
   2--->search for the given word
   3--->search for the word with given prefix
   4--->remove the word
   
   
   5
1
word
1
word
3
wo
4
word
['word']
2
word

'''

'''n=int(input())
l=[]
res=[]
for i in range(n):
    a=int(input())
    b=input()
    if a==1:
        l.append(b)
    elif a==2:
        if b in l:
            res.append("True")
        else:
            res.append("False")
    else:
        le=len(b)
        c=''
        for i in range(len(l)):
            t=l[i]
            c=c+t[0:len(b)]
            print(b,c)
            if b==c:
                res.append("True")
                break
        else:
            res.append("False")
            
        

print(res)'''

n=int(input())
l=[]
res=[]
dc=[]
co=0
for i in range(n):
    a=int(input())
    b=input()
    if a==1:
        l.append(b)
    elif a==2:
        if b in l:
            res.append("True")
        else:
            res.append("False")
    elif a==4:
        for i in l:
            if i==b:
                l.remove(i)
            print(l)
    else:
        le=len(b)
        c=''
        for i in range(len(l)):
            t=l[i]
            c=c+t[0:len(b)]
            if b==c:
                if l[i] not in dc:
                    co=co+1
                    dc.append(l[i])
            c=''
            
        

print(l,res,co)