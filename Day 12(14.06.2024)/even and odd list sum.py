'''
i/p: [6,3,2,9,4,7]
     [8,7,5,3,6,9]
     6+7=13  2+7=9
     6+5=11  2+5=7
     6+3=9   2+3=5
     6+9=15  2+9=11
o/p: [13,11,9,15,9,7,5,11,11,9,7,13] sum of even number in list 1 and odd numbers in list 2
'''
'''def eosum(l1,l2,el,ol,e):
    if e<len(l1):
        if l1[e]%2==0:
            el.append(l1[e])
def mfun(el,ol,i,l3):
    if i<len(el):
        def fun(el,ol,j,l3,s):
            if j<len(ol):
                s=s+el[i]+ol[j]
                fun(el,ol,j+1,l3,s)
            l3.append(s)
        fun(el,ol,0,l3,0)
        mfun(el,ol,i+1,l3)
    return l3

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
el,ol=eosum(l1,l2,[],[],0) 
print(el,ol)'''
'''
use recursions
ip:
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
size of both lists same

o/p:generate another list all
    6+7=13    2+7=9
    6+5=11    2+5=7
    6+3=9     2+3=5
    6+9=15    2+9=11
    
    [13,11,9,15,9,7,5,11,11,9,7,13]
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
        def fun(el,ol,j,l3):
            if j<len(ol):
                s=el[i]+ol[j]
                l3.append(s)
                fun(el,ol,j+1,l3)
        fun(el,ol,0,l3)
        mfun(el,ol,i+1,l3)
    return l3
        
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
el,ol=eofun(l1,l2,[],[],0)
print(el,ol)
print(mfun(el,ol,0,[]))