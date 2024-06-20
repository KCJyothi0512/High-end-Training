''' i/p:
         2
         polikujmnhytgbvfredcxswqaz
         abcd
         qwryupcsfoghjkldezxvbintma
         ativedoc
    o/p:
         bdca
         codevita'''
'''n=int(input())
for i in range(n):
    s=input()
    str=input()
    l=[]
    for i in str:
      l.append(s.index(i))
    print(l)
    l.sort()
    for i in l:
        print(s[i],end='')'''
n=int(input())
b=[]
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if (i in c):
            s=s+(i*count(i))
    print(s)
    n=n-1