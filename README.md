# 🗿📄✂️ Rock, Paper, Scissors - Advanced Edition

This is an advanced, multi-user implementation of the classic "Rock, Paper, Scissors" game, built entirely in Python. It has evolved from a simple command-line script into a complete application featuring a robust user account system and persistent data storage using JSON.

This project demonstrates a comprehensive understanding of core programming principles, including modular design, data management, user authentication, and robust error handling, making it a strong portfolio piece.

## ✨ Key Features

### User & Data Management
* **User Registration & Login:** A full-fledged account system allows users to register new accounts and log in to existing ones.
* **Persistent Data Storage:** All user data, including credentials and scores, is saved to a `users.json` file, ensuring progress is never lost between sessions.
* **Score Tracking:** The game keeps a running tally of wins, losses, and ties for each individual user account.
* **Data Durability:** To prevent data loss from unexpected program termination, data is saved automatically after every critical event (new user registration and after each game round).

### Gameplay & User Experience
* **Classic Game Logic:** Accurately determines the winner based on the timeless rules (Rock > Scissors, Scissors > Paper, Paper > Rock).
* **Randomized Opponent:** The computer's choice is random in every round, ensuring fair and unpredictable gameplay.
* **Robust Input Validation:** The application is "bulletproof," handling invalid inputs for game moves, menu choices, and replay prompts gracefully.
* **Replayability:** A clean game loop allows users to play as many rounds as they wish after logging in.

## 🏗️ Code Architecture

The project is built on a clean, modular architecture where each function has a single, clear responsibility, separating concerns for better readability and maintainability.

* **Data Layer (`load_users`, `save_users`):** Handles all file I/O for reading from and writing to the `users.json` data store.
* **Authentication Layer (`register`, `login`):** Manages all user authentication logic, including new user creation and credential verification.
* **Game Logic Layer (`get_user_choice`, `get_computer_choice`, `determine_winner`):** Contains the pure logic of the game, completely decoupled from the user interface or data storage.
* **Main Application Flow (`play_one_round`, `main`):** Orchestrates the high-level program flow, from the initial user menu to the main game loop and final data save.

The script uses the `if __name__ == '__main__':` construct to serve as a proper entry point for the application.

## 🚀 How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository to your local machine.
3.  Navigate to the project directory in your terminal.
4.  Run the script with the following command:
    ```bash
    python game.py 
    ```
    *(Replace `game.py` with the actual name of your Python file if it's different.)*

## 💻 Technologies Used

* Python 3
* `random` module (Python Standard Library)
* `json` module (Python Standard Library)