# string
# literal assignment
first = "Dave"
last ="Gray"
print(type(first))
print(type(first)==str)
print(isinstance(first,str))

print("******************")
# constructor function :(to comment or uncomment all at once ctrl+slash)
# pizza = str("Pipperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))
print("******************")
#concatenation (adding to strings together to form larger string)
fullname = first +' '+ last
print(fullname)

fullname += "!"
print(fullname)

print("&&&&&&&&&&&&&")
# casting number into a string(change type)=> to concatenate with string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I enter prepatory school about" + decade +"s"
print(statement)

# multiple line print :(3 quotation marks either single or doubled)
multiline ='''
 hey, how are you?

 I was just check in.
                       All is Good.
'''
print(multiline)
print("%%%%%%%%%%%")
# Escaping special character usage :
sentence = 'I\'m back at work!\tHey!\n\nwhere\'s at\\located?'
print(sentence)

print("%%%%%%%%%%%")
# string methods(function of the class either dot or not):
print(first.lower())
print(first.upper())
print(first)

print(multiline.title()) # title version
print(multiline.replace("Good","Ok")) # replace version
print(multiline) # original version

print(len(multiline))
multiline += "                                                       "
multiline = "                                "+multiline
print(len(multiline))

# to remove this unuseful white space => strip method
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# build a menu:(make method directly with value)
title="menu".upper()
print(title.center(20,"=")) # make what is print in center of 20 ==
print("coffee".ljust(20,".")+ "$1".rjust(4))
print("maffin".ljust(20,".")+ "$3".rjust(4))
print("cheesecake".ljust(20,".")+ "$4".rjust(4))

print("@@@@@@@@@@@@@")
# string index value
print(first[0])
print(first.index("a",0,))
print(first[-1])
print(first[1:-1])
print(first.find("v",1,))
print(first[1:])

print(".................")
# boolean method with string
print(first.startswith("D"))
print(first.endswith("z"))

print("!!!!!!!!!!!!!!!!!!!!")
# boolean data type
myvalue = True
x = bool(False) # constructor function
print(type(x))
print(isinstance(x,bool))

# numeric data type :
# int
price = 100
best_price = int(80)
print(type(price))
print(isinstance(price,int))

# float 
gpa = 100.421
y = float(80)
print(type(y))
print(isinstance(y,int))

# complex_value
comp_value = 5 + 3j
print(type(comp_value))
print(isinstance(comp_value,complex))
print(comp_value.real) # give me the real part
print(comp_value.imag)
print("-------------")

# built-in function for the number
print(abs(gpa))
print(abs(gpa*-1))
print(round(gpa))
print(round(gpa,1)) # nearst decimal place

print("++++++++++++")
# import module as an object to use its function
import math
print(math.pi) #math. and choose what do you want
print(math.sqrt(gpa)) # make function on the variable
print(math.sqrt(100))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string into number
zipcod = "10001"
zip_value = int(zipcod)
print(type(zip_value))