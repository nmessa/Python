## Lab Exercise 1/3/2020 Problem 3
## Author: 
## This program will test Goldbach's Conjecture
from math import sqrt

#Test a number for primality
def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

#Generates a list of prime numbers from 2 to num
def makePrimeList(num):
    primeList = []
    for i in range(2, num):
        if isPrime(i):
            primeList.append(i)
    return primeList

#generates a list of 2 numbers from prime list if possible           
def goldbach(num, pl):
    #Add code here
    

#test code
found = False
#Test all even numbers to 10000
#Do not test the number 2
for number in range(4, 1000, 2):
    #Create a prime list for the number you are testing
    pl = makePrimeList(number)

    #pass the number you are testing and the prime list to
    #goldbach funtion
    temp = goldbach(number, pl)

    #if you get back an empty list, you found a number that
    #disproves Goldbach's Conjecture
    if len(temp)==  0:
        foundNumber = number
        found = True
        break;

if not found:
    print("You have verified Goldbach's Conjecture for numbers to 1000")
else:
    print("You have disproven Goldbach's Conjecture for", foundNumber)


        
