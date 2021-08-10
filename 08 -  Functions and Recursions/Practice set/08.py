'''Problem 8. Write a python function to remove a given word from a list and strip it at the same time.'''
# What is strip  ? - 
# this = "Vasudev Jaiswal    is good boy "
# print(this)
# print(this.strip)    # remove the strip 

    
def remove_and_split(string,word):
    newsStr = string.replace(word," ")




this = "   Vasudev Jaiswal is good boy"
n = remove_and_split(this,"Vasudev")
print(n)