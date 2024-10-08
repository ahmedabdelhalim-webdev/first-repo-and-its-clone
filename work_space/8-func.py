# placeholder to receive data for the function called parameter(never change)=> reusablity of function
def sum(num1,num2): # placeholder(programmer intial symbol or data)
    print(num1+num2)

sum(2,3)# pass actual data(argument)=> change (as user need)
sum(100,25)
sum(54,69)

print("function return value to make action(stored in variable ,print..)".center(60,","))
# more abstraction=> store in variable
def sum(num1,num2): # placeholder
    if (type(num1) is not int or type(num2) is not int):
        return #don't return anything
    return num1+num2

#total = sum("54",40) # return =>none (if passed non int)
total = sum(54,40)
print(total)

# default value of the parameter(initial value)=> in case no argument(user data)passed
def sum(num1,num2 =2): # placeholder
    if (type(num1) is not int or type(num2) is not int):
        #return 0 possible to tell that is not int 
        return 
    
    return num1+num2
total = sum(5) # able to write one argument as there default(initial parameter value)for other variable
print(total)

# make placeholder(parameter)=> allow user to enter multiple arguments(args)=> def name(*args)
# output is tuple
def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items("goda","nany","tall") # type is tuple
multiple_items(1,2,3) # type is tuple

# you can make output as dictionary => def name(**kwargs): =>keywordargs (indexing by keyword)
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

# name(key="value",key="value")
multi_named_items(first="goda",last="malo")

print("scope of the variable".title().center(50,"."))
# global variable => act in all function 
# local variable only act in thier function
# argument(user entry)has priority in the function action than global variable
name = "saad"
def greeting(firstname):
    color = "blue"
    print(color)
    print(name)
    print(firstname)

greeting("alaa")
print("priority of argument over global var in fun")
# even if global name has the same name of parameter , still argument has priority
name = "saad"
def greeting2(name):
    color = "blue"
    print(color)
    
    print(name)

greeting2("alaa")
# global scope function =>can be execute in any function
def another():
    print("global function as greeting")
    greeting("sla") # call global function in another function

another()
# define function in another function :
print("nested function")
def another2():
    def greeting2(name): #define local scope function
        color = "blue"
        print(color)
        
        print(name)
    greeting("kdf") # global function

another2()
# global variable can access function but you can't modify in function before tell it 
# global variablename += value
count = 1
def addto():
    #count +=1  #cant modified as access only as parameter(placeholer or initial value)
    global count # define as it is the same global variable
    count +=1 # now you can
    print(count)
addto()
print("####")

# the same concept present in nested function:
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x # same idea of global var but in nested function
    x = "hello"
  myfunc2() # call it inside mother function to appear outside
  return x

print(myfunc1())

print("lambda function(function maker in one line,not use anywhere else)".title().center(70,"."))
# lambda arguments: expression
# A lambda function that adds 10 to its argument
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Lambdas are often used with functions like map(), filter(), and sorted()
# Using lambda with map to square numbers
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

# Using lambda with filter to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Sorting a list of tuples based on the second element
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

print("filter=> apply function of iterable(list,tuple)".title().center(70,"."))
# syntax : filter(function, iterable)
# filtering even number
# 1- Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]


#2- Using filter to apply the is_even function
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list and print it
print(list(even_numbers))  # Output: [2, 4, 6]

# using lambda with filter :
# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Using filter with a lambda function to get even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list and print it
print(list(even_numbers))  # Output: [2, 4, 6]


# 3- filtering string :
# Function to check if a string has more than 3 characters
def long_words(word):
    return len(word) > 3

# List of words
words = ['cat', 'elephant', 'dog', 'hippopotamus']

# Using filter to apply the long_words function
long_words_list = filter(long_words, words)

# Convert the filter object to a list and print it
print(list(long_words_list))  # Output: ['elephant', 'hippopotamus']

""" important notes :
The filter() function returns an iterator, so you need to convert it to 
a list (or another collection type) if you want to see the results.

If you pass None as the function, filter() will remove all items 
from the iterable that are False (e.g., 0, None, '', False, etc.).

"""
# Removing falsy values from a list
items = [0, 1, '', 'hello', False, True, None]
truthy_items = filter(None, items)
print(list(truthy_items))  # Output: [1, 'hello', True]







