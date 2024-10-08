person = "DAvid"
coins = 3
# 1- use concatenation => take care to make all data in string 
print("\n" + person +" has"+ str(coins) +"coins left!")

# 2- as c language by place holder %s 
print("\n%s has %s coins left" %(person,coins))

# 3- .format(variable or "value")
print("\n{} has {} coins left".format(person,coins))

# {indexing what appear first}
print("\n{1} has {0} coins left".format(person,coins))

# "{ variable}".format(variable = value)
print("\n{person} has {coins} coins left".format(person=person,coins = coins))

# { key}".format(**dictionaryname)
player={"person":"david","coins":3}
message ="\n{person} has {coins} coins left".format(**player)
print(message)

print("f-string is the most used one".title().center(60,"."))
# f"{variable}"
message= f"\n{person} has {coins} coins left."
print(message)
# pass value to it
message= f"\n{person} has {2*5} coins left."
print(message)

# use method in it
message= f"\n{person.lower()} has {coins} coins left."
print(message)

#  for dictionary :
message= f"\n{player['person']} has {coins} coins left." #double quote surround message and single around key or vice versa 
print(message)

# pass formating option
print("."*50)
num = 10
print(f"\n2.25 times {num} is {2.25*num:.2f}\n")

# using for loop
for num in range(1,11):
    print(f"2.25 times {num} is {2.25*num:.2f}")
print("^"*20)
for num in range(1,11):
    print(f"{num} divided by 4.52 is {num/4.52:.2%}") # you can use either f (fixed)or % (placeholder)beside decimal point