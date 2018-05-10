#!/usr/bin/python

print('All things python')
print('Change')

#Single comment

'''Multiple Line 
Comment'''

'''
Five Data Types

1. Numbers
2. Strings
3. Lists
4. Tuples
5. Dictionaries

Seven Arithmetic Operations

1. +
2. -
3. *
4. /
5. % Modulus
6. ** Exponential Multiplication 
7. // Divides and removes remainder 

'''

name= "Invisible"
print(name)

print("5*2=", 5*2)

single_line_string = "You can do whatever you aim for"
multiple_line_string = ''' I dont like when people are selfish and do not care
for others feelings'''

# Play around with different ways of printing strings
print('I want to say that', single_line_string, multiple_line_string)

# concatenating the strings together
print(single_line_string + multiple_line_string)
print(" %s %s %s " % ("I want to say that", single_line_string, multiple_line_string))

#Lists

New_list = ['Apples', 'Orange', 'Bananas']
print(New_list)

'''
There are a bunch of functions you can apply on lists, use index to represent a particular item in the list; replace, delete, remove, sort, append items; print
min and max of the list; add two lists to combine them into one; make a list of lists, strings, numbers, etc
'''

#Tuples

New_Tuple = (1,45, 23, 7, 9)
print(New_Tuple)

'''
Similarly, you use index to represent an item, min, max BUT the main difference between a list and tuple is you cannot change
a tuple. You can convert it into a list to make changes and then convert back to a tuple
'''

#Dictionaries

New_dictionary= {'Actor': 'Michael',
		'Director': 'David',
		'Actress': 'Lisa'}

print(New_dictionary)

'''
Dictionaries have values - each of them with their unique key (Actor, Director, Actress are keys). Dictionaries are very similar to lists except that 
you cannot add two dictionaries - thats the main difference
'''
