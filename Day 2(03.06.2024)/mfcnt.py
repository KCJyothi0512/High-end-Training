'''
i/p: "MMFFMFFMFMFMFFMMFFMMF"  remember this  count-negative(F),count-positive(M),count-0(equal)
'''
a=input()
b=a.count('M')
c=a.count('F')
if b==c:
    print('0')
elif b>c:
    print('M')
else:
    print('F')