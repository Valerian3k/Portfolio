with open("quiz.txt", "r", encoding="utf-8") as file:
    questions = [i.strip() for i in file]


def quiz():
    score = 0
    for i in range(len(questions)):
        if i % 9 != 0 or i == 0:
            if i % 9 < 7:
                print(questions[i])
            elif i % 9 == 7:
                x = input("Choose your answer (a,b,c,d): ")
                if x == questions[i]:
                    score += 1
                    print('Your answer is correct!')
                else:
                    print(questions[i + 1])
                    print('Your answer is incorrect!')
        else:
            print("\n")

    print(f"\n\nYour end score is: {score}/10")


quiz()
