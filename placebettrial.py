class Bet:
    pass

if __name__ == "__main__":
    placeBet = {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}
    placeBet[4] = 25
    placeBet[10] = 325
    

    for number, amount in placeBet.items():
        print(number, amount)
