# 0925-2025 Blackjack Game
import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computerHand=[]
userHand=[]
gameOver=False
openingQuestion="Do you want to play a game of Blackjack? Type 'y' or 'n': "
anotherCardQuestion="Type 'y' to get another card, type 'n' to pass:"
#Value for testing
blackjackHand=[11,10]

def nextCard():
    i=random.randint(0,len(cards)-1)
    card=(cards[i])
    return card


def initialDeal():
    computerHand.clear()
    computerHand.append(nextCard())
    computerHand.append(nextCard())
    userHand.clear()
    userHand.append(nextCard())
    userHand.append(nextCard())

def detectblackjack(hand):
    if len(hand)==2 and 11 in hand and 10 in hand:
        return True
    else:
        return False

def determinescore(hand):
    total=sum(hand)
    if total > 21 and 11 in hand:
        total-=10
    return total

answer='y'
while answer == 'y':
    gameOver= False
    answer=input(openingQuestion).lower()

    #Deal both user and computer a starting hand of 2 random card values.
    print("\n" * 20)
    print(art.logo)
    initialDeal()
    #Output starting hand

    print(f"Your cards:{userHand}, current score:: {determinescore(userHand)}")
    #print(f"Computer's first card: {dealerHand[0]}")
    #test print(f"Dealer:{dealerHand} which is: {determinescore(dealerHand)}")

    #test userHand.append(11)
    #test print(f"You:{userHand} which is: {determinescore(userHand)}")

    #Evaluate initial deal
    if (detectblackjack(computerHand))== True:
        dealerWon= f"Computer has won {computerHand} you:{userHand}"
        print(dealerWon)
        gameOver=True
    elif(detectblackjack(userHand)) == True:
        userWon= f"You have won you:{userHand} Computer: {computerHand}"
        print(userWon)
        gameOver=True


    anotherCard = 'y'
    while not gameOver and anotherCard == 'y':
        print(f"Computer's first card: {computerHand[0]}")
        anotherCard= input(anotherCardQuestion).lower()
        if anotherCard == 'y':
            userHand.append(nextCard())
            print(userHand)
            print(determinescore(userHand))
            if determinescore(userHand) > 21:
                print(f"Your final hand: {userHand}, final score: {determinescore(userHand)} \nComputer's final hand: {computerHand}, final score: {determinescore(computerHand)} \nYou lose")
                gameOver = True

    while not gameOver:
        dealerContinue=True
        while dealerContinue:
            if (determinescore(computerHand)) <= 16:
                computerHand.append(nextCard())
            else:
                if determinescore(computerHand) > 21:
                    print(f"Your final hand: {userHand}, final score: {determinescore(userHand)} \nComputer's final hand: {computerHand}, final score: {determinescore(computerHand)} \nYou win")
                    dealerContinue=False
                    gameOver = True
                elif determinescore(userHand) > determinescore(computerHand):
                    print(f"Your final hand: {userHand}, final score: {determinescore(userHand)} \nComputer's final hand: {computerHand}, final score: {determinescore(computerHand)} \nYou win")
                    dealerContinue = False
                    gameOver = True
                elif determinescore(userHand) == determinescore(computerHand):
                    print( f"Your final hand: {userHand}, final score: {determinescore(userHand)} \nComputer's final hand: {computerHand}, final score: {determinescore(computerHand)} \nYou tie!")
                    dealerContinue = False
                    gameOver = True
                else:
                    print(f"Your final hand: {userHand}, final score: {determinescore(userHand)} \nComputer's final hand: {computerHand}, final score: {determinescore(computerHand)} \nYou lose")
                    dealerContinue=False
                    gameOver = True

#0926-2025
# need to put debug information in play
# seems iterate well need to reveiw with the requirements and solution
# ALSO
  #ToDo After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
    # https://listmoz.com/view/6h34DJpvJBFVRlZfJvxF







