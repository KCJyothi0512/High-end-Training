''' i/p: abcd                     longest common subsequence
         axbdc
         
         abcd-> a        b       c     d
                ab       bc      cd
                ac       bd
                ad       bcd
                abc
                abd
                acd
                abcd
    o/p: abd
'''
s1=input()
s2=input()
s=''
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
    print(m)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])

u,v=len(s1),len(s2)
while(u!=0 and v!=0):
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v]==m[u-1][v]):
            u=u-1
        else:
            v=v-1
print("".join(reversed(s)))
    