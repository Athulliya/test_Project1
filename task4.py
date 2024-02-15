a="india is my country"#countof vowel and consonant
b=["a","A","e","E","i","I","o","O","u","U"]
x=0
y=0
for i in a:
    if i in b:
        x=x+1
    else:
        y=y+1
print(x)
print(y)

d=input("enter your name")#palindrome or not
c=d[::-1]
print(c)
if c==d:
    print("palindrome")
else:
    print("not palindrome")

#pattern printing
for i in range(6):
    for j in range(i):
     print(i,end="      ")#row spacing
    print("    ")
    
#star pattern
for i in range(6):
    for j in range(i):
        print("*",end="   ")
    print("     ")
    
#number pattern
for i in range(6):
    for j in range(1,i+1):
        print(j,end="   ")
    print("    ")
    
#nested dictionary
dict1={
    "person1":{"name":"anu","age":12,"place":"adoor"},
    "person2":{"name":"ammu","age":32,"place":"kochi"},
    "person3":{"name":"anu","age":12,"place":"adoor"}}
print(dict1)
print()
    
               

    

    
    





