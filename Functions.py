import sys
import time


def title_screen():
    print("    Welcome to the game    \n___________________________")
    choice = ""
    while choice not in ['start', 'help', 'exit']:
        choice = input("> ").lower().replace(" ", "")
        if choice == "start":
            start_game()
        elif choice == "help":
            help_menu()
            choice = ""
        elif choice == "quit":
            print("Exiting game . . .")
            sys.exit()
    if choice not in ['start', 'help', 'exit']:
        print('Please enter a valid command.\n')



def start_game():
    print("Nice")


def help_menu():
    print("Start - Starts game\nHelp - Opens help menu\nQuit - Quits game \n")
   
