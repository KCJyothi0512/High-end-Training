'''
i/p: l1 = 6 3 2 9 4 7
     l2 = 8 7 5 3 6 9
o/p: [48,32,40]
'''
def eofun(l1,l2,el,ol,e):
    if e<len(l1):
        if l1[e]%2==0:
            el.append(l1[e])
        if l2[e]%2!=0:
            ol.append(l2[e])
        eofun(l1,l2,el,ol,e+1)
    return (el,ol)

def mfun(el,ol,i,l3):
    if i<len(el):
        def fun(el,ol,j,l3,s):
            if j<len(ol):
                s=s+el[i]+ol[j]
                fun(el,ol,j+1,l3,s)
                return s   #6 3 2 9 4 7 8 7 5 3 6 9
            l3.append(s)
        fun(el,ol,0,l3,0)
        mfun(el,ol,i+1,l3)
    return l3
        
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
el,ol=eofun(l1,l2,[],[],0)
print(el,ol)
print(mfun(el,ol,0,[]))