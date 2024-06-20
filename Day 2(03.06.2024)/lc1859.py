#leetcode 1859
a=input().split()
res=[0]*len(a)
for i in a:
    res[int(i[-1])-1]=i[:-1]
return ''.join(res)