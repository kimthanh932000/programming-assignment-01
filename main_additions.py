import math
import random
import time

######################################
def random_list(quantity, minimum, maximum):
    result = []
    
    for i in range(quantity):
        number = random.randint(minimum, maximum)
        result.append(number)

    return result

##################################
def get_question(number, randomList):
    question = ""
    randomChoice = None

    if number == 1:
        question = "What is the smallest number in this list? " + str(randomList)

    elif number == 2:
        question = "What is the biggest number in this list? " + str(randomList)

    elif number == 3:
        question = "What is the sum of the numbers in this list? " + str(randomList)

    elif number == 4:
        question = "What is the average of the numbers in this list? " + str(randomList) + "(round UP to nearest integer)"

    elif number == 5:
        question = "What is the difference between the smallest and biggest numbers in this list? " + str(randomList)

    else:
        randomChoice = random.choice(randomList)
        question = "How many " + str(randomChoice) + "s are there in this list? " + str(randomList)
        
    return [question, randomChoice]

###################################
def get_correct_answer(number, randomList, randomChoice):
    answer = None

    if number == 1:
        answer = min(randomList)
        
    elif number == 2:
        answer = max(randomList)
        
    elif number == 3:
        answer = sum(randomList)
        
    elif number == 4:
        answer = math.ceil(sum(randomList) / len(randomList))

    elif number == 5:
        answer = max(randomList) - min(randomList)

    else:
        answer = randomList.count(randomChoice)

    return answer

##################################
def is_valid(value):
    if value in ["E", "M", "H", "EASY", "MEDIUM", "HARD"]:
        return True

    return False

###################################
def get_difficulty_attributes(difficulty):
    if difficulty in ["E", "EASY"]:
        return [2, 3, 1, 5]
    
    elif difficulty in ["M", "MEDIUM"]:
        return [4, 5, 3, 12]

    return [6, 8, 10, 25]

##################################
def print_selcted_difficulty(difficulty):
    text = ""

    if difficulty in ["E", "EASY"]:
        text = "Easy"
        
    elif difficulty in ["M", "MEDIUM"]:
        text = "Medium"
        
    else:
        text = "Hard"

    print(text + " difficulty selected!\n")

###############################

print("Welcome to the Number List Test program.")

difficulty = input("Select a difficulty:\n[E]asy\n[M]edium\n[H]ard\n").upper()

while True:
    if is_valid(difficulty):
        print_selcted_difficulty(difficulty)
        break
    
    difficulty = input("Invalid choice! Enter E, M or H.\n").upper()

attributes = get_difficulty_attributes(difficulty)

questions = attributes[0]
quantity = attributes[1]
minimum = attributes[2]
maximum = attributes[3]

score = 0

for i in range(questions):
    randomList = None

    print("Question " + str(i + 1) + " of " + str(questions) + ".")

    if i + 1 < questions:
        randomList = random_list(quantity, minimum, maximum)
    else:
        print("Challenge questions!")
        randomList = random_list(quantity, minimum * 2, maximum * 2)

    number = random.randint(1,6)

    results = get_question(number, randomList)
    
    print(results[0])
        
    correctAnswer = get_correct_answer(number, randomList, results[1])

    timeBefore = None
    timeAfter = None
    answer = None

    while True:
        try:
            timeBefore = time.time()
            answer = int(input())
            timeAfter = time.time()
            break
        except ValueError:
            print('Invalid input! Answer contains integer only.')
    
    timeDiff = round(timeAfter - timeBefore, 1)

    if answer == correctAnswer:
        print("Correct! You answered in", timeDiff, "seconds.\n")
        score = score + 1
    else:
        print("Incorrect! Correct answer was " + str(correctAnswer) + ". You answered in " + str(timeDiff) + " seconds.\n")

print("Test complete!\nYou scored", str(score) + "/" + str(questions), "(" + str(round(score / questions * 100, 1)) + "%).")

if score == questions:
    print("Perfect score, well done!")










