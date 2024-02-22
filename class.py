class a:#class
    x=5
    #print(a)
b=a()#here b is object
print(b.x)#obj.variable




class y:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("hello"+self.name)
z=y("anna",44)
z.display()   
#print(z.name)  
#print(z.age)  



#inheritance
class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def show(self):
        print(self.firstname,self.lastname)
p=person("ammu","chikku")
p.show()



class child(person):
    pass
t=child("anu","ammmu")
t.show()