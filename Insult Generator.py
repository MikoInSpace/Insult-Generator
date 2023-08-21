import random
import os
import time

def pick_random_word(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    
    if words:
        return random.choice(words)
    else:
        return "No words found in the file."

while True:
 
 print("Welcome to the insult generator!")
 print("Select an option.")
 print("1. Pick a random word.")
 print("2. Exit.")

 option = input("Option: ")
 
 if option == "1":
     os.system('cls' if os.name == 'nt' else 'clear')
     script_directory = os.path.dirname(os.path.abspath(__file__))
     filename = os.path.join(script_directory, "insults.txt")
     random_word = pick_random_word(filename)
     print("Random word:", random_word)
     print(" ")
 elif option == "2":
     print("Exiting...")
     time.delay(1)
     break
