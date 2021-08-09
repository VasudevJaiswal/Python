


# 01. Method  for finding percentage

marks = [45,78,86,77]
Percentage = (sum(marks)/400)*100
print(Percentage)

# 02.  Method for finding percentage
marks1 = [75,98,88,78]
p2 = (sum(marks1)/400)*100
print(p2)

# If programmer don't know function then he use to find percentage this method

# 03.  Method for finding percentage
marks2 = [75,98,88,78]
p2 = ((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100
print(p2)



# *******************************************************************

# Chapter 8 – Functions and Recursions

# A function is a group of statements performing a specific task.

# When a program gets bigger in size and its complexity grows, it gets difficult for a programmer to keep track of which piece of code is doing what!

# A function can be reused by the programmer in a given program any number of times.



# Percentage finding Using Function   - Very Important points 

def percent(marks):
    p = (sum(marks)/400)*100
    return p

marks1 = [45,78,86,77]
percentage1 = percent(marks1)    # We call the function - percent

marks2 = [75,98,88,78]
percentage2 = percent(marks2)     # We call the function - percent



print(percentage1,percentage2)


# result of the function 
# 71.5 84.75  

# That's very easy way to call a  funtion to evalute a program 




# Example and Syntax of a function  :

# The syntax of a function looks as follows:

def func1():
	print(“Hello”)

    
'''Note: This function can be called any number of times, anywhere in the program.'''

'''Function call :

Whenever we want to call a function, we put the name of the function followed by parenthesis as follows:
func1()      #This is called function call
'''


# Types of functions in Python
# There are two types of functions in Python:

# Built-in functions #Already present in Python
# User-defined functions #Defined by the user

# Examples of built-in function includes len(), print(), range(), etc.

# The func1() function we defined is an example of a user-defined function.