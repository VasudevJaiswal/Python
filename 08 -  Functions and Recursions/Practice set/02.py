# Problem 1. Write a program using the function to find the greatest of three numbers.

def maximum(num1,num2,num3):
    if(num1>num2):
        return num1
    else:
        return num2
    
    if(num2>num3):
        return num2
    else:
        return num3

    if(num3>num1):
        return num3
    else:
        return num1


m = maximum(10,20,3)
print("The value of the maximum is: " +str(m))
