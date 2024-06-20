'''
i/p: [(1,3) (2,5) (4,6) (6,7) (5,8) (7,9)] 1,3 4,6 6,7 7,9    (2,5)->6  (5,8)->11 => 11+6=17
     [5,6,5,4,11,2]                                  #j-0 to i-1  i-1 to len(l) j-updated i-original list b[j]+a[i]>b[i] b[i]=b[j]+a[i]
o/p: 17 '''                       
#j[1]<i[0]  j==i-1 i+=1 j[1]is not less than i[0] j+=1
job=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(job)):
    for j in range(0,i):
        if (job[j][1]<=job[i][0]):
           if (b[j]+a[i]>b[i]):
               b[i]=b[j]+a[i]
#print(b)
print(max(b))