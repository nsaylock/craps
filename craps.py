
"""
Filename: craps.py
Author: Nick Saylock
Date: 2025-12-23
Version 1.0
"""
import random
# To DO next: 
# Place bet does not move behind the pass line when new target established after winning round
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
    comeBetAmount = 0
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
    draw_initial_craps_table(comeBetAmount)
    
    print(' Starting Bankroll: $', bankroll, sep='',end='\n\n')
    while bankroll > minBet and playerQuit == False:     # PASS LINE BET --------------

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
                elif bankroll < minBet:
                    print(' You don\'t have the min bet')
                    playerQuit = True
                    break
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
            hardWays = {4:0, 10:0, 6:0, 8:0}
            oneRollBet = {3:0, 11:0, 2:0, 12:0}
            comeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}

        #sum = 7         # Initial value allows
        target = 0         # Initial Value to get passed into function before assigned a useful number
        fieldBet = 0
        print()
        while gameOn == False and bankroll >= 0:
            bb = input(' Press Enter to Roll')
            print()
            if bb == 'quit': #Make way to quit -- delete later -- delete later -- delete later -- delete later -- delete later --
                playerQuit = True
                break
            dice = dice_roll()
            sum = dice[2]
            if bankroll < minBet or sum < 4 or sum == 12 or sum == 7 or sum == 11:
                draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                draw_dice_roll(dice)

            
            if sum < 4 or sum == 12:
                draw_pass_line(bankroll, passBet, passOdds)
                print(' Craps! You lost $',passBet, ' from the Pass Line\n',sep='')
                passBet = 0
                break
            elif sum == 7:
                bankroll += passBet
                draw_pass_line(bankroll, passBet, passOdds)
                print(' Lucky Seven! You won $',passBet,sep='')
                print()
            elif sum == 11:
                bankroll += passBet
                draw_pass_line(bankroll, passBet, passOdds)
                print(' YO ELEVEN! You won $',passBet,sep='')
                print()
            else:
                target = sum
                gameOn = True
                draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                draw_dice_roll(dice)
                print('    <<',target,'>>')
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
                        draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                        #draw_dice_roll(dice)
                        draw_pass_line(bankroll, passBet, passOdds)
                        break
                    elif number == target:
                        passOddsPlayed = True
                        print(' Placing Bet behind the pass line\n')
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
                        if placeBet[number] != 0:
                            print(' ', number, ' already has place bet', end=' ')
                            replaceBet = input('Do you wish to pull back? (y/n) :')
                            if replaceBet == 'y': # Need to make sure input can only be y/n
                                bankroll += placeBet[number]
                                placeBet[number] = 0
                            break
                        while selection == 'pb':
                            try:
                                amount = int(input(' Bet Amount: $'))           # amount as variable name may be arbitrary
                                if amount < minBet:
                                    print(' Min Bet is $', minBet, sep='')
                                elif amount > maxBet:
                                    print(' Max Bet is $', maxBet, sep='')
                                
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
                draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)
                draw_pass_line(bankroll, passBet, passOdds)

            # HARDWAYS HARDWAYS HARDWAYS HARDWAYS HARDWAYS HARDWAYS HARDWAYS HARDWAYS HARDWAYS
            while selection == 'hw':
                try:
                    hardNumber = int(input(' Which Number for Hard Ways Bet? (0 When Done): '))
                    if hardNumber == 0:
                        selection = 'gobacktoselectionmenu'
                        draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                        draw_pass_line(bankroll, passBet, passOdds)
                        break
                    elif hardNumber == 4 or hardNumber == 6 or hardNumber == 8 or hardNumber == 10:
                        while selection == 'hw':
                            try:
                                amount = int(input(' Enter amount $'))
                                if amount > bankroll:
                                    print(' You don\'t have that much money try again')
                                elif amount == 0:
                                    print(' Betting Canceled')
                                    break
                                elif amount < 0:
                                    print(' Negative bets are not accepted here. Try again')
                                elif amount > maxBet:
                                    print(' Max bet is $2000. Try again')
                                else:
                                    hardWays[hardNumber] = amount
                                    bankroll -= amount
                                    break
                            except ValueError:
                                print(' Invalid Input: Enter a Dollar amount')
                    else:
                        print(' The only hard numbers are 4, 6, 8, and 10')
                except ValueError:
                    print(' Invalid Input: Enter an Integer')

                draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                draw_pass_line(bankroll, passBet, passOdds)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # Come and Don't come Tree Goes Here
            while selection == 'come':
                try:
                    comeBetAmount = int(input(' Enter Amount for Come Bet (0 to Cancel): $'))
                    if comeBetAmount == 0:
                        selection = 'gobacktoselectionmenu'
                        draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)
                        draw_pass_line(bankroll, passBet, passOdds)
                        print(' Come Bet Canceled')
                        break
                    elif comeBetAmount > bankroll:
                        print(' You don\'t have that much money try again')
                    elif comeBetAmount < 0:
                        print(' Negative bets are not accepted here. Try again')
                    elif comeBetAmount > maxBet:
                        print(' Max bet is $2000. Try again')
                    else:
                        bankroll -= comeBetAmount
                        draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)
                        draw_pass_line(bankroll, passBet, passOdds)
                        selection = 'gobacktoselectionmenu'
                        break
                except ValueError:
                    print(' Invalid Input: Enter a Dollar Amount')
            #### FIELD BET ### #### #### ### #### ### ### ### ### ### FIELD BET
            while selection == 'fb':
                try:
                    amount = int(input(' Enter Amount for Field Bet (0 to Cancel): $'))
                    if amount == 0:
                        selection = 'gobacktoselectionmenu'
                        draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)
                        draw_pass_line(bankroll, passBet, passOdds)
                        print(' Field Bet Canceled')
                        break
                    elif amount > bankroll:
                        print(' You don\'t have that much money try again')
                    elif amount < 0:
                        print(' Negative bets are not accepted here. Try again')
                    elif amount > maxBet:
                        print(' Max bet is $2000. Try again')
                    else:
                        fieldBet = amount
                        bankroll -= amount
                        break
                except ValueError:
                    print(' Invalid Input: Enter a Dollar Amount')
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            # One Roll Bet Tree Goes Here
            while selection == 'or':
                try:
                    number = int(input(' Which number for One Roll Bet? (0 When Done): '))
                    if number == 0:
                        selection = 'gobacktoselectionmenu'
                        draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                        draw_pass_line(bankroll, passBet, passOdds)
                        break
                    elif number == 3 or number == 11 or number == 2 or number == 12:
                        while selection == 'or':
                            try:
                                amount = int(input(' Enter Amount: $'))
                                if amount > bankroll:
                                    print(' You don\'t have that much money try again')
                                elif amount == 0:
                                    print(' Betting Canceled')
                                    break
                                elif amount < 0:
                                    print(' Negative bets are not accepted here. Try again')
                                elif amount > maxBet:
                                    print(' Max bet is $2000. Try again')
                                else:
                                    oneRollBet[number] = amount
                                    bankroll -= amount
                                    break
                            except ValueError:
                                print(' Invalid Input: Enter Amount in Dollars')
                    else:
                        print(' The only One Roll Bets are 2, 3, 11, and 12')
                except ValueError:
                    print(' Invalid Input: Enter an integer')
                draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                draw_pass_line(bankroll, passBet, passOdds)

            ############# GAME ON ROLLS - SCORING SECTION ##################################################
            if selection != 'gobacktoselectionmenu':   # Skips this section when player finishes setting place bets but not ready to roll
                dice = dice_roll()                     # Will be (selection = '') when player presses enter to roll
                sum = dice[2]
                orWin = 0
                reset_oneRollBet(sum, oneRollBet)

                if sum != 7:
                    draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)
                    draw_dice_roll(dice)

                if sum == 2:
                    if oneRollBet[2] != 0:
                        orWin = int(oneRollBet[2]*30)
                        bankroll += orWin
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Snake Eyes')
                elif sum == 3:
                    if oneRollBet[3] != 0:
                        orWin = int(oneRollBet[3]*15)
                        bankroll += orWin
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Craps Three')
                elif sum == 4:
                    if sum != target:
                        draw_pass_line(bankroll, passBet, passOdds)
                        if dice[0] == dice[1]:
                            print(' Hard Four')
                        else:
                            print(' Four')
                    if placeBet[4] != 0:
                        pbWin = int(placeBet[4]*9/5)
                        bankroll += pbWin
                        if sum != target:
                            print(' Place Bet won $',pbWin,sep='')
                        #control = False
                    if hardWays[4] != 0:
                        if dice[0] == dice[1]:
                            pbWin = int(hardWays[4]*7)
                            bankroll += pbWin
                            print(' Hard 4 Won $', pbWin, sep='')
                        else:
                            hardWays[4] = 0
                            print(' Hard 4 Bet Cleared')
                    if comeBet[4] != 0:
                        bankroll += comeBet[4]*2
                        print(' Come Bet Won $', comeBet[4], '. Initial bet returned to player.', sep='')
                        comeBet[4] = 0
                elif sum == 5:
                    if sum != target:
                        draw_pass_line(bankroll, passBet, passOdds)
                        print(' Five')
                    if placeBet[5] != 0:
                        pbWin = int(placeBet[5]*7/5)
                        bankroll += pbWin
                        if sum != target:
                            print(' Place Bet Won $',pbWin,sep='')
                    if comeBet[5] != 0:
                        bankroll += comeBet[5]*2
                        print(' Come Bet Won $', comeBet[5], '. Initial bet returned to player.', sep='')
                        comeBet[5] = 0
                elif sum == 6:
                    if sum != target:
                        draw_pass_line(bankroll, passBet, passOdds)
                        if dice[0] == dice[1]:
                            print(' Hard Six')
                        else:
                            print(' Six')
                    if placeBet[6] != 0:
                        pbWin = int(placeBet[6]*7/6)
                        bankroll += pbWin
                        if sum != target:
                            print(' Place Bet Won $',pbWin,sep='')
                        #control = False
                    if hardWays[6] != 0:
                        if dice[0] == dice[1]:
                            pbWin = int(hardWays[6]*9)
                            bankroll += pbWin
                            print(' Hard 6 Won $', pbWin, sep='')
                        else:
                            hardWays[6] = 0
                            print(' Hard 6 Bet Cleared')
                    if comeBet[6] != 0:
                        bankroll += comeBet[6]*2
                        print(' Come Bet Won $', comeBet[6], '. Initial bet returned to player.', sep='')
                        comeBet[6] = 0
                elif sum == 7:
                    passBet = 0
                    passOdds = 0
                    passOddsPlayed = False
                    hardWaysPlayed = False
                    target = 0
                    placeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}
                    hardWays = {4:0, 10:0, 6:0, 8:0}
                    oneRollBet = {3:0, 11:0, 2:0, 12:0}
                    comeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}
                    draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                    draw_dice_roll(dice)
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Seven Out | All Bets Cleared\n')
                    gameOn = False
                    roundWon = False
                elif sum == 8:
                    if sum != target:
                        draw_pass_line(bankroll, passBet, passOdds)
                        if dice[0] == dice[1]:
                            print(' Hard Eight')
                        else:
                            print(' Eight')
                    if placeBet[8] != 0:
                        pbWin = int(placeBet[8]*7/6)
                        bankroll += pbWin
                        if sum != target:
                            print(' Place Bet Won $',pbWin,sep='')
                    if hardWays[8] != 0:
                        if dice[0] == dice[1]:
                            pbWin = int(hardWays[8]*9)
                            bankroll += pbWin
                            print(' Hard 8 Won $', pbWin, sep='')
                        else:
                            hardWays[8] = 0
                            print(' Hard 8 Bet Cleared')
                    if comeBet[8] != 0:
                        bankroll += comeBet[8]*2
                        print(' Come Bet Won $', comeBet[8], '. Initial bet returned to player.', sep='')
                        comeBet[8] = 0
                elif sum == 9:
                    if sum != target:
                        draw_pass_line(bankroll, passBet, passOdds)
                        print(' Nine')
                    if placeBet[9] != 0:
                        pbWin = int(placeBet[9]*7/5)
                        bankroll += pbWin
                        if sum != target:
                            print(' Place Bet Won $',pbWin,sep='')
                    if comeBet[9] != 0:
                        bankroll += comeBet[9]*2
                        print(' Come Bet Won $', comeBet[9], '. Initial bet returned to player.', sep='')
                        comeBet[9] = 0
                elif sum == 10:
                    if sum != target:
                        draw_pass_line(bankroll, passBet, passOdds)
                        if dice[0] == dice[1]:
                            print(' Hard Ten')
                        else:
                            print(' Ten')
                    if placeBet[10] != 0:
                        pbWin = int(placeBet[10]*9/5)
                        bankroll += pbWin
                        if sum != target:
                            print(' Place Bet Won $',pbWin,sep='')
                    if hardWays[10] != 0:
                        if dice[0] == dice[1]:
                            pbWin = int(hardWays[10]*7)
                            bankroll += pbWin
                            print(' Hard 10 Won $', pbWin, sep='')
                        else:
                            hardWays[10] = 0
                            print(' Hard 10 Bet Cleared')
                    if comeBet[10] != 0:
                        bankroll += comeBet[10]*2
                        print(' Come Bet Won $', comeBet[10], '. Initial bet returned to player.', sep='')
                        comeBet[10] = 0
                elif sum == 11:
                    if oneRollBet[11] != 0:
                        orWin = int(oneRollBet[11]*15)
                        bankroll += orWin
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Yo Eleven')
                elif sum == 12:
                    if oneRollBet[12] != 0:
                        orWin = int(oneRollBet[12]*30)
                        bankroll += orWin
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' Midnight')

                if sum == target:
                    bankroll += passBet
                    if passOddsPlayed == True:
                        if target == 4 or target == 10:
                            oddsWin = int(passOdds*2)
                        elif target == 5 or target == 9:
                            oddsWin = int(passOdds*3/2)
                        elif target == 6 or target == 8:
                            oddsWin = int(passOdds*7/5)
                        bankroll += oddsWin
                        bankroll += passOdds
                        passOdds = 0
                    draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet)

                    draw_dice_roll(dice)
                    draw_pass_line(bankroll, passBet, passOdds)
                    print(' WINNER!! Hit target number', target, 'Game goes off\n')
                    print(' Pass Line Won $',passBet, sep='')
                    if placeBet[target] != 0:
                        print(' Place Bet Won $', pbWin, sep='')
                    if passOddsPlayed:
                        print(' Pass Odds Wins $', oddsWin, sep='')
                    #draw_pass_line(bankroll, passBet, passOdds)  # need if statement so this wont print when already printed on winning place bet
                    # Probably could permanently delete ^^^
                    gameOn = False
                    passOddsPlayed = False
                    roundWon = True

                if orWin != 0:
                    print(' One Roll Bet Won $', orWin, sep='')

                if fieldBet != 0:
                    if sum == 2 or sum == 3 or sum == 4 or sum == 9 or sum == 10 or sum == 11 or sum == 12:
                        bankroll += fieldBet*2
                        print(' Field Bet Won $', fieldBet, '. Initial Field Bet Returned',sep='')
                    else:
                        print(' Lost $', fieldBet, ' in the field', sep='')
                    fieldBet = 0
                
                if comeBetAmount != 0:
                    if sum < 4 or sum == 12:
                        print(' Come Bet lost. $', comeBetAmount, ' removed from table.', sep='')
                        comeBetAmount = 0
                    elif sum == 7 or sum == 11:
                        bankroll += comeBetAmount
                        print(' Come Bet Won $', comeBetAmount, sep='')
                    else:
                        comeBet[sum] = comeBetAmount
                        print(' Come Bet moved to the ', sum, sep='')
                        comeBetAmount = 0

                #if control != False:
                #    draw_pass_line(bankroll, passBet, passOdds)

        
### ^ End Main Game Loop ##################################################################
###########################################################################################
###########################################################################################
print('\n Player Can no longer make the minimum pass line bet. Exiting Game')

def reset_oneRollBet(sum, oneRollBet):
    if sum != 2:
        oneRollBet[2] = 0
    if sum != 3:
        oneRollBet[3] = 0
    if sum != 11:
        oneRollBet[11] = 0
    if sum != 12:
        oneRollBet[12] = 0

def selection_prompt():
    print('\n pb - Place Bet |', end='')
    print(' hw - Hardways |', end='')
    print(' or - One Roll Bets')
    print(' fb - Field Bet |', end='')
    print(' come - Come Bet |', end='')
    print(' dc - Don\'t Come Bet |')
    print(' quit - Exit game')
    print(' Press Enter to Roll')
    selection = 'badstring'
    while (selection != 'pb' and selection != 'hw' and selection != 'or' and selection != 'fb'
            and selection != 'come' and selection != 'dc'
            and selection != '' and selection != 'quit'):
        selection = input(' ')
    return selection

def dice_roll():
    dice = []        
    for i in range(2):
        die = random.randint(1, 6)
        dice.append(die)
    dice.append(dice[0] + dice[1])
    return dice

def draw_initial_craps_table(comeBetAmount):
    draw_place_bets()
    draw_come_lines(comeBetAmount)
    draw_field_bets()
    draw_hardways()
    draw_one_roll_bets()

def draw_craps_table(target, placeBet, hardWays, oneRollBet, comeBetAmount, comeBet):
    print('\n\n\n')
    for i in range(75):
        print('\u2500', end='')
    print('\n')
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
    for i, amount in placeBet.items():
        if amount != 0:
            print('    $', amount,sep='', end='    ')
        else:
            print('         ',end='')
    print()
    for i, amount in comeBet.items():
        if amount != 0:
            print('    $', amount,sep='', end='    ')
        else:
            print('         ',end='')
    print()
    draw_come_lines(comeBetAmount)
    draw_field_bets()
    draw_hardways()
    for i, amount in hardWays.items():
        if amount != 0:
            print('       $', amount,sep='', end='      ')
        else:
            print('               ',end='')
    print()
    draw_one_roll_bets()
    for i, amount in oneRollBet.items():
        if amount != 0:
            print('       $', amount,sep='', end='      ')
        else:
            print('               ',end='')
    print()
    

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

def draw_come_lines(comeBetAmount):
    for i in range(58): #Top Lines
        if i == 0 or i == 20:
            print(' ',end='')
        print("\u2582",end="")
    print()

    for i in range(2): # Word Lines
        if i == 1:
            print("\u2595     DON\'T COME    \u2595",end='')
            if comeBetAmount == 0:
                print("\u2595                COME                 \u2595",end="")
            else:
                print("\u2595                COME    $", comeBetAmount,"          \u2595",sep='',end="")
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

    for i in range(2):
        if i == 0:
            print("\u2595              2 \u2219 3 \u2219 4 \u2219 9 \u2219 10 \u2219 11 \u2219 12                \u2595")
        if i == 1:
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

def draw_one_roll_bets():
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
            print('\u2595                O N E  R O L L    B  E  T  S               \u258F',end='')
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
    print('\n PASS LINE: $',passBet,sep='')
    if passOdds != 0:
        print(' PASS LINE ODDS: $', passOdds, sep='')
    print(' BANKROLL: $',bankroll,sep='')
    for i in range(75):
        print('\u2500',end='')
    print()

def draw_dice_roll(dice):
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