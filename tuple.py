a=(1,2,3,4,5,6,7)
print(a)
print(type(a))
print(len(a))
print(a[0])
print(a[-1])
print(a[5:])
print(a[:3])
if 4 in a:
    print("yes")
if 9 in a:
    print("yes")
else:
    print("no")
    
print(list(a))
b=list(a)
b[1]=10
print(b)
b.append(15)
print(b)
b.remove(15)
print(b)
print(tuple(b))
x=b
del x
#print(x)

a=(1,2,3,4,5)#add 2 tuple
print(a)
b=("a","b","c")
print(b)
print(a+b)
print(b*3)

for  i in a:#loop
    print(i)
for i in range(len(a)):
      print(a[i])
i=0
while i<len(a):
    print(a[i])
    i=i+1
d=b.count("c")#count
print(d)
e=b.index("b")
print(e)

    
    
