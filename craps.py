"""
Filename: craps.py
Author: Nick Saylock
Date: 2025-12-23
Version 1.0
"""
import random

def main():
    #Main Code Block
    print("craps")
    drawCrapsTable()

def drawCrapsTable():
    drawPlaceBets()
    drawComeLines()
    drawFieldBets()

def drawComeLines():
    for i in range(34):
        if i == 0 or i == 17:
            print(' ',end='')
        print("\u2582",end="")
    print()
    for i in range(2):
        if i == 1:
            print("\u2595   DON\'T COME   \u2595",end='')
            print("\u2595      COME      \u2595")
        for j in range(36):
            if j == 0 or j == 17 or j == 18 or j == 35:
                print("\u2595",end="")
            else:
                print(" ",end="")
        print()
    for i in range(34):
        if i == 0 or i == 17:
            print(' ',end='')
        print("\u2594",end="")
    print()

def drawFieldBets():
    # Bullet = \u2219
    for i in range(35):
        if i == 0:
            print(' ',end='')
        print("\u2582",end="")
    print()
    for i in range(3):
        if i == 1:
            print("\u2595   2 \u2219 3 \u2219 4 \u2219 9 \u2219 10 \u2219 11 \u2219 12   \u2595")
        if i == 2:
            print("\u2595              FIELD               \u2595")
        for j in range(36):
            if j == 0 or j == 35:
                print("\u2595",end="")
            else:
                print(" ",end="")
        print()
    for i in range(35):
        if i == 0:
            print(' ',end='')
        print("\u2594",end="")
    print()
    
def drawPlaceBets():
# Place bets ------------------------------------------------------    
# KEY: \u2582 = _ (line touching bottom of char space)
#      \u258F = | (line touch left of char space)
#      \u2595 = | (line touch right of char space)
#      \u2594 = - (line touch top of char space)

    placeBetHorLine("\u2582")
    placeBetVertLine()
    print(" \u258F   4   \u2595",end=" ")
    print("\u258F   5   \u2595",end=" ")
    print("\u258F   6   \u2595",end=" ")
    print("\u258F   8   \u2595",end=" ")
    print("\u258F   9   \u2595",end=" ")
    print("\u258F  10   \u2595",end="")
    print()   
    placeBetVertLine()
    placeBetHorLine("\u2594")

def placeBetVertLine():
    for i in range(6): # Range must be same as length of top lines
        if i == 0:
            print(' ',end='')
        print("\u258F       \u2595 ", end="")
    print()

def placeBetHorLine(line):
    for i in range(6):
        if i == 0:
            print(' ',end='')
        for i in range(9): # range is length of bottom lines (same as top)
            print(line,end="")
        print(" ",end="")
    print()

if __name__ == "__main__":
    main()