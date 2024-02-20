n=int(input("enter your number"))#factorial
def factorial(numbers):
    if numbers==1:
        return 1
    else:
        return(numbers*factorial(numbers-1))
    
    
result=factorial(n)
print(result)








        
