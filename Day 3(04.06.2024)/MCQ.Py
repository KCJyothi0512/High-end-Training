'''a=[6,5,7,3,2]
a.append([5,8])
a.extend([4,2,1])
a.append(78)
print(len(a))
print(a)



a=[6,5,7,3,2]
a.append([5,8])
a.extend([4,2,1])
a.extend(78)--->extend will not work for integer or floats only work for sequences,strings
a.extend([2])
print(len(a))
print(a)

a=[6,5,7,3,2]
a.append([5,8])
a.extend([4,2,1])
a.extend('7.8')
a.extend("hi")
print(len(a))
print(a)'''


'''a={5,5.0,'5',3,2}
print(len(a))
--->op:4
{2,3,'5',5.0}-->duplicate elements:5,5.0'''

'''a={5,5.2,'5',(5,2),[5,2],(2,5)}
print(a)

o/p:error
set does not allow a list to be inside it and set,dictionary is also not allowed inside a set'''


a={5,1,'5',(5,2),1,(2,5),"hi",'hi',True,False}
print(a)
print(len(a))

a={5,1,'5',(5,2),1,(5,2),"hi",'hi',True,False}
print(a)
print(len(a))

