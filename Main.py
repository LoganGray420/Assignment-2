#Importing a function that allows random options for the rock, paper, scissors function
import random

#Displaying the options for the user to pick which function to run
print("Please choose which function you want to use:")
print("0. Modulo Calculator")
print("1. Integer Division Calculator")
print("2. Float & Integer Calculator")
print("3. For Loop Counter")
print("4. Integer and Float Addition ")
print("5. Print ASCII values of letters in a string")
print("6. Change Machine")
print("7. Rock Paper Scissors")
print("8. Mario wins a level")

#Asking the user which of the functions they want to run
user_input= (int(input("What is your selection?")))




#Declaring that you want to run the modulo calculator function
def modulo_calculator():
    #Getting an input from the user as the first integer needed to run the calculation. Using int to declare it as a whole number
     x=int (input("Please enter your first number"))
     #Getting the second int from the user for the calculation
     y=int (input ("Please enter your second number"))

    #Running the calculation using z as the answer and finding out what the remainder of x%y
     z=x%y
     #Displaying the answer as a print and declaring z as a string so the modulo is properly displayed
     print ("The result is", str(z))

#Dispaying the end of the function but leaving it commented out so that the program does not try to run this without first being called
#modulo_calculator()
#Declaring our int division function allowing the program to call it
def int_division():

    #Getting an int from the user to be divided using x as the variable
    x=int (input("Please enter your first number"))
    #Getting our dividend from the user using y as the variable
    y=int (input("Please enter your dividend"))
    #Running the calculation of the first user input divided by the second using z as our answer
    z= x/y
    #Returning the solution to the user and declaring z as a string so it is properly shown
    print("The result is", str(z))
#Dispaying the end of the function but leaving it commented out so that the program does not try to run this without first being called
#int_division()

def float_and_int():
    #Allowing the user to input a float instead of just an int
    x= float(input("Please enter your first float"))
    y= float(input("Please enter your second float"))

    z= x/y
    #Returning an int to the user so the answer is rounded at the end
    print ("The result is:", + int(z))

#float_and_int()

def for_loop_counter():
    #Getting the initial number from the user as a float allowing them to start the counter as a decimal
     initial= float (input ("what is the initial value of the counter "))
     #Getting the whole number of times the user wants the loop to run
     count= int(input("How many times is the loop running?"))
     #Getting the amount that the loop increments by each time from the user. Allowing it as a float so it can increase or decrease by a decimal
     increment= float(input("How much should the counter increment by?"))
     #Asking the user if the counter is positive or negative so we know to increment or decrease by the given increment 
     #Couldn't get the decrement to work properly.
     is_positive= (input("Should the counter incriment or decrement? y/n"))
    
     #Incrementing the counter the number of times the user declared(count)
     for increment in range(count):
        #starting at the user declared value and adding the incremental value each time it is less than the count
            initial= initial + increment
            #Returning the answer to the user. Displaying initial since it was the value that changed
     print("The final value is", initial)
        

#for_loop_counter

def int_float_addition():

    x= int (input("Please enter your int"))
    y=float (input("Please enter your float"))

    z= x+y
    #Displaying the sum but allowing z to be a float so it isn't rounded
    print("The sum of the two numbers is:", float(z))

#int_float_addition()

def ascii_printing():
    #Getting the user input for what they want the value of
   user_string=input("Enter a string you want the values of")
   #Assigning ascii values as an array
   ascii_values = []
   #For loop that finds each character in the string and assigns the ascii value to it
   for character in user_string:
        #Function that converts the individual character to an ascii value
        ascii_values.append(ord(character))
    #Displaying each individual ascii value
   print (ascii_values) 

#ascii_printing()

def change_machine():
    #Using c (coins) as my int
    c=int(input('Please enter an amount between 0-99:'))
    #Dividing the user input by 25 to represent quarters and displaying how many quarters are dispensed 
    print(c//25, "quarters")
    #Determining the remainder after we take out the quarters to find out how many dimes we need
    c = c%25
    #Dime calculation
    print(c//10, "dimes")
    #Finding the remainder to see if we need to add a nickle
    c = c%10
    print(c//5, "nickles")
    c = c%5

#change_machine()

def rock_paper_scissors():

    user_action = input("Enter a choice (rock, paper, scissors): ")
    #Only allowing the user to input the specific rps choices
    possible_actions = ["rock", "paper", "scissors"]
    #Getting a random choice for the AI
    ai_action = random.choice(possible_actions)
    #Returning to the user what both they and the AI chose
    print(f"You chose {user_action}, AI chose {ai_action}.\n")
    #Creating a tie condition if the AI and user choose the same option
    if user_action == ai_action:
        #Returning to the user that they chose the same option as the AI
        print(f"Both players selected {user_action}. It's a tie!")
        #If the user chooses rock (going through each possibility of the user selection and the ai selection):
    elif user_action == "rock":
        #Determing the result if the AI randomly selects scissors
        if ai_action == "scissors":
            #User wins
            print(" You win!")
            #If the AI selects an option that isn't scissors or rock (picking paper):
        else:
            print(" You lose.")
        #If the user picks paper run this part of the if statement
    elif user_action == "paper":
        if ai_action == "rock":
            print(" You win!")
        else:
            #If the ai selects scissors
            print(" You lose.")
    elif user_action == "scissors":
        if ai_action == "paper":
            print("You win!")
        else:
            print("You lose.")
    
  
#rock_paper_scissors()


def mario_level():
  
    #Asking the user how high they want the stairs. 
    print('Enter how many stairs you want:');
    #Using h as my int from the user input
    h = int(input());
    #Creating an error if the user tries to have stairs that are too big or small
    while(h<0 or h > 10):
        print("That is an invalid input")
       
    #For loop using i to iterate how many #'s to print depending on user input while having h-1 so that the stairs print to the
    #left rather than right
    for i in range(h):
        print(" "*(h-i)+"#"*(i+1))
#mario_level()


#Running the corresponding function from the user input as an if statement while returning "not a valid selection" if the user 
#does not input a valid number
#Putting it at the end so it recognizes that all the functions are properly defined
if user_input== 0:
    modulo_calculator()
elif user_input==1:
    int_division()
elif user_input==2:
    float_and_int()
elif user_input==3:
    for_loop_counter()
elif user_input==4:
    int_float_addition()
elif user_input==5:
    ascii_printing()
elif user_input==6:
    change_machine()
elif user_input==7:
    rock_paper_scissors()
elif user_input==8:
    mario_level()
else:
    print("Not a valid selection")



