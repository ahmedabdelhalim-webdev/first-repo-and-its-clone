# recursion : function call its self(iterate itself)
def add_one(num):
    if num >= 9: # you should under number 9 to recursion work
        return num+1
    total = num + 1
    print(total)
    return add_one(total) # update 
add_one(0) # no number 10 as no print in if statement => use it as function without return it till 9
print("...")
# use it as function with return (either stored in variable or print directly)=> each reach its accurate value 10
print(add_one(2)) # number 10 present as function terminate its recursion
