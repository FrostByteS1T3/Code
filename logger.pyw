# -------MUST BE RUN AS ROOT--------
import keyboard

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while keyboard.is_pressed('q') == False:
    for i in letters:
        if keyboard.is_pressed(i) == True:
            print(i)