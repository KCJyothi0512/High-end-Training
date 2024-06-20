''' i/p: [4,9,8,2,14,3,5,6]
          4 8 9 2 14 3 5 6
            2 8 9 14 3 5 6     a[0]=min(9,8,1)
              8 9 14 3 5 6     a[2]=max(9,8,1)
                3 9 14 5 6     a[1]=s-max-min
                  5 9 14 6
                    6 9 14
    o/p :[4,2,8,3,5,6,9,14]
'''
l=list(map(int,input().split()))
for i in range(len(l)-2):
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
    if(l[i+1]>l[i+2]):
        l[i+1],l[i+2]=l[i+2],l[i+1]
    if(l[i]>l[i+1]):
         l[i],l[i+1]=l[i+1],l[i]
print(l)