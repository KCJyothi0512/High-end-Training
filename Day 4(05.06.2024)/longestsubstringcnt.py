'''
i/p: xyzabcdefklmnopqefgh
o/p: 7
'''
s=input()
c,m=1,0
for i in range(len(s)-1):
    if i+1<len(s):
        if ord(s[i])==ord(s[i+1])-1:
          c+=1
        else:
          if c>m:
              m=c
          c=1
if c>m:
    m=c
print(m)