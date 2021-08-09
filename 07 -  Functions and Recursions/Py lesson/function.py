# Chapter 8 – Functions and Recursions

# A function is a group of statements performing a specific task.

# When a program gets bigger in size and its complexity grows, it gets difficult for a programmer to keep track of which piece of code is doing what!

# A function can be reused by the programmer in a given program any number of times.




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


