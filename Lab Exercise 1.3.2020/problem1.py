## Lab Exercise 1/3/2020 Problem 1
## Author: 
## This program will calculate your weight on other planets.

#Create a dictionary of planet names (string) to gravitational
#conversion (float). Name the dictionary planets
#Add code here


#Create a dictionary of menu number (int) to planet name (string)
#Name your dictionary menuToPlanet
#Add code here


#This function displays a menu and returns menu choice number
def displayMenu():
    #Add code here
    
    choice = int(input("Choose a planet: "))
    return choice

#This function returns the weight on the chosen planet
def findWeight(weight, planet):
    #Add code here
    

#Code to test functions
choice = displayMenu()
myWeight = float(input("How much do you weigh? "))
planetWeight = findWeight(myWeight, menuToPlanet[choice])
print ("You weigh", planetWeight, 'pounds on', menuToPlanet[choice])
    
