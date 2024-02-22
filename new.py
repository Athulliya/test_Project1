x=open("new.txt","r")#readmode
#print(x.read())
#print(x.read(4))#read 4 letters
#print(x.readline())
#print(x.readline())
x.close()

y=open("new.txt","a")#append mode
y.write("\n i am living in adoor")
y.close()

z=open("new.txt","r")
#print(z.read())


d=open("new.txt","w")
d.write("welcome to adoor")
d.close()

e=open("new.txt","r")
print(e.read())

import os
os.remove("new.txt")