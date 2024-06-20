'''
  ip:
    [4,7,1,4,1,3]--->foods
    3---->no:of rats
    5---->units of food 1 rat can consume
'''

l=list(map(int,input().split()))
n=int(input())
u=int(input())
un=n*u
for i in range(len(l)):
    un=un-l[i]
    if un<1:
        break
print(un,i)  
print("no:of unvisited houses:",len(l)-(i+1))
