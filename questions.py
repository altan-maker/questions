import random
random.seed(100)

answers = []

answers.append(raw_input("Enter what is your name?:"))
print len(answers)
answers.append(raw_input("Enter what is your quest?:"))
print len(answers)

for x in range(0, 4):
    r = random.randint(0, 4)
    print(r)

    if (r == 1):
         answer = int(raw_input("Enter what is 2+2?:"))
         if (answer == 4):
             answers.append(answer)
         else:
             print "wrong answer"
             break

    elif (r == 2):
        answer = int(raw_input("Enter what is 2x2?:"))
        if (answer == 4):
            answers.append(answer)
        else:
            print "wrong answer"
            break

    elif (r == 3):
        answers.append(raw_input("Enter what is 3+3?:"))

print answers
