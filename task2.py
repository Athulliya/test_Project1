x=["chicken","noodles","beef","mutton","pork"]
print(x)
print(len(x))
print(type(x))
print(x[1])
print(x[2:5])
print(x[4:])
if "beef" in x:
    print("yes")
else:
    print("no")
x[1]="curry"
print(x)
x.insert(2,"kuruma")
print(x)
x.append("egg")
print(x)
x.remove("curry")
print(x)

y=["maths","physics","chemistry","botany","english"]
print(y)
print(len(y))
x.extend(y)
print(x)
x.sort()
print(x)
