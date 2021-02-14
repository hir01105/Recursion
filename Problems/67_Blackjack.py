def winnerBlackjack(playerCards, houseCards):
    playerScore = 0
    dealerScore = 0
    letters = ["A", "J", "Q", "K"]
    for card in playerCards:
        if card[1:] in letters:
            if card[1:] == "A":
                num = 1
            elif card[1:] == "J":
                num = 11
            elif card[1:] == "Q":
                num = 12
            else:
                num = 13
            playerScore += num
        else:
            playerScore += int(card[1:])

    for card in houseCards:
        if card[1:] in letters:
            if card[1:] == "A":
                num = 1
            elif card[1:] == "J":
                num = 11
            elif card[1:] == "Q":
                num = 12
            else:
                num = 13
            dealerScore += num
        else:
            dealerScore += int(card[1:])

    if playerScore > 21:
        return False
    elif dealerScore < 22 and dealerScore > playerScore:
        return False
    elif dealerScore < playerScore or dealerScore > 21:
        return True
    else:
        return False
    

print(winnerBlackjack(["♣4","♥7","♥7"],["♠Q","♣J"]))