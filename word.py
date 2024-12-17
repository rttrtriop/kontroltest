import random

words = ["apple", "banana", "grape", "lemon", "mango", "peach", "plum", "berry", "cherry", "date", "fig", "kiwi", "lime", "melon", "pear", "peach", "plum", "berry", "cherry", "date"]

word = random.choice(words)
countt = len(word)
underscopes = "_" * countt
trueguess = []

def trueword():
    while '_' in shifr:
        guess = input("введите букву :   ")

        if guess in trueguess :
            print('такая буква уже угадана')
        elif guess in word:
            trueguess.append(guess)
            start()
        else :
            print('такой буквы не в слове')



def start():
    global shifr
    shifr = ""
    for letter in word:
        if letter in trueguess:
            shifr += letter
        else :
            shifr += '_'
    print(shifr)


start()
trueword()
print('you win')
