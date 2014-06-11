class VirtualPet:

    """ A virtual pet which can talk and do other things"""
    
    def __init__ (self,name):
        
        print("Hi i have been born")

        #attributes
        
        self.name = name
        
    def talk(self):

        print("Hello, I am {0}.".format(self.name))

    def eat(self, food):

        if food == "apple":
            print("I love apples!")
        elif food == "cake":
            print("Cake is awesome!")
        elif food == "sandwich":
            print("Nothing like a good sandwich!")
        else:
            print("I don't like that food!")
        
def main():
    name = input("PLease enter a name for your pet: ")
    pet_one = VirtualPet(name)
    pet_one.talk()
    food = input("I'm hungry. What can you give me?: ")
    pet_one.eat(food)

if __name__ == "__main__":

    main()
