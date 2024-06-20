'''strong password
  ip:
    asd123!@#                              ip:                     ip:
  op:                                         A1234b                    a123456
    1(Add 1 character to make it valid)    op:                     op:
                                               2                         2
  ip:                                                              ip:
    123456789                            ip:                           abcdef127
  op:                                        A1234a@4              op:
    3                                      op:                         2
  ip:                                          -1
    ab                                  ip:
  op:                                      1234567
    6                                  op:3
'''                                       

str=input()
u,l,d,s=0,0,0,0

for i in str:
    if i.isupper():
        u=1
    elif i.islower():
        l=1
    elif i.isdigit():
        d=1
    elif not i.isalnum():#else:
        s=1
'''c=u+l+d+s
n=len(str)
if n>=8:
    if c==4:
        print("-1")
    else:
        print(4-c)
else:
    k=8-n
    a=4-c
    print(max(k,a))'''

m=4-(u+l+d+s)
if (len(n)+m)<8:
    print(8-len(n))
else:
    if m==0 and len(n)>=8:
        print("-1")
    else:
        print(m)
    