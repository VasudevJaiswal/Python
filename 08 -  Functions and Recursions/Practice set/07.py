'''Problem 7. Write a python function that converts inches to cms.'''

def cms(inches):
    return(inches*(2.54))    #multiply the length value by 2.54

len = cms(int(input("Enter the length of the Inches : ")))
print("Inches covert in CMS Successful The result is  :" +str(len))