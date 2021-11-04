import random
from random import randrange

money = 100


def flipping(bet, choice):
    if(bet > money):
        return 0
    result = (random.choice(["Heads", "Tails"]))
    if( choice == result):
        return bet
    else:
       return -bet

def cho_han(bet, choice):
    if bet > money:
        return 0
    first_dice = randrange(1,7)
    second_dice = randrange(1,7)
    sum = first_dice + second_dice
    if(sum%2 == 0):
        if(choice == 'even'):
            return bet
        else:
            return -bet
    else:
        if(choice == 'odd'):
            return bet
        else:
            return -bet

def card_game(bet):
    if bet > money:
        return 0
    player_turn = randrange(1,14)
    computer_turn = randrange(1,14)
    if(player_turn > computer_turn):
        return bet
    elif(player_turn < computer_turn):
        return -bet
    else:
        return bet


def roulette(bet, guess):
    if bet > money:
        return 0
    roulette_number = randrange(1,37)
    if(type(guess) == str):
        if(guess == "Even"):
            if(roulette_number%2==0):
                return bet
            else:
                return -bet
        else:
            if(roulette_number%2 == 1):
                return bet
            else:
                return -bet
    else:
        if(guess == roulette_number):
            return 35*bet
        else:
            return -bet
    



money += (flipping(10, 'Heads'))
money += (cho_han(5, 'even'))
money += (roulette(10, 10))