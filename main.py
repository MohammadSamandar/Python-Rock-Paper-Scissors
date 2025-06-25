from random import choice



options = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        userinput = input("Select an option {rock, paper, scissors}: ").lower()
        if userinput in options:
            break
        else: 
            print("Invalid Input")
    

    print("user selected: ", userinput)
    return userinput





def get_computer_choice():

    computer_choice = choice(options)
    print("bot selected: ", computer_choice)
    return computer_choice





def determine_winner(player_choice, computer_choice):


    if player_choice == computer_choice:
        return "tie"

    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and       computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
        return "win"


    else:

        return "lose"






def play_game():

    while True:
        
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        game_result  = determine_winner(user_choice,computer_choice)
        if game_result  == "tie":
            print("It's a tie")
        elif game_result  == "lose":
            print("You Failed!!!")
        else:
            print("You won!")
    

            


        while True:
    
            play_again = input("Do you want play again? {yes , no}: ").lower()
            play_again_list = ['yes', 'no']
            if play_again in play_again_list:
                break
            else:
                print("Invaid Input.")

        if play_again == 'no':
            break


if __name__ == "__main__":
    play_game()



# while True:


    # options = ['rock', 'paper', 'scissors']


    # while True:
    #     userinput = input("Select an option {rock, paper, scissors}: ").lower()
    #     if userinput in options:
    #         break
    #     else: 
    #         print("Invalid Input")
    

    # print("user selected: ", userinput)



    # computer_choice = choice(options)
    # print("bot selected: ", computer_choice)





    # if userinput == computer_choice:
    #     print("It's a tie!")

    # elif (userinput == 'rock' and computer_choice == 'scissors') or (userinput == 'paper' and       computer_choice == 'rock') or (userinput == 'scissors' and computer_choice == 'paper'):
    #     print("You won!")


    # else:

    #     print('You Failed!!!')



    # while True:
    
    #     play_again = input("Do you want play again? {yes , no}: ").lower()
    #     play_again_list = ['yes', 'no']
    #     if play_again in play_again_list:
    #         break
    #     else:
    #         print("Invaid Input.")

    # if play_again == 'no':
    #     break
