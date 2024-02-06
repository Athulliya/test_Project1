s={"apple","orange","cherry","apple"}
print(s)
print(len(s))
print(type(s))
for i in s:
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