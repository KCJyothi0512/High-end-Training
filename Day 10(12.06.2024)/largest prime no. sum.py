'''
i/p: [4,8,14,22,36,68]                                  i/p: [14,16,20,22]
non -prime nos 4-8 (largest prime no. between 4 to 8)          0+19+0=19
       7 13 19 13 67 = 137                              o/p: 19
       o/p: 137
''' #sliding window algorithm

def isprime(x):
    for i in range(2,x//2+1):
        if(x%i==0):
            return 0
    return 1
def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
l=list(map(int,input().split()))
s=0
for i in range(len(l)-1):
    s=s+lprime(l[i],l[i+1])
print(s)