import time
import sys

score = 0

def intro():
    print("Welcome to Quizbee")
    time.sleep(1)
    print("You have to answer 5 questions or else you will be punished")
    time.sleep(1)
    print("Let the game begin!")
    time.sleep(1)
    print()

def Question1():
    global score
    question1 = ''
    while question1 != 'A' and question1 != 'B':
        print('What is the capital of France?')
        time.sleep(1)
        print("A for Paris")
        time.sleep(1)
        print("B for Rome")
        time.sleep(1)
        answer = input('Answer:').upper()  # Convert input to uppercase to avoid case sensitivity

        if answer == 'A':
            print('Good job! DUMBASS!!')
            score += 1
            break
        elif answer == 'B':
            print('DUMBASS, please study more.')
            break
        else:
            print("Read the instructions, INVALID!!")
            break

    Question2()


def Question2():
    global score
    question2 = ''
    while question2 != 'A' and question2 != 'B':
        print('Which number is even?')
        time.sleep(1)
        print("A for 3")
        time.sleep(1)
        print("B for 4")
        time.sleep(1)
        answer = input('Answer:').upper()  # Convert input to uppercase to avoid case sensitivity

        if answer == 'B':
            print('Good job! DUMBASS!!')
            score += 1
            break
        elif answer == 'A':
            print('DUMBASS, please study more.')
            break
        else:
            print("bitch INVALID!!")
            break
    
    Question3()

def Question3():
    global score
    question3 = ''
    while question3 != 'A' and question3 != 'B':
        print('Which animal is known as the "King of the Jungle"?')
        time.sleep(1)
        print("A for Lion")
        time.sleep(1)
        print("B for Wolf")
        time.sleep(1)
        answer = input('Answer:').upper()  # Convert input to uppercase to avoid case sensitivity

        if answer == 'A':
            print('Good job! DUMBASS!!')
            score += 1
            break
        elif answer == 'B':
            print('DUMBASS, please study more.')
            break
        else:
            print("bitch INVALID!!")
            break
    Question4()

def Question4():
    global score
    question3 = ''
    while question3 != 'A' and question3 != 'B':
        print('What is the boiling point of water at sea level?')
        time.sleep(1)
        print("A for 100°C")
        time.sleep(1)
        print("B for 50°C")
        time.sleep(1)
        answer = input('Answer:').upper()  # Convert input to uppercase to avoid case sensitivity

        if answer == 'A':
            print('Good job! DUMBASS!!')
            score += 1
            break
        elif answer == 'B':
            print('DUMBASS, please study more.')
            break
        else:
            print("bitch INVALID!!")
            break
    Question5()

def Question5():
    global score
    question3 = ''
    while question3 != 'A' and question3 != 'B':
        print('Which color is a primary color?')
        time.sleep(1)
        print("A for Blue")
        time.sleep(1)
        print("B for Green")
        time.sleep(1)
        answer = input('Answer:').upper()  # Convert input to uppercase to avoid case sensitivity

        if answer == 'A':
            print('Good job! DUMBASS!!')
            score += 1
            break
        elif answer == 'B':
            print('DUMBASS, please study more.')
            break
        else:
            print("bitch INVALID!!")
            break
    end_quiz()

def end_quiz():
    print(f"You got {score} correct answers.")

# Call the functions
intro()
Question1()
sys.exit()

#DONE AND DUSTED
#WORKING AS HELL
#must be nice if nattrrack kung ilan yung mali at tama.





     
