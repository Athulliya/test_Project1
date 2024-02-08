s={"apple","orange","cherry","apple"}
print(s)
print(len(s))
print(type(s))
for i in s:#for loop
    print(i)
print("apple" in(s))
s.add("banana")
print(s)
r={2,3,4}
s.update(r)#join 2 sets
print(s)
s.remove("banana")
print(s)
s.discard("banana")#remove(error varilla)
print(s)
m=s.pop()
print(m)
print(s)
a={"sum","add","mul","div","modulo",4,5}#difference
b={1,2,3,4,5,"div"}
c=a.difference(b)
print(c)
a.difference_update(b)#diff update
print(a)
f={11,12,1,14,15}#intersection
g={10,12,14,16,18}
e=f.intersection(g)
print(e)
f.intersection_update(g)#intersection update
print(f)
x={"A","S","G",3,6,9,10}#subset
y={3,6,"S"}
z=y.issubset(x)
print(z)
m=y.issuperset(x)
print(y)
n=y.issubset(y)
print(n)
