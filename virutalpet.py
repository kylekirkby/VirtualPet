import random

class VirtualPet:

    """ A virtual pet which can talk and do other things"""
    
    def __init__ (self,name):
        
        print("Hi i have been born")

        #attributes
        
        self.name = name
        self.hunger = 10
        self.energy = 1
        
    def talk(self, speech):

        print(speech)

    def eat(self, food):

        if food == "apple":
            self.hunger = self.hunger - 2
            self.energy = self.energy + 2
            print("I love apples!")
            
        elif food == "cake":
            self.hunger = self.hunger - 4
            self.energy = self.energy + 4
            print("Cake is awesome!")
            
        elif food == "sandwich":
            self.hunger = self.hunger - 3
            self.energy = self.energy + 3
            print("Nothing like a good sandwich!")
            
        else:
            print("I don't like that food!")

        print("New energy level: {0}".format(self.energy))
        print("New hunger level: {0}".format(self.hunger))
        
def main():
    name = input("Please enter a name for your pet: ")
    pet_one = VirtualPet(name)
    pet_one.talk("Hi i am {0}".format(name))

    while pet_one.hunger > 5:
        sayings = ["I'm still hungry!", "My tummy is rumbling","Give me more food! I need energy!"]
        randomNum = random.randint(0,2)
        pet_one.talk(sayings[randomNum])
        food = input("Enter food name:")
        pet_one.eat(food)

if __name__ == "__main__":

    main()
