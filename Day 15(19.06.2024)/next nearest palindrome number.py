'''
i/p: 122                                    2) 1234        3)24     4) 1112      5) 7654     6) 56472
o/p:
     131 (next nearest palindrome)             1331          33        1221         7667        56565
'''
'''def rev(n,re):
    if n==0:
        return re
    re=re*10+(n%10)
    return rev(n//10,re)

def fun(n):
    if(rev(n,0)==n):
        print(n)
    else:
        n=n+1
        fun(n)
n=int(input())
fun(n)'''

n=input()
