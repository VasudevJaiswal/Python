# Recursion
# Recursion is a function which calls itself.

# It is used to directly use a mathematical formula as a function. For example:

# factorial(n) = n * factorial(n-1)
# This function can be defined as follows:

# n! = 1 *2 * 3*4--------*n
n  = 4
product  = 0
for i in range(n):
    product = product * (i+1)
    print(product)



2. 

# '''def factorial(n):
# 	if i == 0 or i == 1 : #Base condition which doesn’t call the function any further
# 		return i
# 	else:
# 		return n*factorial(n-1) #Function calling itself'''