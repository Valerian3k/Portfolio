userNumbers = []

with open("dl.txt", "r", encoding="utf-8") as file:
    all_numbers = [i.strip().split(" ")[2].split(",") for i in file]


def add_numbers():
    i = 1
    while i < 7:
        x = input(f"Enter your {i} number(1 to 49): ")
        if 1 <= int(x) <= 49:
            b = True
            for j in range(len(userNumbers)):
                if userNumbers[j] == x:
                    print("Numbers can't repeat!")
                    b = False
            if b:
                userNumbers.append(x)
                i += 1
        else:
            print("Enter number from 1 to 49!")

    print(userNumbers)


def check_number():
    shoots = [0 for _ in range(4)]
    for i in range(len(all_numbers)):
        hits = 0
        for j in range(len(userNumbers)):
            for k in range(len(all_numbers[i])):
                if all_numbers[i][k] == userNumbers[j]:
                    hits += 1
                    break
        if hits >= 3:
            shoots[hits - 3] += 1

    return shoots


add_numbers()
s = check_number()
print(f"Three: {s[0]} \nFour: {s[1]} \nFive: {s[2]} \nSix: {s[3]} \n")
