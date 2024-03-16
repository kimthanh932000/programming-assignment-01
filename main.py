import math
import random

######################################
def random_list(quantity, minimum, maximum):
    result = []
    
    for i in range(quantity):
        num = random.randint(minimum, maximum)
        result.append(num)

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

print("Welcome to the Number List Test program.")

difficulty = input("Select a difficulty:\n[E]asy\n[M]edium\n[H]ard\n").upper()

while True:
    if difficulty in ['E', 'M', 'H']:
        break
    difficulty = input("Invalid choice! Enter E, M or H.\n").upper()

if difficulty == 'E':
    print("Easy difficulty selected!\n")
elif difficulty == 'M':
    print("Medium difficulty selected!\n")
else:
    print("Hard difficulty selected!\n")

questions = None
quantity = None
minimum = None
maximum = None

if difficulty == 'E':
    questions = 2
    quantity = 3
    minimum = 1
    maximum = 5
    
elif difficulty == 'M':
    questions = 4
    quantity = 5
    minimum = 3
    maximum = 12

else:
    questions = 6
    quantity = 8
    minimum = 10
    maximum = 25

score = 0
randomList = None

for question in range(questions):
    print("Question" + str(question + 1) + " of " + str(questions) + ".")

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







    












