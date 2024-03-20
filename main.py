import math
import random

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

    if number == 1:
        question = "What is the smallest number in this list? " + str(randomList)

    elif number == 2:
        question = "What is the biggest number in this list? " + str(randomList)

    elif number == 3:
        question = "What is the sum of the numbers in this list? " + str(randomList)

    else:
        question = "What is the average of the numbers in this list? " + str(randomList) + "(round UP to nearest integer)"

    return question

###################################
def get_correct_answer(number, randomList):
    answer = None

    if number == 1:
        answer = min(randomList)
        
    elif number == 2:
        answer = max(randomList)
        
    elif number == 3:
        answer = sum(randomList)
        
    else:
        answer = math.ceil(sum(randomList) / len(randomList))

    return answer

##################################
def is_valid(value):
    if value.upper() in ["E", "M", "H"]:
        return True

    return False

###################################
def get_difficulty_attributes(difficulty):
    if difficulty == "E":
        return [2, 3, 1, 5]
    
    elif difficulty == "M":
        return [4, 5, 3, 12]
    
    return [6, 8, 10, 25]

##################################
def print_selcted_difficulty(difficulty):
    text = ""

    if difficulty == "E":
        text = "Easy"
        
    elif difficulty == "M":
        text = "Medium"
        
    else:
        text = "Hard"

    print(text + " difficulty selected!\n")

###############################

print("Welcome to the Number List Test program.")

difficulty = input("Select a difficulty:\n[E]asy\n[M]edium\n[H]ard\n")

while True:
    if is_valid(difficulty):
        print_selcted_difficulty(difficulty)
        break
    
    difficulty = input("Invalid choice! Enter E, M or H.\n")

attributes = get_difficulty_attributes(difficulty)

questions = attributes[0]
quantity = attributes[1]
minimum = attributes[2]
maximum = attributes[3]

score = 0

for i in range(questions):
    randomList = None

    print("Question" + str(i + 1) + " of " + str(questions) + ".")

    if question + 1 < questions:
        randomList = random_list(quantity, minimum, maximum)
    else:
        print("Challenge questions!")
        randomList = random_list(quantity, minimum * 2, maximum * 2)

    number = random.randint(1,4)

    print(get_question(number, randomList))
    
    correctAnswer = get_correct_answer(number, randomList)
    
    answer = int(input())

    if answer == correctAnswer:
        print("Correct!\n")
        score = score + 1
    else:
        print("Incorrect! Correct answer was " + str(correctAnswer) + ".\n")

print("Test complete!\nYou scored", str(score) + "/" + str(questions), "(" + str(round(score / questions * 100, 1)) + "%).")

if score == questions:
    print("Perfect score, well done!")










