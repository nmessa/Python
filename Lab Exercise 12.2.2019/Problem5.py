## Lab Exercise 12/2/2019 Problem 5
## Author: 
## This program generates Pascal's Triangle
#Create a list that will hold a other lists to become a list of lists
pascal = []

def blank_list_gen(x):
    #create a list of empty lists of all zeros
    while len(pascal) < x:
        pascal.append([0])

def pascals_triangle_generator(rows):

    #Adjust rows so range function works
    rows -= 1
    
    blank_list_gen(rows)

    #create lists each containing [0]
    #Add code here
    

    #Put a 1 the beginning and end of each row
    #Add code here
    
        
    #Add first two rows of triangle
    #[1]
    #[1, 1]
    #Add code here
    

    #Add the rest of the rows
    #Add code here
    

pascals_triangle_generator(10)

#Print the triangle
for row in pascal:
    print(row)

## Output
## [1]
## [1, 1]
## [1, 2, 1]
## [1, 3, 3, 1]
## [1, 4, 6, 4, 1]
## [1, 5, 10, 10, 5, 1]
## [1, 6, 15, 20, 15, 6, 1]
## [1, 7, 21, 35, 35, 21, 7, 1]
## [1, 8, 28, 56, 70, 56, 28, 8, 1]
## [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
## [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    
