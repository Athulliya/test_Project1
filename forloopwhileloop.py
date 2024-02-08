a=["sun","moon","venus","mars",5,6,7]#forloop
for i in a:
    print(i)
b="apple"
for i in b:
    print(i)
for i in a:
    print(i)
    if i==5:
       break
for i in a:
    if i==5:
        continue
    print(i)
    
    
    #range
for i in range(5):
    print(i)
for i in range(2,6):#continous value range kanan comma use cheyyum
    print(i)
for i in range(2,10,3):#stepsize
 print(i)
 
 #whileloop
 i=0
 while i<6:
     print(i)
     if i==3:
        break
     i+=1
     
i=0
while i<5:
    i+=1
    if i==3:
     continue
    print(i)

    
