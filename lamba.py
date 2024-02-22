x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(5,5))

z=lambda a,b,c:a+b+c
print(z(1,2,3))

def myfunction(n):
    return lambda a:a*n
f=myfunction(2)
print(f(11))

#lambda sorting
list=[("apple",15),("orange",10),("grapes",6),("cherry",54)]
r=sorted(list,key=lambda x:x[1])
print(r)
    
    
    
    
    