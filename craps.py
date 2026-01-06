
"""
Filename: craps.py
Author: Nick Saylock
Date: 2025-12-23
Version 1.0
"""
import random
# To DO next: 
# Make a way to have place bet go behind the line ---- Will display for now, need way to calculate winning this bet
# Let player overwrite place bet without getting stuck in loop
# Let player pull back place bets
# Let Player buy 4 and 10 bets

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
    passOdds = 0
    bankroll = 500
    minBet = 25
    maxBet = 2000
    playerQuit = False
    gameOn = False
    roundWon = False
    passOddsPlayed = False

    print(' Welcome to NS Casino Craps Table!')
    print(' You have $500 to make it big or lose it all')
    print(' The minimum bet is $25. Maximum is $2000. Bet $0 to exit.')
    print(' Place your bet on the pass line')
    print('\n\n\n')
    draw_initial_craps_table()
    
    print(' Starting Bankroll: $', bankroll, sep='',end='\n\n')
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
            print(' BANKROLL: $',bankroll,sep='')
        if playerQuit:
            print(' Player Quit')
            break    
                        # END SET PASS LINE BET #
        
        #############  Come out roll #####################################3
        if roundWon == False:                                   # Initial is false, assign true when dice sum = target, assign false when sum = 7
            placeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}          # Initialize/Reset place bets in Dictionary

        #sum = 7         # Initial value allows
        target = 0         # Initial Value to get passed into function before assigned a useful number
        print()
        while gameOn == False and bankroll >= 0:
            bb = input(' Press Enter to Roll')
            if bb == 'quit': #Make way to quit -- delete later -- delete later -- delete later -- delete later -- delete later --
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
                draw_pass_line(bankroll, passBet, passOdds)
                print(' Craps! You lost $',passBet, ' from the Pass Line\n',sep='')
                passBet = 0
                break
            elif sum == 7:
                bankroll += passBet
                draw_pass_line(bankroll, passBet, passOdds)
                print(' Lucky Seven! You won $',passBet,sep='')
                print(' BANKROLL: $', bankroll, sep='', end='\n')
            elif sum == 11:
                bankroll += passBet
                draw_pass_line(bankroll, passBet, passOdds)
                print(' YO ELEVEN! You won $',passBet,sep='')
                print(' BANKROLL: $', bankroll, sep='', end='\n')
            else:
                target = sum
                gameOn = True
                draw_craps_table(target, placeBet)
                print_dice_roll(dice)
                print('    <<',target,'>>\n')
                draw_pass_line(bankroll, passBet, passOdds)
                print(' GAME ON | Point Established on ', target, '. Place additional bets now',sep='')

        #^^^^^^^^^^^^^^^^^^^^ END COME OUT ROLL ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

        ################## GAME ON - << Point Established >> #########################################

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
                        selection = 'gobacktoselectionmenu' # Change selection to exit while loop
                        draw_craps_table(target, placeBet)
                        #print_dice_roll(dice)
                        draw_pass_line(bankroll, passBet, passOdds)
                        break
                    elif number == target:
                        passOddsPlayed = True
                        print('Place bets on point target will be placed behind the pass line for better payout')
                        while selection == 'pb':
                            try:
                                passOdds = int(input(' Pass Line Odds Bet Amount $'))
                                if passOdds < minBet:
                                    print(' Min Bet is $', minBet, sep='')
                                elif passOdds > maxBet:
                                    print(' Max Bet is $', maxBet, sep='')
                                elif number == 4 or number == 10:
                                    # Pay is 2:1 any amount over minBet and less than maxBet should be good to go
                                    bankroll -= passOdds
                                    break
                                elif number == 5 or number == 9:
                                    if passOdds % 2 != 0:
                                        print(' Payout is 3:2. Must be divisible by 2')
                                    else:
                                        bankroll -= passOdds
                                        break
                                elif number == 6 or number == 8:
                                    if passOdds % 5 != 0:
                                        print(' Payout is 7:5. Must be divisible by 5')
                                    else:
                                        bankroll -= passOdds
                                        break
                            except ValueError:
                                print(' Invalid Input: Enter a dollar amount using numbers')
                    elif (number == 4 or number == 5 or number == 6 or number == 8 or 
                    number == 9  or number == 10):

                        while selection == 'pb':
                            try:
                                amount = int(input(' Bet Amount: $'))           # amount as variable name may be arbitrary
                                if amount < minBet:
                                    print(' Min Bet is $', minBet, sep='')
                                elif amount > maxBet:
                                    print(' Max Bet is $', maxBet, sep='')
                                elif placeBet[number] != 0:
                                        print(' ', number, ' already has place bet') ## ERROR ERROR ERROR ERROR ERROR WILL GET STUCK IN LOOP
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
                #print_dice_roll(dice)
                draw_pass_line(bankroll, passBet, passOdds)
            # Hardways Bet Tree Goes Here
            # One Roll Bet Tree Goes Here

            ############# GAME ON ROLLS - SCORING SECTION ##################################################
            if selection != 'gobacktoselectionmenu':   # Skips this section when player finishes setting place bets but not ready to roll
                dice = dice_roll()                     # Will be (selection = '') when player presses enter to roll
                sum = dice[2]
                control = True  # Trying to control where the draw_pass_line appears at the bottom of this decision tree

                if sum != 7:
                    draw_craps_table(target, placeBet)
                    print_dice_roll(dice)

                if sum == 2:
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Snake Eyes')
                    control = False
                elif sum == 3:
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Craps Three')
                    control = False
                elif sum == 4:
                    print(' Four')
                    if placeBet[4] != 0:
                        win = int(placeBet[4]*9/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet, passOdds)
                        print(' Place Bet won $',win,sep='')
                        control = False
                elif sum == 5:
                    print(' Five')
                    if placeBet[5] != 0:
                        win = int(placeBet[5]*7/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet, passOdds)
                        print(' Place Bet Won $',win,sep='')
                        control = False
                elif sum == 6:
                    print(' Six')
                    if placeBet[6] != 0:
                        win = int(placeBet[6]*7/6)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet, passOdds)
                        print(' Place Bet Won $',win,sep='')
                        control = False
                elif sum == 7:
                    passBet = 0
                    passOdds = 0
                    passOddsPlayed = False
                    target = 0
                    placeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}
                    print(' Seven Out | All Bets Cleared\n')
                    draw_craps_table(target, placeBet)
                    print_dice_roll(dice)
                    draw_pass_line(bankroll, passBet, passOdds)
                    control = False
                    gameOn = False
                    roundWon = False
                elif sum == 8:
                    print(' Eight')
                    if placeBet[8] != 0:
                        win = int(placeBet[6]*7/6)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet, passOdds)
                        print(' Place Bet Won $',win,sep='')
                        control = False
                elif sum == 9:
                    print(' Nine')
                    if placeBet[9] != 0:
                        win = int(placeBet[5]*7/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet, passOdds)
                        print(' Place Bet Won $',win,sep='')
                        control = False
                elif sum == 10:
                    print(' Ten')
                    if placeBet[10] != 0:
                        win = int(placeBet[4]*9/5)
                        bankroll += win
                        if sum != target:
                            draw_pass_line(bankroll, passBet, passOdds)
                        print(' Place Bet Won $',win,sep='')
                        control = False
                elif sum == 11:
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Yo Eleven')
                    control = False
                elif sum == 12:
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Midnight')
                    control = False

                if sum == target:
                    bankroll += passBet
                    print(' Pass Line Won $',passBet, sep='')
                    if passOddsPlayed == True:
                        if target == 4 or target == 10:
                            win = int(passOdds*2)
                        elif target == 5 or target == 9:
                            win = int(passOdds*3/2)
                        elif target == 6 or target == 8:
                            win = int(passOdds*7/5)
                        bankroll += win
                        print(' Pass Odds Wins $', win, sep='')
                    print(' WINNER!! Hit target number',target, '-- Game goes off\n')
                    passOdds = 0
                    #draw_pass_line(bankroll, passBet, passOdds)  # need if statement so this wont print when already printed on winning place bet
                    # Probably could permanently delete ^^^
                    gameOn = False
                    roundWon = True

                if control != False:
                    draw_pass_line(bankroll, passBet, passOdds)

        
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

def draw_pass_line(bankroll, passBet, passOdds):
    #print(' DON\'T PASS: ')
    print(' PASS LINE: $',passBet,sep='')
    if passOdds != 0:
        print(' PASS LINE ODDS: $', passOdds, sep='')
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