"""
Filename: craps.py
Author: Nick Saylock
Date: 2025-12-23
Version 1.0
"""
import random

# DICE KEY - \u2680 = 1
#            \u2681 = 2
#            . . .
#            \u2685 = 6

# KEY: \u2582 = _ (line touching bottom of char space)
#      \u258F = | (line touch left of char space)
#      \u2595 = | (line touch right of char space)
#      \u2594 = - (line touch top of char space)
def main():
    print("            CRAPS V1.0\n\n\n\n")

    passBet = 0
    bankroll = 500
    minBet = 25
    maxBet = 2000
    intCheck = False
    playerQuit = False
    gameOn = False

    print(' Welcome to NS Casino Craps Table!')
    print(' You have $500 to make it big or lose it all')
    print(' The minimum bet is $25. Maximum is $2000. Bet $0 to exit.')
    print(' Don\'t pass is currently unavailable. Place your bet on the pass line')
    print('\n\n\n')
    drawInitialCrapsTable()
    
    print('\n\n Bankroll: $', bankroll, sep='')
    print()
    while bankroll > 0 and playerQuit == False:     # PASS LINE BET --------------
        while passBet < minBet or passBet > maxBet or passBet > bankroll:
            try:
                passBet = int(input(' Pass Line Bet: $'))
                if passBet == 0:
                    playerQuit = True
                    break
                elif passBet < minBet:
                    print(' The minimum bet is $',minBet,sep='')
                elif passBet > maxBet:
                    print(' The maximum bet is $',maxBet,sep='')
                elif passBet > bankroll:
                    print(' You only have $',bankroll,'to bet')
                else:
                    bankroll -= passBet
            except ValueError:
                print(' Invalid Input: Enter a Number')
        if playerQuit:
            print(' Player Quit')
            break    
                        # END SET PASS LINE BET #
        
        #############  Come out roll #####################################3
        sum = 7   
        target = 0  
        while gameOn == False and bankroll >= 0:
            bb = input(' Press Enter to Roll')
            if bb == 'quit': #Make way to quit -- delete later
                playerQuit = True
                break
            dice = dice_roll()
            sum = dice[2]
            print_dice_roll(dice)
            if bankroll < minBet:
                print(' You don\'t have enough money left')
                playerQuit = True
            elif sum < 4 or sum == 12:
                bankroll -= passBet
                print(' Craps! You lost $',passBet,sep='')
            elif sum == 7:
                bankroll += passBet
                print('Lucky Seven! You won $',passBet,sep='')
            elif sum == 11:
                bankroll += passBet
                print('YO Eleven! You won $',passBet,sep='')
            else:
                target = sum
                gameOn = True

            drawCrapsTable(bankroll, passBet, target)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ################## GAME ON #########################################
        while gameOn == True:
            bb = input(' Press Enter to Roll')
            if bb == 'quit': #Make way to quit -- delete later
                playerQuit = True
                break  
            validPlaceBet = False
            while validPlaceBet == False:
                placeBetInitializer = input('What Number for Place Bet? (0 for None): ')
                if placeBetInitializer == 0:
                    break
                elif { placeBetInitializer == 4 or placeBetInitializer == 5
                 or placeBetInitializer == 6 or placeBetInitializer == 8
                 or placeBetInitializer == 9 or placeBetInitializer == 10 }:
                    validPlaceBet = True
            



            dice = dice_roll()
            sum = dice[2]
            print_dice_roll(dice)
            if sum == target:
                bankroll += passBet
            elif sum == 2:
                print('Snake Eyes')
            elif sum == 3:
                print('Craps Three')
            elif sum == 4:
                print('Four')
            elif sum == 5:
                print('Five')
            elif sum == 6:
                print('Six')
            elif sum == 7:
                print('Seven Out')
                gameOn = False
            elif sum == 8:
                print('Eight')
            elif sum == 9:
                print('Nine')
            elif sum == 10:
                print('Ten')
            elif sum == 11:
                print('Yo Eleven')
            elif sum == 12:
                print('Midnight')
        
#   ^  End Main Game Loop



def dice_roll():
    dice = []        
    for i in range(2):
        die = random.randint(1, 6)
        dice.append(die)
    dice.append(dice[0] + dice[1])
    return dice

def drawInitialCrapsTable():
    drawPlaceBets()
    drawComeLines()
    drawFieldBets()
    drawHardways()
    drawCrapsBets()

def drawCrapsTable(bankroll, passBet, target):
    if target == 0:
        pass
    elif target == 4:
        print('     ON')
    elif target == 5:
        print('              ON')
    elif target == 6:
        print('                        ON')
    elif target == 8:
        print('                                   ON')
    elif target == 9:
        print('                                             ON')
    else:
        print('                                                       ON')
    
    drawPlaceBets()
    drawComeLines()
    drawFieldBets()
    drawHardways()
    drawCrapsBets()
    drawPassLine(bankroll, passBet)

def drawPlaceBets():        # Place bets ---------------------------    
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
##################### END Place BETS ##############################

def drawComeLines():
    for i in range(58): #Top Lines
        if i == 0 or i == 20:
            print(' ',end='')
        print("\u2582",end="")
    print()

    for i in range(2): # Word Lines
        if i == 1:
            print("\u2595     DON\'T COME    \u2595",end='')
            print("\u2595                COME                 \u2595",end="")
            print()

        for j in range(60): # Vert Lines
            if j == 0 or j == 20 or j == 21 or j == 59:
                print("\u2595",end="")
            else:
                print(" ",end="")
        print()

    for i in range(58): # Bottom Lines
        if i == 0 or i == 20:
            print(' ',end='')
        print("\u2594",end="")
    print()

def drawFieldBets():
    # Bullet = \u2219
    for i in range(59):
        if i == 0:
            print(' ',end='')
        print("\u2582",end="")
    print()

    for i in range(3):
        if i == 1:
            print("\u2595              2 \u2219 3 \u2219 4 \u2219 9 \u2219 10 \u2219 11 \u2219 12                \u2595")
        if i == 2:
            print("\u2595                        FIELD                             \u2595")
        for j in range(60):
            if j == 0 or j == 59:
                print("\u2595",end="")
            else:
                print(" ",end="")
        print()

    for i in range(59):
        if i == 0:
            print(' ',end='')
        print("\u2594",end="")
    print()
    
def drawHardways():
    # DICE KEY - \u2680 = 1
#            \u2681 = 2
#            . . .
#            \u2685 = 6

# KEY: \u2582 = _ (line touching bottom of char space)
#      \u258F = | (line touch left of char space)
#      \u2595 = | (line touch right of char space)
#      \u2594 = - (line touch top of char space)
    for i in range(6):
        if i == 1:
            print('\u2595               H   A   R   D   W   A   Y   S               \u258F',end='')
        if i == 3:
            print('\u2595     FOUR     ',end='')
            print('\u2595     TEN      ',end='')
            print('\u2595     SIX      ',end='')
            print('\u2595     EIGHT    \u258F',end='')
        if i == 4:
            print('\u2595     \u2681 \u2681      ',end='')
            print('\u2595     \u2684 \u2684      ',end='')
            print('\u2595     \u2682 \u2682      ',end='')
            print('\u2595     \u2683 \u2683      \u258F',end='')
        for j in range(61):
            if i == 0:
                if j > 0 and j < 60:
                    print('\u2582',end='')
                else:
                    print(' ',end='')
            if i == 2:
                if j > 0 and j < 60:
                    print('\u2582',end='')
                elif j == 0:
                    print('\u2595',end='')
                else:
                    print('\u258F',end='')
            if i == 5:
                if j > 0 and j < 60:
                    print('\u2594',end='')
                else:
                    print(' ',end='')
        print()

def drawCrapsBets():
    # DICE KEY - \u2680 = 1
#            \u2681 = 2
#            . . .
#            \u2685 = 6

# KEY: \u2582 = _ (line touching bottom of char space)
#      \u258F = | (line touch left of char space)
#      \u2595 = | (line touch right of char space)
#      \u2594 = - (line touch top of char space)
    for i in range(6):
        if i == 1:
            print('\u2595                C  R  A  P  S    B  E  T  S                \u258F',end='')
        if i == 3:
            print('\u2595     THREE    ',end='')
            print('\u2595     ELEVEN   ',end='')
            print('\u2595  SNAKE EYES  ',end='')
            print('\u2595   MIDNIGHT   \u258F',end='')
        if i == 4:
            print('\u2595     \u2680 \u2681      ',end='')
            print('\u2595     \u2684 \u2685      ',end='')
            print('\u2595     \u2680 \u2680      ',end='')
            print('\u2595     \u2685 \u2685      \u258F',end='')
        for j in range(61):
            if i == 0:
                if j > 0 and j < 60:
                    print('\u2582',end='')
                else:
                    print(' ',end='')
            if i == 2:
                if j > 0 and j < 60:
                    print('\u2582',end='')
                elif j == 0:
                    print('\u2595',end='')
                else:
                    print('\u258F',end='')
            if i == 5:
                if j > 0 and j < 60:
                    print('\u2594',end='')
                else:
                    print(' ',end='')
        print()    

def drawPassLine(bankroll, passBet):
    if passBet == 0:
        #print(' DON\'T PASS: ')
        print('  PASS LINE: \n')
    else:    
        #print(' DON\'T PASS: ')
        print(' PASS LINE:  $',passBet,sep='')
    print(' BANKROLL: $',bankroll,sep='')

def print_dice_roll(dice):
    print('\n\n')
    for i in range(2):
        if dice[i] == 1:
            print(' \u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print(' \u2595      \u25CF       \u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print('  \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
            
        elif dice[i] == 2:
            print(' \u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print(' \u2595          \u25CF   \u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print(' \u2595  \u25CF           \u258F')
            print(' \u2595              \u258F')
            print('  \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')

        elif dice[i] == 3:
            print(' \u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print(' \u2595          \u25CF   \u258F')
            print(' \u2595              \u258F')
            print(' \u2595      \u25CF       \u258F')
            print(' \u2595              \u258F')
            print(' \u2595  \u25CF           \u258F')
            print(' \u2595              \u258F')
            print('  \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
        elif dice[i] == 4:
            print(' \u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print(' \u2595              \u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print('  \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
        elif dice[i] == 5:
            print(' \u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print(' \u2595      \u25CF       \u258F')
            print(' \u2595              \u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print('  \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
        else:
            print(' \u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print(' \u2595  \u25CF       \u25CF   \u258F')
            print(' \u2595              \u258F')
            print('  \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')

if __name__ == "__main__":
    main()