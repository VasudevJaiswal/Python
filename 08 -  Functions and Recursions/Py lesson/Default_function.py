Default Parameter Value

We can have a value as the default argument in a function.

If we specify name = “stranger” in the line containing def, this value is used when no argument is passed.

For Example:

def greet(name=’stranger’):
	#function body
greet()                       #Name will be ‘stranger’ in function body(default)

greet(“Harry”)        #Name will be “Harry” in function body(passed)