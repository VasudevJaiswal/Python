'''Problem 3. Write a python program using the function to convert Celsius to Fahrenheit.'''

def farh(cel):
    return (cel *(9/5) )+ 32

c = 45
f = farh(c)
print("Fahreheit temperature is " +str(f))

