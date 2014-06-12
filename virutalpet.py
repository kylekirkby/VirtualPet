import random,time

class VirtualPet:

    """ A virtual pet which can talk and do other things"""
    
    def __init__ (self,name):
        
    
        #attributes
        
        self.name = name
        self.hunger = 10
        self.thirst = 5
        self.energy = 3
        self.sleep = 6
        self.foodItems = {'apple':2,'cake':4,'sandwich':3}
        
        
    def talk(self):

        ##hint towards how the pet is feeling

        if hunger == 10:
            print("I am really hungry! I need to eat before I can do anything else!")
    def eat(self, food):

        ##allows the virtual pet to eat some food

        

        if food in self.foodItems.keys():
            
            value = self.foodItems.get(food)
            self.hunger = self.hunger - value
            self.energy = self.energy + value
            print("New energy level: {0}".format(self.energy))
            print("New hunger level: {0}".format(self.hunger))
            
        else:
            print("I don't like that food")

    def walk(self):
        ## take the virtual pet for a walk

        if self.hunger < 6:
        
            if self.energy < 5:
                print("I don't have enough energy to walk :(")
            else:
                print("Yay, I needed a walk I had so much energy!")
                self.energy -= 2
                self.sleep -= 1
                self.hunger += 1
        else:
            print("I am really hungry! I need to eat to get my energy up before I can go on a walk!")
                

    def petSleep(self):
        ## Let your pet sleep
        if self.sleep > 5:
            print("I don't need anymore sleep :) ")
        else:
            print("Great! I need to sleep. I am so tired!")
            self.sleep += 2
            self.energy += 2
            time.sleep(2)
            
            print("That was a good sleep! I needed that!")
    def drink(self):
        print("I needed a drink")



    def playGame(self):
        print("I was bored! But thanks for paying attention to me!")



    def showStats(self):
        print()
        print("Hunger Level: {0}".format(self.hunger))
        print("Thirst Level: {0}".format(self.thirst))
        print("Energy Level: {0}".format(self.energy))
        print("Sleep Level: {0}".format(self.sleep))
        print()
def mainMenu(name):
    print()
    print("VirtualPet Beta")
    print()
    print("1. Give {0} food".format(name))
    print("2. Give {0} a drink".format(name))
    print("3. Take {0} for a walk".format(name))
    print("4. Play a game with {0}".format(name))
    print("5. Let {0} sleep".format(name))
    print("6. View Stats")
    print("9. Exit")
    print()
        
def main():
    nameAccepted = False
    while nameAccepted != True:
        name = input("Please enter a name for your pet: ")
        if name != "":
            nameAccepted = True
        else:
            print("Your pet must be given a name!")
    pet_one = VirtualPet(name)
    
    option = 0
    while option != 9:
        mainMenu(pet_one.name)
        try:
            option = int(input("Please choose: "))

        except ValueError:
            print("Please enter a number!")
        if option == 1:
            ## Feed Pet
            print("Your food supply:")
            for key in pet_one.foodItems.keys():
                print(key, end=" | ")
            print()
            food = input("Enter food name:")
            print()
            pet_one.eat(food)
            print()
        elif option == 2:
            pet_one.drink()
        elif option == 3:
            pet_one.walk()
        elif option == 4:
            pet_one.playGame()
        elif option == 5:
            pet_one.petSleep()
        elif option == 6:
            pet_one.showStats()
if __name__ == "__main__":

    main()
