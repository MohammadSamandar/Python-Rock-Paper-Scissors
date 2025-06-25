from random import choice
import json




def load_users():

    try:
        with open('users.json', 'r') as f:

            return json.load(f)
        
    except FileNotFoundError :
        
        return {}
        

   
    


def save_users(users_data):

    with open('users.json', 'w') as f:
        json.dump(users_data, f, indent=4)






    
def register(user_data):
    
    while True:
        username = input("Enter a new username: ")
        if username in user_data:
            print("This username already exists. Please choose another one.")

        else: 
            password = input("Enter a password: ")

            user_data[username] = {
                'password': password,
                'scores': {'win': 0, 'lose': 0, 'tie': 0}
            }

            print(f"User '{username}' registered successfully! Now you can login to account.")

            return user_data






def login(users_data):
    

    while True:
        username = input("Enter your username: ")
        
       
        if username not in users_data:
            print("username  invalid!!")
            continue
        
        password = input("Enter your password: ")
        if password == users_data[username]['password']:
            print(f"Welcome back, {username}!")
            return users_data[username]
        else:
            print("Incorrect password. Please try again.")


   
        



        






def get_user_choice():

    options = ['rock', 'paper', 'scissors']

    while True:
        user_input = input("Select an option {rock, paper, scissors}: ").lower()
        if user_input in options:
            return user_input
        else: 
            print("Invalid Input. Please choose from rock, paper, or scissors.")
    


def get_computer_choice():

    options = ['rock', 'paper', 'scissors']
    return choice(options)





def determine_winner(player_choice, computer_choice):


    if player_choice == computer_choice:
        return "tie"

    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "win"


    else:

        return "lose"




def play_one_round(current_user):
    print("\n--- New Round ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice,computer_choice)
    if result  == "tie":
        print("It's a tie")
        current_user['scores']['tie'] += 1
    elif result  == "lose":
        print("You Failed!!!")
        current_user['scores']['lose'] += 1
    else:
        print("You won!")
        current_user['scores']['win'] += 1


    scores = current_user['scores']
    print(f"Current scores - Win: {scores['win']}, Losses: {scores['lose']}, Tie: {scores['tie']}")



        
    


def main():
    
    all_user_data = load_users()
    current_user = None




    while True:
        choice = input("\n1. Login\n2. Register\n3. Exit\nEnter your choice: ")
            
        if choice == '1':
            current_user = login(all_user_data)
            if current_user:
                break

        elif choice == '2':
            all_user_data = register(all_user_data)

        elif choice== '3':
            print("GoodBye!")
            return
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
   

    while True:
        play_one_round(current_user)


        while True:
    
            play_again = input("Do you want play again? {yes / no}: ").lower()
            play_again_list = ['yes', 'no']
            if play_again in play_again_list:
                break
            else:
                print("Invaid Input.")

        if play_again == 'no':
            break


    save_users(all_user_data)
    print("Your scores have been saved. Thanks for playing!")



if __name__ == "__main__":
    main()