# exception handling => show me the error and run progrm with this error(test running the rest of program)
# python built-in exceptions => page contain all exception python had
# print(x) # one of the built-in exception of python 

print("How to built your own exceptions in python".title().center(80,"*"))
# built in exception with customize message for me
# try:
#     print(y)
# except NameError: 
    # print("There is an error,seem to be undefined ")

x = 2
try:
    # print(x/0) # devision by zero error can't be catch by name error
    print(x/1)
except NameError: 
    print("There is an error,seem to be undefined ")
except ZeroDivisionError:
    print("please don't divide by zero")
else: # if no error occure
    print("No errors!")
finally: # print in all cases(presence or absence of error )
    print("print with or without error")


# create an error 
print("."*50)

x = 2
try:
    if not type(x)is str:
        # raise TypeError("only strings are allowed .")
        raise TypeError()
except NameError: 
    print("There is an error,seem to be undefined ")
except ZeroDivisionError:
    print("please don't divide by zero")
except Exception as error: # Exception is if condition before
    print(error)
else: # if no error occure
    print("No errors!")
finally: # print in all cases(presence or absence of error )
    print("print with or without error")

print("custom exception by raise and exception or name of class".title().center(100,"."))

x = 2
try:
    raise Exception("I'm a custom exception!")
except NameError: 
    print("There is an error,seem to be undefined ")
except ZeroDivisionError:
    print("please don't divide by zero")
except Exception as error: # Exception is if condition before
    print(error)
else: # if no error occure
    print("No errors!")
finally: # print in all cases(presence or absence of error )
    print("print with or without error")

print("*"*50)
class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("this is not just cool!")
except NameError: 
    print("There is an error,seem to be undefined ")
except ZeroDivisionError:
    print("please don't divide by zero")
except Exception as error: # Exception is if condition before
    print(error)
else: # if no error occure
    print("No errors!")
finally: # print in all cases(presence or absence of error )
    print("print with or without error")


