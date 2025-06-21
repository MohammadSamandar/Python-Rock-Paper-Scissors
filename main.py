from random import choice




while True:


    options = ['rock', 'paper', 'scissors']


    while True:
        userinput = input("Select an option {rock, paper, scissors}: ").lower()
        if userinput in options:
            break
        else: 
            print("Invalid Input")
    

    print("user selected: ", userinput)

    computer_choice = choice(options)
    print("bot selected: ", computer_choice)

    if userinput == computer_choice:
        print("It's a tie!")

    elif (userinput == 'rock' and computer_choice == 'scissors') or (userinput == 'paper' and       computer_choice == 'rock') or (userinput == 'scissors' and computer_choice == 'paper'):
        print("You won!")


    else:

        print('You Failed!!!')



    while True:
    
        play_again = input("Do you want play again? {yes , no}: ").lower()
        play_again_list = ['yes', 'no']
        if play_again in play_again_list:
            break
        else:
            print("Invaid Input.")

    if play_again == 'no':
        break
