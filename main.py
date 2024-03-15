import random

def random_list(quantity, minimum, maximum):
    result = []
    
    for i in range(quantity):
        num = random.randint(minimum, maximum)
        result.append(num)

    return result

##############################################
import math

print("Welcome to the Number List Test program.")

difficulty = input("Select a difficulty:\n[E]asy\n[M]edium\n[H]ard\n").upper()
##print("input:", difficulty)

while True:
    if difficulty in ['E', 'M', 'H']:
        break
    difficulty = input("Invalid choice! Enter E, M or H.\n")

if difficulty == 'E':
    print("Easy difficulty selected!")
elif difficulty == 'M':
    print("Medium difficulty selected!")
else:
    print("Hard difficulty selected!")

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
randNumbers = None

for question in range(questions)
    print("Question", question + 1, "of", questions, ".")

    # not up to final question
    if question + 1 < questions:
        randNums = random_list(quantity, minimum, maximum)

    else:
        print("Challenge questions!")
        randNums = random_list(quantity, minimum * 2, maximum * 2)

    number = random.randint(1,4)

    if number == 1:
        value = int(prompt("What is the smallest number in this list?", randNumbers))
        answer = min(randNumbers)
        
        if value == answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect! Correct answer was", answer)
            
    elif number == 2:
        value = int(prompt("What is the biggest number in this list?", randNumbers))
        answer = max(randNumbers)
        
        if value == answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect! Correct answer was", answer)

    elif number == 3:
        value = int(prompt("What is the sum of the numbers in this list?", randNumbers))
        answer = sum(randNumbers)
        
        if value == answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect! Correct answer was", answer)

    else:
        value = int(prompt("What is the average of the numbers in this list?", randNumbers))
        answer = math.ceil(sum(randNumbers) / len(randNumbers))
        
        if value == answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect! Correct answer was", answer)

print("Test complete!\n You scored", score, "/", questions, "(", round(score / questions * 100, 1), "%).")

if score == questions:
    print("Perfect score, well done!")







    












