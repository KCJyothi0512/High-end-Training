'''
i/p: tu5g2k1h8
     g5g8gd6h3
o/p:
     865312 take unique numbers from the strings and get largest even number
'''
'''s1=input()
s2=input()
s=set()
for i in s1:
    if i.isdigit():
        s.add(int(i))
        
for i in s2:
    if i.isdigit():
        s.add(int(i))

s=list(s)
s.sort(reverse=True)

for i in range(len(s)-1,-1,-1):
    if s[i]%2==0:
        t=s[i]
        s.remove(s[i])
        break

s.append(t)
js="".join(map(str,s))
print(int(js))'''

a=input()
b=input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
    if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop())
            print(''.join(d))
            break
    else:
        print('-1')