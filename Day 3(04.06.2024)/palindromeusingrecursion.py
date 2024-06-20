'''
ip:
    12321 integer input dont conert it into string
    reverse it using recursion and check it is palindrome or not
'''

def rev(n,re):
    if n==0:
        return re
    re=re*10+(n%10)
    return rev(n//10,re)

n=int(input())
if(rev(n,0)==n):
    print("palindrome")
else:
    print("not palindrome")