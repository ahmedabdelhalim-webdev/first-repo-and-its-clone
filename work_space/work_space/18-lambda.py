# def squared(num) : return num * num
# squared = lambda num :num *num
# print(squared(2))

# change variable into function
squared = lambda num :num *num
print(squared(3))

# def add(num) : return num+2
add = lambda num :num +2
print(add(8))

# def multiply(x,y): return x*y
multiply = lambda x,y : x*y
print(multiply(6,7))

print("lambda use in another function".center(60,".").title())

def funcbuilder(x):
    return lambda num : num +x

addnum = funcbuilder(10) # change variable into function(as closure), pass argument of x
print(addnum(5)) # pass argument of num 
print(addnum(50))

print("higher order function".center(60,".").title())
# take one or more function as argument or return function as a result (either its input or output is a function)
# 1- variable = map(function,data_collection_variable)
numbers = [2,4,5,6,3,6,8,8,9]
# map use function as iterator 
squared_num = map(lambda num : num*num , numbers) 
print(squared_num) # map object address
print(list(squared_num)) # list of squared num
print("filter".title().ljust(7,":"),"use other function as lambda".rjust(20,"."))

lambda num : num %2 != 0
#syntax = variable= filter(function,collection_variable)
odd_nums = filter(lambda num : num %2 != 0,numbers)
print(odd_nums)# filter object address
print(list(odd_nums))

# from functools import reduce
from functools import reduce

# syntax => variable=reduce(function,data_collection_variable)=>reduce all number to first one in accumulation manner
# to add with reduce(function,variable,new_added_value) = sum(variable,new_dded_value)
total = reduce(lambda acc , curr : acc + curr,numbers)
print(total)
print("*"*40)
names = ["david milan","linux torvaldes","vangschmidertvanbukh"]
character_count = reduce(lambda acc,curr : acc + len(curr),names,0) # 0 means handle it as a number not a string
print(character_count)