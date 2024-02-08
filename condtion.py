if 3>2:
    print("yes")
else:
    print("no")
num=int(input("enter the number"))
if num>0:
    print("positive no")
elif num<0:
    print("negative")
else:
    print("zero")
    
a=8
b=4
if a>b and b<2:
    print("false")
else:
    print("yes")
    
#nested if
num=float(input("enter the no:"))
if num>=0:
 if num==0:
     print("zero")
 else:
     print("positive")
else:
    print("negative")