import os
path = '/Users/Saul/Documents/GitHub/Code/wordlist.txt'
f = open(path, 'r')

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

def check(length, letters, word):
    if letters in word:
        return word

def find():
    global length
    global letters
    
    while True:
        word = f.readline()
        print(check(length, letters, word))


find()