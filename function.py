def athulliya():
  print("hello")
athulliya()
    
def name(firstname,lastname):
    print(firstname+ "  "+lastname)
name("athulliya","george")

def mango(*child):#arbitrary argument
    print("hello"+ " "+child[2])
mango("akash","athulliya","ananth")

def myfunction(kid1,kid2,kid3):#keyword argument
    print("hello"+ kid2)
myfunction(kid1="anu",kid2="anna",kid3="minnu")

def new(**kid):#arbitrary keyword argument
    print("hello"+ " "+kid["lastname"])
new(firstname="ammu",lastname="anuja")

fruits=["apple","orange","cherry","banana"]#all elements calling
def food(veg):
    for i in veg:
        print(i)
food(fruits)

def number(i):
    return 5*i
print(number(7))

a=int(input("enter your no:"))#sum
b=int(input("enter your no:"))
def sum(c,d):
    return c+d
print(sum(a,b))

list1=[1,2,3,4,5]
def sum(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
sum(list1)


list2=[1,2,3,4,5]
def mul(numbers):
    mul=1
    for i in numbers:
        mul=mul*i
    print(mul)
mul(list2)


list3=[1,2,3,2,4,3,5]
def num(numbers):
    list4=[]
    for i in numbers:
        if i  not in list4:
          list4.append(i)
    print(list4)
num(list3)


wow="india is my country"
    
def vowels(alpha):
    a=0
    b=0
    hai="a","e","i","o","u","A","E","I","O","U"
    for i in alpha:
        if i in hai:
         a=a+1
        else:
            b=b+1
    print(a)
    print(b)
vowels(wow)
            

            
    



    
