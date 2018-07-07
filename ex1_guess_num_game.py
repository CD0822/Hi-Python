#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename: ex1_guess_num_game.py
# History: July 2,2018 - [Dan Chen] created
# This file is written for a game guessing a random int number.

import random

answer = random.randint(0,100)
print(answer)
count = 5

while count > 0:
    temp = input("Please input your guess number(0-100): ")
    if temp.isdigit():
        num = int(temp)
        count -= 1
        if num == answer:
            exit("Congradulations! %d is the right answer! \n" %num)
        elif count == 0:
            exit("You have run out of all the chances, and the correct answer is %d" % (answer))
        elif num > answer:
            print("Your number %d is bigger, you only have %d chances. \n" %(num,count))
        elif num < answer:
            print("Your number %d is smaller,you only have %d chances. \n" %(num,count))
    else:
        print("Error: %r is not a number! Please input again!" %temp)
    
        




