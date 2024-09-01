#Travis Wilson
#Module 2 Homework
#TWilsonGradeChecker.py
#Accepts inputs for a students name and GPA, then checks their grade to see if they've made the 
#dean's list or honor roll.  Also validates input.

#Define constants DEANSLIST and HONORROLL
DEANSLIST = 3.5
HONORROLL = 3.25

#Import re module
import re

#defile list of invalid characters (everything but what is listed)
invalid = r"[^a-zA-Z\s\-\.\']"

#Master loop so the program keeps running
while True:
    lastName = str(input("Please enter the last name or ZZZ to quit: "))

    # input validation
    while True:
        if re.search(invalid,lastName) == None:
#the results of the re.search function will be None if there are no invalid characters
#and the loop will be broken.
            break
        else:
            lastName = str(input("You entered an invalid character, please try again: "))

    #quit on exit string
    if lastName == "ZZZ":
        print("You have chosen to end the program.")
        quit()
     
    #repeating the same process as I did with the lastName    
    firstName = str(input("Please enter the first name: "))
    while True:
        if re.search(invalid,firstName) == None:
            break
        else:
            firstName = str(input("You entered an invalid character, please try again: "))

    #GPA input
    gradePointAverage = input(f"Please enter the GPA for {firstName} {lastName}: ")

    #Testing that the GPA is a number, and between 0 and 4
    while True:
        try: 
            gradePointAverage = float(gradePointAverage) 
            if gradePointAverage > 4 or gradePointAverage < 0:
                print(f"\n{gradePointAverage} is outside of the range of 0.0 to 4.0")
                gradePointAverage = input(f"Please enter a numerical value for the GPA of {firstName} {lastName}: ")
            else:
                break
        except ValueError:
            gradePointAverage = input(f"Please enter a numerical value for the GPA of {firstName} {lastName}: ")
            
    #Checking the GPA against the constants
    if gradePointAverage >= DEANSLIST:
        print(f"{firstName} {lastName} has a GPA of {gradePointAverage} and has made the Dean's list.")
        print("The program will now restart.\n\n\n")
    elif gradePointAverage >= HONORROLL:
        print(f"{firstName} {lastName} has a GPA of {gradePointAverage} and has made the Honor Roll.")
        print("The program will now restart.\n\n\n")
    else:
        print(f"{firstName} {lastName} has a GPA of {gradePointAverage}.")
        print("The program will now restart.\n\n\n")