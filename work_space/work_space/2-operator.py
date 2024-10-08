# statement => operation of the value
# operator => symbol perform operation on value and variable hold this value(operand)
# operator=> =
# arthimatic operator(+ - * / % **)
meaning = 5

meaning +=6
meaning -=3
print(meaning)
meaning *=5
print(meaning)
meaning /=4
print(meaning) # default float
print(round(meaning)) # default int
meaning %3
print(meaning)# default float

# boolean operator(==,>,<,>=,<=,!=)=> is that statement true or false
print(54==54)
print(54 != 54)
print(1>2);print(2>1)

print("   **   ")
# use it with notation
x = True
y= False
z = True
print(not x)
print(not y)
print(x and y)# pass the first one and give the value of the second
print(y and x) # stop at the first one and reveal its value
print(x or y)
print(y or x)
a = "if statement examples "
print(a.center(20,"."))
meaning = int(input("enter the value : "))

if meaning == 10:
  print("Right On!")
else:
  print("not correct!")

print(a.center(20,"$"))
value = int(input("enter the value : "))

if value > 100:
  print("Right On!")
else:
  print("not correct!")

# ternary operator :if statement in one raw
# output if True else other-output
num = int(input("enter the value : "))
print("that is correct") if num ==100 else print("that is not correct")
