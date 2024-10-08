# while loop and for loop
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value +=1
print("continue function with if".center(50,"."))
counter = 1 
while counter <= 10 :
    counter += 1  # as when it reach 5 not updating the loop (infinite looping)
    if counter == 5 :
        continue  # not make any other step in loop and go new updated number and its condition
    print(counter)
else :
    print("value now is equal to " + str(counter))

print("....................")
value = True
while value:
    print("hello the value is : ",value)
    value = False # the same is 0

# anything rather than 0 mean true
value = "y"
while value :
    print(value) # the value here is y (consider as true)
    value =0
print("continue function make evaluation of output again".center(100,"."))
value = "y"
count = 0
while value :
    count += 1
    print(count)
    if count ==5:
        break
    else : 
        value = 0 # reassign value to zero
        continue # pass the next action if there => go to reevaluate condition (stop looping as condition changed)
print("....................")

print("for loop : used for sequence".title())
names = ["hosa","kota","tota","khota"]
for name in names :
    if name == "tota":
        break
    print(name)

teachers =["science","geography","math"]
for teacher in teachers:
    if teacher == "geography":
        continue
    print(teacher)
print("range".ljust(6,":") + "function for for loop".rjust(40))
for x in range(0,16,2):
    print(x)
else :
    print("Glad that\'s over")

print("nested loops".title().center(50,"."))
subjects =["science","geography","math"]
students =["morad","gad","tamer"]
for subject in subjects :# what happen for the inside
    for student in students:
        print(f"{subject} studied by" + ":" + student)

print("explain comprehensions in python".center(60,"."))

# comprehension : sequence creator in one line(sequence : list,set,dict,generator expressions)
#syntax => [expression for item in iterable if condition]
"""
    expression(operations happens to item=output): The value to include in the new list.
item: The current item from the iterable=> counter
iterable: The sequence or collection to loop through=> as input inside range function
condition (optional): A condition to filter items.
"""
#  create list => [0:10]
squares = [x**2 for x in range(10)]
print(squares)

# create list of even square from 0 to 9
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# create set(unordered , no duplicate)
# syntax => {expression for item in iterable if condition}
# create set of a unique length of words from a list
words = ['apple', 'banana', 'cherry', 'date']
word_lengths = {len(word) for word in words}
print(word_lengths)

# create a dictionary in concise way
# syntax => {key_expression: value_expression for item in iterable if condition}
# create dictionary from the list where value is the square of the item
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

# expression generator (for large data set,more efficient than list)
# syntax => (expression for item in iterable if condition)
# create generator for even square :
even_squares_gen = (x**2 for x in range(10) if x % 2 == 0)

for square in even_squares_gen:
    print(square)

# zip => (packing iterables or collector)combines collection(list,tuple) fo data together,create dictionary
# zip(iterable1, iterable2, ..., iterableN)
# 1- combinning 2 lists :
# names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

combined = list(zip(names, ages))
print(combined) #[('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# 2-unzipping:To unzip a list of tuples, you can use the * operator to unpack the zipped object
combined = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

names, ages = zip(*combined)
print(names)
print(ages)
'''
output :
('Alice', 'Bob', 'Charlie')
(25, 30, 35)
'''

# 3. Zipping with Different Lengths(stop at shorter length iterable)
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]

combined = list(zip(names, ages))
print(combined) # [('Alice', 25), ('Bob', 30)]

# 4. Using zip in a Loop : to iterate over multiple sequences in parallel
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
"""
output :
Alice: 85
Bob: 90
Charlie: 88
""" 
# 5- create dictionary : 
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

dictionary = dict(zip(keys, values))
print(dictionary) # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# transpose matrix : convert to list of list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print(transposed) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print("mapping function in python".center(50,"."))
# maping : make function to each iterable items(list,tuple)=>used to change data 
# syntax : map(function, iterable, ...)
# 1- applying function to each item :
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the result to a list to see the output
print(list(squared_numbers)) #[1, 4, 9, 16, 25]

# 2- with lambda(function maker):
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

print(list(squared_numbers))


# 3- mapping multiple iterable:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

added_lists = map(lambda x, y: x + y, list1, list2)

print(list(added_lists)) # [5, 7, 9]

# 4- converting data type within other data type
string_numbers = ['1', '2', '3', '4', '5']
integer_numbers = map(int, string_numbers)

print(list(integer_numbers)) # [1, 2, 3, 4, 5]









