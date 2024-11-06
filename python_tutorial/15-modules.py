# module is a file containning fuction and variable => to use it => import(import math) it 
# or part from it=> from math import pi
#import math
#print(math.pi) # access the module
from math import pi
print(pi)

# using alias with the imported module:
import random as rdm

# to know all modules =>print(help("modules")) , to know what the use of its part=> print(help("modulesname"))
# to know what inside the module(after importing it)
# 1- module or its alias +. (all function,attribute)
# 2- print(dir(modulename)) or for item in dir(modulename): print(item)
# 3- python module index => all details of the module

print(__name__) # it is the main function, in which all function run in this page

# imported function also has its main function(not work here,work locally only) => modulename.__name__
print(rdm.__name__) # random => name of module (this module by its content except its main function)

# make function run locally only(prevent it imported by another page)
if __name__==__main__: 
    randomfunfact() 
