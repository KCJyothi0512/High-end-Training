'''
i/p: "abfgresagtyuiofde" print len of longest substring without repeating characters
o/p: 12
'''
a=input()
d={}
s=""
i=0
m=0
while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)