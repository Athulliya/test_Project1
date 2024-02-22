import re
x="rain in spain"
y=re.findall("ai",x)
print(y)
u=re.findall("re",x)
print(u)


c=re.search("i",x)
print(c.start())


f=re.split("\s",x)#spacing
print(f)

h=re.split("\s",x,1)
print(h)


j=re.sub("\s","2",x)
print(j)



