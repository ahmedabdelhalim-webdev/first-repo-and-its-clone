# collection : single variable used to store multiple variable
# collection : list(ordered,changable data,duplicate,indexing by value)
# tuple(unchangable)
# set(unordered,immeutable,add,remove,no duplicate)
# tuple faster than list
# set used to unique value
empty_list=[]
samedatatypelist=["he","is","a","boy"]
diffdatatypelist=["he",5,7.2,True,100]

# to modify item in the list => use enumerate method:
numbers = [10, 20, 30]
for index, number in enumerate(numbers):
    numbers[index] = number * 2
print(numbers)

print("boy" in samedatatypelist) #(boolean of the list)
print("is" in empty_list)
print("!!!")
#position of the specific value
print(samedatatypelist[-1])

# what is the position of this element(index)
print(diffdatatypelist.index(100))
print("&"*40)
# range of value 
print(samedatatypelist[0:2]) # count from 2 to 0 , take number right to 0 till 2
print(samedatatypelist[-3:-1]) # count from right to left in that index
print(samedatatypelist[-1:1]) # count from 1 till -1 and take number from -1 to its right 
print(samedatatypelist[1:-1]) # count from -1 till reach 1 , take number from one till -1

# len = length of item
print(len(samedatatypelist))

# append the list(add one item only)=> add at the end
diffdatatypelist.append("named")
print(diffdatatypelist)

# add item at certain position .insert(position,"what added")
samedatatypelist.insert(0,"begin")
print(samedatatypelist)

# add items at certain position using range[sameindex:sameindex]=>as beginning
samedatatypelist[2:2] = ["alex","bob"]
print(samedatatypelist)

# add list to list
#1- using += ["list item one or more"]
diffdatatypelist += ["khaled","sword"]
diffdatatypelist +=["hi"]
diffdatatypelist += "thi" #this 3 items list
print(diffdatatypelist)

#2- using extend to add new or pr existent list
diffdatatypelist.extend(["program","success"])
print(diffdatatypelist)
diffdatatypelist.extend(samedatatypelist)
print(diffdatatypelist)

# replace value by =>using [index : diffindex]

samedatatypelist[0:2]=["hello,","morad"]
print(samedatatypelist)

# removing item from the list 
# 1- at any position using .remove("name")
samedatatypelist.remove("is")
print(samedatatypelist)

# 2- at the end => .pop("name") => it return a value 
print(samedatatypelist.pop())

# 3- by del dataype[index]
del samedatatypelist[1]
print(samedatatypelist)

# 4- delete whole list and return error if print it
del diffdatatypelist
# print(diffdatatypelist)

# 5- clear list from its item only
samedatatypelist.clear()
print(samedatatypelist)

samedatatypelist=["He","Is","A","Boy"]
# sort the list item
samedatatypelist.sort()
print(samedatatypelist)

# lowercae print after uppercase
samedatatypelist[1:1] = ["hazem"]
samedatatypelist.sort() # make hazem at last position
print(samedatatypelist)

# to correct alpha order despite upper or lower case use => .sort(key=str.lower)
samedatatypelist.sort(key=str.lower)
print(samedatatypelist)

# to reverse index order of item existed list
num = [2,8,42,95,6,3]
num.reverse()
print(num)

# reverse item value of the list
num.sort(reverse=True)
print(num)

num = [2,8,42,95,6,3]
# sorted in screen without change of the original list => use sorted(list,reverse=True)=>has return value
print(sorted(num,reverse=True))
print(num)

print("copy of the list".center(50,"-"))
# make copy of the list by 3 ways:
copy1 = num.copy()
copy2 = list(num)
copy3 = num[:]
num.sort()
print(copy3)# copy not affect the original list
print(num)

print("type , create list".center(40,"*"))
print(type(num))
print(isinstance(num,list))
# to create list=> list([items])
mylist = list(["how","are","you","?"])
print(mylist)
print(".......")
print("Tupule".ljust(7,":")+" non changable list creation".rjust(25))
# tupulename = tuple((items))
mytuple = tuple(("hello",23,3.4,True)) # creation with constructor
anothertuple =("another","tuple")
print(anothertuple)
print(type(anothertuple))

# to change tuple convert it to list
newlist = list(mytuple)
newlist.append("bye")
print(newlist)
newtuple = tuple(newlist)
print(newtuple)

# unpacking of the tuple => assign its value to variables , *variable => rest of variable in list form
ourtuple = (5,2,3,3,4)
(one,*two,three) = ourtuple
print(one)
print(two)
print(three)

# to know method available in tuple and list in vsc=>tuplename.
print(ourtuple.count(3)) # number of occurence
#print(dir(ourtuple)) # one which not surround with 2 underscore is method
# to see description of that method =>help(collectionname)
#print(help(ourtuple))

# modifying nested tuple:
# 1- by converting to list ,unpacking :
'''
    Although tuples are immutable, you can still modify nested tuples by:

Unpacking the tuples into mutable types (like lists).
Making the necessary modifications.
Repacking the tuples back into their original structure.
'''
data = (
    ('apple', (10, 20)),
    ('banana', (30, 40)),
    ('cherry', (50, 60))
)
# Convert the nested tuple to a list for easier manipulation
data_list = list(data)

# Modify the value
for i, (fruit, numbers) in enumerate(data_list):
    if fruit == 'banana':
        numbers = (35, 45)  # New tuple for 'banana'
        data_list[i] = (fruit, numbers)

# Convert the list back to a tuple
data = tuple(data_list)

print(data)

# another solution for more complex situation :
# Define a function to modify the nested tuples
def modify_tuple(tup, target_fruit, new_values):
    # Convert the tuple to a list
    tup_list = list(tup)
    
    # Iterate and modify the target
    for i, (fruit, numbers) in enumerate(tup_list):
        if fruit == target_fruit:
            tup_list[i] = (fruit, new_values)
    
    # Convert back to tuple
    return tuple(tup_list)

# Use the function to modify
data = modify_tuple(data, 'cherry', (55, 65))

print(data)




