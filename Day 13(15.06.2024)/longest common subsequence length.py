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
    o/p: abd - 3
'''
s1='abcd'
s2='axbdc'
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])