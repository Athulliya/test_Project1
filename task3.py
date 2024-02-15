num=int(input("enter your number"))
if (num%2)==0:
    print("even")
else:
    print("odd")
list1=[10,15,20,25,30,35,40]
list2=[]
list3=[]
a=0
b=0
for i in list1:
    if i%2==0:
     list2.append(i)
     a=a+1    
    else:
        list3.append(i)
        b=b+1
print(list3)
print(list2)
print(a)
print(b)



num=int(input("enter your number"))
if num==1:
    print("not prime")
elif num>1:
    for i in range(2,num):
        if num%i==0:
         print("not prime")
         break
    else:
           print("prime")
else:
    print(" prime Not")       



    