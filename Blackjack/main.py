import random
import art

def sum_cards(cards):
    if sum(cards)==21 and len(cards)==2:
        return 21
    elif 11 in cards and sum(cards)<21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

gameOn=True
while gameOn:
    play_game=input("Do you want to play blackjack cards? 'y' to play and 'n' to exit: ").lower()
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if play_game!='y':
        gameOn=False
        print("Exited")
    elif play_game=='y':
        print(art.logo)

        user_cards=[]
        comp_cards=[]
        for i in range(0,2):
            user_cards.append(random.choice(cards))
            comp_cards.append(random.choice(cards))

        user_sum=sum(user_cards)
        comp_sum=sum(comp_cards)

        print(f"Your Cards: {user_cards}, Your score: {user_sum}\n"
            f"Computer's cards: {comp_cards[0]}, Computer scores: {comp_sum}")

        if user_sum==21 and comp_sum!=21:
            print("You Win!")
            continue
        elif comp_sum==21 or user_sum>21:
            print("You Lose!!")
            continue
        elif user_sum>21 and comp_sum>21:
            print("BUST!!!!!!!!")


        continuation=input("Type 'y' to draw another card or 'n' to exit: ").lower()

        winner=False

        while continuation=='y':
            user_cards.append(random.choice(cards))
            print(f"Your Cards: {user_cards}, Your score: {sum(user_cards)}\n"
                f"Computer's cards: {comp_cards[0]}, Computer scores: {sum(comp_cards)}")
            user_sum = sum(user_cards)
            if user_sum>21:
                print("You Lose!!!!!")
                winner=True
                break
            continuation = input("Type 'y' to draw another card or 'n' to exit: ").lower()
        if winner:
            continue
        while comp_sum<17:
            comp_cards.append(random.choice(cards))
            comp_sum = sum(comp_cards)

        print(f"Your score: {user_sum}\nComputer scores: {comp_sum}")

        if comp_sum<21:
            if user_sum>comp_sum:
                print("You Win!")
            elif comp_sum>user_sum:
                print("You Lose")
            elif user_sum==comp_sum:
                print("Draw")
        elif comp_sum==21:
            print("You lose!!")
        elif comp_sum>21:
            print("You win")
        else:
            print("You Lose!")