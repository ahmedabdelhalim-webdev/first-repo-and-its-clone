class Vehicle:
    def __init__(self,make,model) : # init => to make parameter of the class itself(make class parameter)
        self.make = make  # make as a prop or members of class
        self.model = model
        pass
    def move(self): # self means can be access by class or its instance
        print("move along ...")

    def get_make_model(self):
        print(f"I have a {self.make} {self.model} .") # 




my_car = Vehicle("Tesla","model 3")# pass value of method(construct object or instance of class with its properities)
# print(my_car.make) # to print argument in class(before making get_make_model function,which make this role)
# print(my_car.model)
my_car.get_make_model()
my_car.move()

your_car = Vehicle("Nissan","Model 50")
your_car.get_make_model()
your_car.move()

print("inheritance : class inherite from other class".title().center(60,"."))

# class Airplane(Vehicle): # inherite what in the vehicle class
#     def move(self): # overwrite this function in vehicle class
#         print("flie along ...") 

class Airplane(Vehicle): # to customize paramete for airplane(some inherite and other unique for Airplane)
    def __init__(self, make, model,faa_id):# initialize class(make , assigne parameter to it)
        super().__init__(make, model) # inherite from class
        self.faa_id = faa_id  # add these unherited parameter

class Truck(Vehicle):
    def move(self):
        print("Rumbles along..")

class GolfCart(Vehicle):
    pass # inherite everything from vehicle class

cessna = Airplane("cessna","skyhawk","N-123434")
mack = Truck("Mack","pinnacle")
golfwagon =GolfCart("yamaha","gcsc")
cessna.get_make_model()
cessna.move()
mack.get_make_model()
mack.move()
golfwagon.get_make_model()
golfwagon.move()

print("\n\npolymorphism".upper().center(40,"."))
# polymorphism : ability to behave differently with the same input messages
# make loop for each object
for v in (my_car,your_car,cessna,mack,golfwagon):
    v.get_make_model()
    v.move()
