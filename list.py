fruits=["apple","mango","cherry","grapes","guava","plum"]#list
print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[1])
print(fruits[-1])
print(fruits[2:5])
if "apple" in fruits:
    print("yes")
else:
    print("no")
    
fruits[1]="banana"#replace an item
print(fruits)
fruits[1:3]="pear","chikko"
print(fruits)
fruits[1:3]=["watermelon"]
print(fruits)
fruits.insert(2,"orange")#insert
print(fruits)
fruits.insert(8,"pine")
print(fruits)
fruits.append("pineapple")#append
print(fruits)

vegetables=["onion","pea","chilly","potato"]
fruits.extend(vegetables)#join two list
print(fruits)

fruits.remove("apple")#remove an element from list
print(fruits)

fruits.pop(2)#remove based on index position
print(fruits)

fruits.pop()#remove last element from list
print(fruits)

del fruits[-1]#remove values
print(fruits)

fruits.clear()#clear whole content
print(fruits)

#del fruits
#print(fruits)

vegetables=["onion","pea","carrot"]#join
print(vegetables)
seeds=["flax","chia","mustard","pumkin"]
vegetables.extend(seeds)
print(vegetables)

frnds=["akku","ammu","minnu"]
frndz1=["chinnu","ciya","kathu"]
s=frnds + frndz1
print(s)

frndz2=frnds.copy()#copy
print(frndz2)

frnds.sort(reverse=True)#reverse
print(frnds)

frnds.sort()
print(frnds)

