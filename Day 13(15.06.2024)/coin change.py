'''i/p:[4,3,7]    [3,4,5] [3,4]
       16          7       5    multiples,% 7 divisible by 3, 7 divisible by 4, 7 is divisible by 3+4
   o/p: 4                  -1
'''
def coin():
    l1=[-1]*(n+1)    #[-1,-1,-1,-1,-1,-1,-1,-1]
    l1[0]=0          #[0,-1,-1,-1,-1,-1,-1,-1]
    for i in l: #i=coin
        for j in range(1,n+1): #j= [0,-1,-1,-1,-1,-1,-1] #(i,n+1)
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=list(map(int,input().split()))
n=int(input())
coin()