# With statement

# The best way to open and close the file automatically is the “with” statement.

# with open(“this.txt”) as f:

#             f.read()
# #There is no need to write f.close() as it is done automatically

with open('that.txt','r') as f:
    a = f.read()
with open('that.txt','w') as f:
    a = f.write()
print(a)