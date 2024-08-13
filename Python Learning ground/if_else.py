import time

def intro():
    print("Welcome to Quizbee")
    time.sleep(2)
    print("You have to answer 5 questions or else you will be punished")
    time.sleep(2)
    print("Let the game begin!")
    time.sleep(2)
    print()

def Question1():
    question1 = ''
    while question1 != 'A' and question1 != 'B':
        print('What is the capital of France?')
        print("A for Paris")
        time.sleep(2)
        print("B for Rome")
        time.sleep(2)
        answer = input('Answer:').upper()

        if answer == 'A':
            print('Good job!')
            break  # Exit the loop once a valid answer is given
        elif answer == 'B':
            print('Incorrect, please study more.')
            break  # Exit the loop even for the incorrect answer
        else:
            print("Read the instructions, INVALID!!")
            time.sleep(2)

    # Proceed to the next question
    Question2()

def Question2():
    question2 = ''
    while question2 != 'A' and question2 != 'B':
        print('Which number is even?')
        print("A for 3")
        time.sleep(2)
        print("B for 4")
        time.sleep(2)
        answer = input('Answer:').upper()

        if answer == 'B':
            print('Good job!')
            break
        elif answer == 'A':
            print('Incorrect, please study more.')
            break
        else:
            print("Read the instructions, INVALID!!")
            time.sleep(2)

# Call the functions to start the quiz
intro()
Question1()
