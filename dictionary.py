dict1={"name":"ammu","age":12, "place":"kannur"}
print(dict1)
print(dict1["name"])
print(len(dict1))
print(type(dict1))
a=dict1.get("age")
print(a)
b=dict1.keys()#keys print cheyyan
print(b)
c=dict1.values()#values print cheyan
print(c)
d=dict1.items()#keyvalue pair
print(d)
dict1["age"]=16#age change cheyyan
print(dict1["age"])
dict1.update({"phn":7655789999})#update method
print(dict1)
dict1.update({"name":"amal"})
print(dict1)
dict1.pop("age")#delete
print(dict1)
dict1.popitem()#last keyvalue pair delete
print(dict1)
del dict1["name"]
print(dict1)
#dict1.clear()
dict2=dict1.copy()#copy
print(dict2)
dict1.clear()
print(dict1)
dict3={"flower":"rose","rupees":10,"color":"black"}#key print akan
for i in dict3:
    print(dict3[i])#value print akan
for i in dict3.values():
    print(i)
for i in dict3.keys():
    print(i)
for i,j in dict3.items():#key value print akan
    print(i,j)
#nested dictionary
myfamily={"child1":{"name":"akash","age":34},
          "child2":{"name":"akku","age":34},
          "child3":{"name":"vinu","age":22}}
print(myfamily)
print(myfamily["child2"]['age'])
