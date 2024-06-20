'''3 3 possible combinations in the list
i/p: [3,2,5,4,1,6,8]
o/p: (3 2 5) (3 2 4) (3 2 1) (3 2 6) (3 2 8)
'''
def combination(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr,end='')
            return
        for i in range(start,len(l)):
            fun(curr + [l[i]], i+1)
        return
    fun([],0)
a=list(map(int,input().split()))
k=3
combination(a,k)