import random
from art import logo

def compare(sum, comp_sum):      
    #Conditions to check who is the winner
    #Condition 1 : If user score is greater than computer score and less than 21 then user wins
    if sum > comp_sum and sum <= 21:
        return "You win. Yay."
    #Condition 2 : If computer score > user score and computer score is less than 21 then computer wins
    elif comp_sum > sum and comp_sum <= 21:
        return "You lose."
    elif sum == comp_sum:
        return "Draw."
    else:
        return "You lose."

def play_game():

    #Print logo
    print(logo)

    #List of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #Randomly Select a pair of two cards from the list of cards
    user_cards = []
    user_cards = random.sample(cards, 2)

    #Add up the two values of user cards
    sum = 0
    for i in range(len(user_cards)):
        sum += user_cards[i]
    print(f"Your cards : {user_cards}    Score is : {sum}")

    #Randomly choose computer's first card
    computer_card = random.sample(cards, 1)
    print(f"Computer's card : {computer_card}")

    #Continue doing this uptil end of game is not true
    end_of_game = False
    while not end_of_game:

        #Ask if user wants to contine or pass
        choice = input("Do you want to choose another card('y') or pass('n'): ")

        #If choice is y
        if choice == 'y':
            #Append third card in previous user cards list
            new_user_cards = random.sample(cards, 1)
            user_cards += new_user_cards
            print(user_cards)

            #Add up the third card
            sum += user_cards[2]
            print(f"Score is : {sum}")

        else:    
            #Randomly choose computer's next card
            comp_sum = 0
            new_computer_card = random.sample(cards, 1)
            computer_card += new_computer_card
            print(computer_card)

            for i in range(len(computer_card)):
                comp_sum += computer_card[i]
            print(f"Computer's score is : {comp_sum}")    

            #Calling compare fucntion
            result = compare(sum, comp_sum)
            print(result)
            end_of_game = True

play_game()
