'''i/p: [2,5,2,3,6,7,1,0,5,7]   i/p:[4,3,4,5,6,1,0,6,7]
   o/p: 20                      o/p: 12
'''
'''def trap(height):
       if not height:return True
       l=0
       res=0
       r=len(height)-1
       maxl=height[l]
       maxr=height[r]
       while(l<r):
           if maxl<maxr:
               l+=1
               maxl=max(maxl,height[l])
               res+=maxl-height[l]
           else:
                r-=1
                maxr=max(maxr,height[r])
                res+=maxr-height[r]
       return res
height=list(map(int,input().split()))
ans=trap(height)
print(ans)'''

h=list(map(int,input().split())) 
l=[0]*len(h)
r=[0]*len(h)
m=0
for i in range(len(h)):
    if(h[i]>m):
        m=h[i]
    l[i]=m
m1=0
for i in range(len(h)-1,-1,-1):
    if(h[i]>m1):
        m1=h[i]
    r[i]=m1
print(l,r)
s=0
for i in range(len(h)):
    s=s+abs(min(l[i],r[i])-h[i])
print(s)