with open("morse.txt", "r", encoding="utf-8") as file:
    morse = [i.strip().split(" ") for i in file]

with open("text.txt", "r", encoding="utf-8") as file:
    text_morse = [i for i in file]

with open("morsetext.txt", "r", encoding="utf-8") as file:
    morse_text = [i for i in file]


def alphabet_to_morse(text):
    m = ""
    for i in range(len(text)):
        for j in range(len(morse)):
            if text[i].upper() == morse[j][0]:
                m += morse[j][1] + " "
        if text[i] == " ":
            m += " "
    return m


def morse_to_alphabet(text):
    a = ""
    temp = ""
    for i in range(len(text)):
        if text[i] != " ":
            temp += text[i]
        if text[i] == " " or i + 1 == len(text):
            for j in range(len(morse)):
                if temp == morse[j][1]:
                    a += morse[j][0]
                    temp = ""
        if text[i] == " " and len(text) != i + 1:
            if text[i + 1] == " ":
                a += " "
    return a


#print(morse)
#print(text)
#print(alphabet_to_morse("Hello world hello\nDawno dawno temu"))
for i in range(len(text_morse)):
    print(alphabet_to_morse(text_morse[i]))
for i in range(len(morse_text)):
    print(morse_to_alphabet(morse_text[i]))

