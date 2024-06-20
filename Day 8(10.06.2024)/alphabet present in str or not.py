''' i/p: "the quick brown fox jumps over the lazy dog"
    o/p: yes
    
    i/p: qwweer yuiop asdfvgh JKL mnbvlkjcxz
    o/p: no
'''
'''s=input()
s=set(s)
if len(s)==27:
    print('yes')
else:
    print('no')'''

'''

i/p: "the 4quick br$^own foENDx j45umps o.ver the lazy dog"
o/p: yes
'''
'''s=input()
s=set(s)
c=0
for i in s:
    if i.islower():
        c+=1
if c==26:
    print('yes')
else:
    print('no')'''

a=input()
'''b="abcdefghijklmnopqrstuvwxyz"
for i in b:
    if(i not in a):
        print("no")
        break
else:
    print("yes")'''

'''for i in range(97,123):
    if chr(i) not in a:
        print('no')
        break
else:
    print('yes')'''
'''d={}
for i in a:
    if i.islower():
        d[i]=1 d.add(i) if set is taken
print(d)'''

d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))
