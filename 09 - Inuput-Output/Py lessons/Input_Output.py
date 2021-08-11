# Chapter 9 – File I/O

# The random access memory is volatile, and all its contents are lost once a program terminates.

# In order to persist the data forever, we use files.

''' A file is data stored in a storage device. A python program can talk to the file by reading content
 from it and writing content to it. '''

# Types of Files

# There are 2 types of files:
 
# 1. Text files (.txt, .c, etc)    #Use Easily Open and Read
# 2. Binary files (.jpg, .dat, etc)    


# Python has a lot of functions for reading, updating, and deleting files.

# Opening a file

# Python has an open() function for opening files. It takes 2 parameters:  @@@  filename and *** mode.

# open(“this.txt”, “r”)
# Here, “this” is the file name and “r” is the mode of opening (read mode)

# Reading a file in Python

# Exp: 

f = open('sample.txt', 'r')
data = f.read()
print(data)

