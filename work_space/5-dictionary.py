# dictionary and list(mutable,dynamic(grow,shrink as needed,can be nested))
# dictionary and list differ in (accessing by key or indexing)=> no dupplication of the key or index
# dictionay key => immeutable as(tuple,int,float,string,boolean),(dictionary and list=>is mutable)
# if key or value from indexing type(numbers) you can use numeric indexing for it
# dictionary : collection data consist of key and value
print("create dictionary".center(50,"."))
# dict(key="value")
school = dict(studentname="mora",schooltype="primary") # by constructor
# tuple in the list=>dict([("key","value")])
hospital = dict([
    ("noha","hassan"),("ahsan","sdhf")
])
# comma separated between key-value pair in {}=>{"key":"value","key":"value"}
library = {
    "philosophy" : "ibn-khaldon",
   "science" : "medecine",
    "literary" : "ba-kather"
}
whereismypen={
    1:"in room",
    2: "on windows",
    3 : "fly a way"
}
print(school);print(type(school));print(len(school))
print(hospital);print(type(hospital));print(len(hospital))
print(library);print(type(library));print(len(library))
print(whereismypen[1])

print("access".ljust(7,":")+ " index of the dictionary".rjust(20))
# 1- by the key => 2 methods
print(school["studentname"])
print(library.get("philosophy"))
# list of all keys
print(hospital.keys()) # doctors
# list all values (todays patients)
print(hospital.values())
# list key , value pair as a list of tuple
print(hospital.items())

# verify a key exist in dictionary
print("science" in library)
print("madbouly" in hospital)

print("change or add value of dict".center(60,"="))
# by assign dict["key"]= "newvalue"
hospital["ahsan"] = "faoul"
print(hospital)
# by dictname.update({"key":"value"}), this method also add key-value pair
library.update({"literary":"elrafi"})
library.update({"history":"victoryday"}) # add key-value pair
print(library)

# remove an item :
#1- dictname.pop("key")
print(library.pop("philosophy")) # return value
print(library)

# 2- assign key to new value:
library["literary"] = "anatomy of body"
print(library)

# 3- remove last item
print(library.popitem())
print(library)

# delete and clear items
teacher_ham = {
    "hassa":{
      "degree":"excellent",
      "attendance":"present"
    },
      "han":{
      "degree":"fair",
      "attendance":"abscent"
    },
      "halo":{
      "degree":"mod",
      "attendance":"getout"
    }
}
del teacher_ham["halo"]
print(teacher_ham)
print(teacher_ham["han"]["degree"])
# clear all item in dictionary
hospital.clear()
print(hospital)
del (hospital)

print("diff bet same reference and create a copy and how".center(70,"."))
library1 = library # this the same reference (any change one will appear in other)
print(library)
library.update({"geography":"italy"})
print(library1)

# copy : change in one of them not appear in another one
school2 = school.copy()
school.update({"gan":"goha"})
school2["nano"]= "talo"  
print(school2)
print(school)

# copy using constructor :
school3 = dict(school)
print(f"this is : {school3}")

# another method to write nested dictionary :
member1 = {
    "name":"halo",
    "study":"engineer"
}
member2 = {
    "name":"galo",
    "study":"science"
}
group = {
    "member1":member1,
    "member2": member2
}
print(group)
print(group["member2"]["name"])

# to create dict from list =>use enumerate method :
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")


print("end of dictionary".center(50,"."))
print("set".ljust(4,":") + " unique item for group data")
# creation of the set
# 1- direct by {}
num1 = {1,2,3,4,5}
num2 = set((1,2,2,2,5))
num3 = {1,True,False,2,3,4,0}
print(num1);print(num2);print(num3);print(type(num1))
# set is unique value (no duplicate), True is duplicate of one,False is duplicate of zero
# check value in a set
print(2 in num2)

# add a new value to the set
num2.add(10);print(num2)

# add element of set to another,update work with list,tuple,dictionary also
num1.update(num3)
num3.update([50,60])
num2.update({"hallo":"ballo"})
print(num1);print(num3);print(num2)

# merge 2 sets and create new one=> oneset.union(another)
set1 = {"a","b","c"}
set2 = {"d","3","e"}
newset = set1.union(set2)
print(newset)
# show intersection(duplicate)of 2 sets
set1 = {"a","b","c"}
set2 = {"d","b","e"}
set3 = set1.intersection(set2)
print(set3)
print("this is ",set1)
# show unique value of that set(exclude the duplicate)=> symetric difference update
#set4 = set1.symmetric_difference_update(set2) => false as it has no return value
set1.symmetric_difference_update(set2)
print(set1)