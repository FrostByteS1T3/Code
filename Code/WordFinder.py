import os
f = open('wordlist.txt', 'r')

length = int
letters = []

def get():
    global length
    global letters
    num = input('Ammount of letters: ')
    num = int(num)
    letters = []
    for i in range(0, num):
        letters.append(input('Letter: '))
    length = len(letters)
#print(set(letters))
get()
run = True
while run == True:
    word = f.readline()
    if length == 1:
        if len(word) - 1 == length and letters[0] in word:
            for b in range(length):
                if letters[b] not in word:
                    break
                elif letters[b] in word:
                    if letters[0] not in word:
                        break
                    else:
                        os.system('clear')
                        print(word)
                        break
    
    if length == 2:
        if len(word) - 1 == length and letters[0] and letters[1] in word:
            for b in range(length):
                if letters[b] not in word:
                    break
                elif letters[b] in word:
                    if letters[0] not in word or letters[1] not in word:
                        break
                    else:
                        os.system('clear')
                        print(word)
                        break
    if length == 3:
        if len(word) - 1 == length and letters[0] and letters[1] and letters[2] in word:
            for b in range(length):
                if letters[b] not in word:
                    break
                elif letters[b] in word:
                    if letters[0] not in word or letters[1] not in word or letters[2] not in word:
                        break
                    else:
                        os.system('clear')
                        print(word)
                        break
    if length == 4:
        if len(word) - 1 == length and letters[0] and letters[1] and letters[2] and letters[3] in word:
            for b in range(length):
                if letters[b] not in word:
                    break
                elif letters[b] in word:
                    if letters[0] not in word or letters[1] not in word or letters[2] not in word or letters[3] not in word:
                        break
                    else:
                        os.system('clear')
                        print(word)
                        break


    if length == 5:
        if len(word) == length and letters[0] and letters[1] and letters[2] and letters[4] and letters[3] in word:
            for b in range(length):
                if letters[b] not in word:
                    break
                elif letters[b] in word:
                    if letters[0] not in word or letters[1] not in word or letters[2] not in word or letters[3] not in word or letters[4] not in word:
                        break
                    else:
                        os.system('clear')
                        print(word)
                        break

    

    