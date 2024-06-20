'''
   ip:
     "xyzabcdefklmnopqefgh:
     print the lenght of longest sub string who has the alphabets in sequence
     sliding window algorithm  for i in range(len(s)-1): -1 is mandatory and at last the condition should be
     if(c>m):
    m=c
    for any problem different conditions
'''

s=input()
c,m=1,0
for i in range(len(s)-1):
    if (ord(s[i+1])-ord(s[i])==1):
        c=c+1
    else:
        if(c>m): 
            m=c#m=max(c,m)
        c=1
if(c>m):
    m=c
print(m)