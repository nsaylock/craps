
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
    playerQuit = False
    gameOn = False
    roundWon = False

    print(' Welcome to NS Casino Craps Table!')
    print(' You have $500 to make it big or lose it all')
    print(' The minimum bet is $25. Maximum is $2000. Bet $0 to exit.')
    print(' Place your bet on the pass line')
    print('\n\n\n')
    draw_initial_craps_table()
    
    print('\n\n Bankroll: $', bankroll, sep='')
    while bankroll > 0 and playerQuit == False:     # PASS LINE BET --------------

        while passBet < minBet or passBet > maxBet:
            try:
                passBet = int(input(' PASS LINE: $'))
                if passBet == 0:
                    playerQuit = True
                    break
                elif passBet < minBet:
                    print(' The minimum bet is $',minBet,sep='')
                elif passBet > maxBet:
                    print(' The maximum bet is $',maxBet,sep='')
                elif passBet > bankroll:
                    print(' You only have $',bankroll,'to bet')
                    passBet = 0
                else:
                    bankroll -= passBet
            except ValueError:
                print(' Invalid Input: Enter a Number')

        if playerQuit:
            print(' Player Quit')
            break    
                        # END SET PASS LINE BET #
        
        #############  Come out roll #####################################3
        if roundWon == False:
            placeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0} # Reset place bets

        sum = 7   
        target = 0  
        print()
        while gameOn == False and bankroll >= 0:
            bb = input(' Press Enter to Roll')
            if bb == 'quit': #Make way to quit -- delete later
                playerQuit = True
                break
            dice = dice_roll()
            sum = dice[2]
            if bankroll < minBet or sum < 4 or sum == 12 or sum == 7 or sum == 11:
                draw_craps_table(target, placeBet)
                print_dice_roll(dice)

            if bankroll < minBet:
                print(' You don\'t have enough money left')
                playerQuit = True
            elif sum < 4 or sum == 12:
                draw_pass_line(bankroll, passBet)
                print(' Craps! You lost $',passBet,sep='')
                print(' BANKROLL: $', bankroll, sep='',end='\n')
                passBet = 0
                break
            elif sum == 7:
                bankroll += passBet
                draw_pass_line(bankroll, passBet)
                print(' Lucky Seven! You won $',passBet,sep='')
                print(' BANKROLL: $', bankroll, sep='', end='\n')
            elif sum == 11:
                bankroll += passBet
                draw_pass_line(bankroll, passBet)
                print(' YO ELEVEN! You won $',passBet,sep='')
                print(' BANKROLL: $', bankroll, sep='', end='\n')
            else:
                target = sum
                gameOn = True
                draw_craps_table(target, placeBet)
                print_dice_roll(dice)
                draw_pass_line(bankroll, passBet)
                print(' GAME ON - Point Established on <<', target, '>> - Place additional bets now',sep='')

        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Place Bets 4 and 10 ------ 9:5
        # Place Bets 5 and 9 ------- 7:5
        # Place Bets 6 and 8 ------- 7:6
        # Pass Line Odds 4 and 10 -- 2:1
        # Pass Line Odds 5 and 9 --- 3:2
        # Pass Line Odds 6 and 8 --- 7:5
        # Hardways ----- 6 and 8 --- 9:1
        # Hardwasy ----- 4 and 10 -- 7:1
        # One Roll ----- 3 and 11 -- 15:1
        # One Roll ----- 2 and 12 -- 30:1

        ################## GAME ON - Point Established#########################################

        while gameOn == True:
            selection = selection_prompt()
            if selection == 'quit':
                gameOn = False
                playerQuit = True
                print(' Player Left the Table . . . . . . . . . . ')
                break

            while selection == 'pb': # PLACE BET Section
                try:
                    number = int(input(' What Number for Place Bet? (0 when done): '))
                    if number == 0:
                        selection = 'donotequalthis' # Change selection to exit while loop
                        draw_craps_table(target, placeBet)
                        print_dice_roll(dice)
                        draw_pass_line(bankroll, passBet)
                        break
                    elif (number == 4 or number == 5 or number == 6 or number == 8 or 
                    number == 9  or number == 10):

                        while selection == 'pb':
                            try:
                                amount = int(input(' Bet Amount: $'))
                                if amount < minBet:
                                    print(' Min Bet is $25')
                                elif placeBet[number] != 0:
                                        print(' ', number, ' already has place bet')
                            # ------- Valid Place Bets ---------------------------------------------
                                elif number == 4 or number == 10:
                                    if amount % 5 != 0:
                                        print(' Payout is 9:5. Must be denomination of 5')
                                    else:
                                        placeBet[number] = amount
                                        bankroll -= amount
                                        break
                                elif number == 5 or number == 9:
                                    if amount % 5 != 0:
                                        print(' Payout is 7:5. Must be denomination of 5')
                                    else:
                                        placeBet[number] = amount
                                        bankroll -= amount
                                        break
                                elif number == 6 or number == 8:
                                    if amount % 6 != 0:
                                        print(' Payout is 7:6. Must be denomination of 6')
                                    else:
                                        placeBet[number] = amount
                                        bankroll -= amount
                                        break
                            # ^^^^^^^^^^ Valid Place Bets ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            except ValueError:
                                print(' Invalid Input: Enter a Dollar Amount')

                    else:
                        print(' Selected number is not on board')
                except ValueError:
                    print(' Invalid Input: Enter a Number 4, 5, 6, 8, 9, or 10')
                draw_craps_table(target, placeBet)
                print_dice_roll(dice)
                draw_pass_line(bankroll, passBet)
            # Hardways Bet Tree Goes Here
            # One Roll Bet Tree Goes Here

            ############# GAME ON ROLLS ##################################################
            if selection != 'donotequalthis':
                dice = dice_roll()
                sum = dice[2]
                win = 1

                if sum != 7:
                    draw_craps_table(target, placeBet)
                    print_dice_roll(dice)

                if sum == 2:
                    draw_pass_line(bankroll, passBet)
                    print(' Snake Eyes')
                    win = 0
                elif sum == 3:
                    draw_pass_line(bankroll, passBet)
                    print(' Craps Three')
                    win = 0
                elif sum == 4:
                    print(' Four')
                    if placeBet[4] != 0:
                        win = int(placeBet[4]*9/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet)
                        print(' Place Bet won $',win,sep='')
                        win = 0
                elif sum == 5:
                    print(' Five')
                    if placeBet[5] != 0:
                        win = int(placeBet[5]*7/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet)
                        print(' Place Bet Won $',win,sep='')
                        win = 0
                elif sum == 6:
                    print(' Six')
                    if placeBet[6] != 0:
                        win = int(placeBet[6]*7/6)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet)
                        print(' Place Bet Won $',win,sep='')
                        win = 0
                elif sum == 7:
                    passBet = 0
                    target = 0
                    placeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}
                    draw_craps_table(target, placeBet)
                    print_dice_roll(dice)
                    draw_pass_line(bankroll, passBet)
                    print(' Seven Out | All Bets Cleared\n')
                    win = 0
                    gameOn = False
                    roundWon = False
                elif sum == 8:
                    print(' Eight')
                    if placeBet[8] != 0:
                        win = int(placeBet[6]*7/6)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet)
                        print(' Place Bet Won $',win,sep='')
                        win = 0
                elif sum == 9:
                    print(' Nine')
                    if placeBet[9] != 0:
                        win = int(placeBet[5]*7/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet)
                        print(' Place Bet Won $',win,sep='')
                        win = 0
                elif sum == 10:
                    print(' Ten')
                    if placeBet[10] != 0:
                        win = int(placeBet[4]*9/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet)
                        print(' Place Bet Won $',win,sep='')
                        win = 0
                elif sum == 11:
                    draw_pass_line(bankroll, passBet)
                    print(' Yo Eleven')
                    win = 0
                elif sum == 12:
                    draw_pass_line(bankroll, passBet)
                    print(' Midnight')
                    win = 0

                if sum == target:
                    bankroll += passBet
                    print(' Pass Line Won $',passBet, sep='')
                    print(' WINNER!! Hit target number',target, '-- Game goes off\n')
                    draw_pass_line(bankroll, passBet)  # need if statement so this wont print when already printed on winning place bet
                    gameOn = False
                    roundWon = True

                if win != 0:
                    draw_pass_line(bankroll, passBet)

        
#   ^  End Main Game Loop

def selection_prompt():
    print('\n pb - Place Bet |', end='')
    print(' hw - hardways |', end='')
    print(' or - One Roll Bets |',end='')
    print(' quit - Exit game')
    print(' Press Enter to Roll')
    selection = 'badstring'
    while selection != 'pb' and selection != 'hw' and selection != 'or' and selection != '' and selection != 'quit':
        selection = input(' ')
    return selection

def dice_roll():
    dice = []        
    for i in range(2):
        die = random.randint(1, 6)
        dice.append(die)
    dice.append(dice[0] + dice[1])
    return dice

def draw_initial_craps_table():
    draw_place_bets()
    draw_come_lines()
    draw_field_bets()
    draw_hardways()
    draw_craps_bets()

def draw_craps_table(target, placeBet):
    if target == 0:
        pass
    elif target == 4:
        print('     ON')
    elif target == 5:
        print('              ON')
    elif target == 6:
        print('                        ON')
    elif target == 8:
        print('                                  ON')
    elif target == 9:
        print('                                             ON')
    else:
        print('                                                       ON')
    
    draw_place_bets()
    #placeBet = [4:0, 5:0, 6:30, 8:30, 9:0, 10:0]
    for i, amount in placeBet.items():
        if amount != 0:
            print('    $', amount,sep='', end='   ')
        else:
            print('          ',end='')

    '''
    if placeBet[4] != 0:
        print('       $', placeBet[4],sep='', end='')
    else:
        print('         ',end='')
    if placeBet[5] != 0:
        print('       $', placeBet[5], end='')
    else:
        print('         ',end='')
    if placeBet[6] != 0:
        print('       $', placeBet[6], end='')
    else:
        print('        ', end='')
    if placeBet[8] != 0:
        print('       $', placeBet[8], end='')
    else:
        print('         ', end='')
    if placeBet[9] != 0:
        print('       $', placeBet[9], end='')
    else:
        print('         ', end='')
    if placeBet[10] != 0:
        print('       $', placeBet[10], end='')
    else:
        print('         ', end='')
    '''
    print()
    draw_come_lines()
    draw_field_bets()
    draw_hardways()
    draw_craps_bets()
    

def draw_place_bets():        # Place bets ---------------------------    
    place_bet_hor_line("\u2582")
    placeBetVertLine()
    print(" \u258F   4   \u2595",end=" ")
    print("\u258F   5   \u2595",end=" ")
    print("\u258F   6   \u2595",end=" ")
    print("\u258F   8   \u2595",end=" ")
    print("\u258F   9   \u2595",end=" ")
    print("\u258F  10   \u2595",end="")
    print()   
    placeBetVertLine()
    place_bet_hor_line("\u2594")

def placeBetVertLine():
    for i in range(6): # Range must be same as length of top lines
        if i == 0:
            print(' ',end='')
        print("\u258F       \u2595 ", end="")
    print()

def place_bet_hor_line(line):
    for i in range(6):
        if i == 0:
            print(' ',end='')
        for i in range(9): # range is length of bottom lines (same as top)
            print(line,end="")
        print(" ",end="")
    print()
##################### END Place BETS ##############################

def draw_come_lines():
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

def draw_field_bets():
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
    
def draw_hardways():
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

def draw_craps_bets():
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

def draw_pass_line(bankroll, passBet):
    #print(' DON\'T PASS: ')
    print(' PASS LINE: $',passBet,sep='')
    print(' BANKROLL: $',bankroll,sep='')
    print()

def print_dice_roll(dice):
    for i in range(2):
        if dice[i] == 1:
            print('\u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print('\u2595      \u25CF       \u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print(' \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
            
        elif dice[i] == 2:
            print('\u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print('\u2595          \u25CF   \u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print('\u2595  \u25CF           \u258F')
            print('\u2595              \u258F')
            print(' \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')

        elif dice[i] == 3:
            print('\u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print('\u2595          \u25CF   \u258F')
            print('\u2595              \u258F')
            print('\u2595      \u25CF       \u258F')
            print('\u2595              \u258F')
            print('\u2595  \u25CF           \u258F')
            print('\u2595              \u258F')
            print(' \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
        elif dice[i] == 4:
            print('\u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print('\u2595              \u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print(' \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
        elif dice[i] == 5:
            print('\u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print('\u2595      \u25CF       \u258F')
            print('\u2595              \u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print(' \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')
        else:
            print('\u2595\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print('\u2595  \u25CF       \u25CF   \u258F')
            print('\u2595              \u258F')
            print(' \u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594\u2594')

if __name__ == "__main__":
    main()