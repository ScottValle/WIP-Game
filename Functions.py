import sys
import time


def title_screen():
    print("    Welcome to the game    ")
    print("___________________________")
    choice = input("> ").lower().replace(" ", "")
    if choice == "start":
        start_game()
    elif choice == "help":
        help_menu()
    elif choice == "quit":
        print("Exiting game . . .")
        sys.exit()
    while choice not in ['start', 'help', 'exit']:
        print('Please enter a valid command.\n')
        title_screen()


def start_game():
    print("Nice")


def help_menu():
    print("Start - Starts game")
    print("Help - Opens help menu")
    input("Quit - Quits game \n")
    title_screen()
