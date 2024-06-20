'''
   ip:             ip:
     3                 4
     xyz                  abcd
     pqr                  xyze
     abc                  pqrw
     "yraxpazr"           stuv
   op:                  "cyptdzsayq"
      yes           op:
                         no
'''

n=int(input())
m=[]

for i in range(n):
    m.append(list(input()))
print(m)
s=input()
f=0

for i in range(len(s)):
    if s[i] in m[i%n]:
        m[i%n].remove(s[i])
        print(m[i%n])
        continue
    else:
        f=1
        break
if f==1:
    print("NO")
else:
    print("YES")
    
    


