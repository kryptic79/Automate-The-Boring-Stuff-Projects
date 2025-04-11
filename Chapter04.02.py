# Chapter 4
# Coin Flip Streaks

import random
#Remeber to always read the question before starting
#Lesson don't reinvent the wheel

def headsOrTails():
    flip = random.randint(0,1)
    if flip == 0:
        return 'H'
    elif flip == 1:
        return 'T'

def loop100():
    choices = [headsOrTails()]
    for i in range(0,99):
        choices.append(headsOrTails())
    return choices


def checksForStreaks(array):
    count = 1
    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            count += 1
            if count == 6:
                return 1  
        else:
            count = 1
    return 0
                   
                   
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
      choices = loop100()
      numberOfStreaks += int(checksForStreaks(choices))
      print(numberOfStreaks)
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
