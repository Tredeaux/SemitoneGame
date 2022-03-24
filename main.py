# ==============================================
#      Welcome to my Semitone Guesser game!
#      Tredeaux Pitout       2022 - 03 - 24
# ==============================================

import random

def initMessage():
    # This function serves to output the instructions
    print("================================================")
    print("   WELCOME TO THE SEMITONE GUESSER GAME!\n")
    print("   Instructions:")
    print("   Enter the amount of semitones between")
    print("   the two notes provided.")
    print("   \n   If you can't guess the simply enter")
    print("   'Give up' and the quiz will stop")
    print("================================================")


def menu():
    # This is the menu that displays the options
    print("\n")
    print("Enter '1' to play")
    print("Enter '2' to exit")


def quiz():
    stop = False
    while stop == False:
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 
                 'D#', 'E', 'F', 'F#', 'G', 'G#']
        
        # Grab 2 random Notes from my list
        firstNote = random.randrange(0, len(notes))
        secondNote = random.randrange(0, len(notes))
        
        # In the case that I grab the same 2 notes, 
        # just keep going until they are unique
        while secondNote == firstNote:
            secondNote = random.randrange(0, len(notes))
        
        # Display notes in nice format
        print("-----------------------------")
        print("Enter 'Give up' if you want to stop")
        print(f"First Note: \t{notes[firstNote]}")
        print(f"Second Note:\t{notes[secondNote]}")
        
        # Check regular distance between items
        length = abs((firstNote + 1) - (secondNote + 1))
            
        if length > 6:
            # Semitones work in both directions so this decision checks
            # if its more efficient to go the other way around
            # It must also check what direction to loop over
            if (firstNote + 1) > 6:
                length = abs((len(notes) - (firstNote + 1)) + (secondNote + 1))
            else:
                length = abs((len(notes) - (secondNote + 1)) + (firstNote + 1))

        # Get user decision
        answer = input("Answer: ")
        if answer == str(abs(length)):
            print("✔️\tCorrect!")
        elif answer.lower() == 'give up':
            stop = True
        else:
            print(f"❌\tIncorrect! The answer is {abs(length)} semitones")


if __name__ == "__main__":
    # Start and show init message
    initMessage()
    # Start menu and get decision
    
    menuOption = 0
    while menuOption != '2':
        menu()
        menuOption = input("Enter option: ")
        while menuOption != '1' and menuOption != '2':
            menuOption = input("Enter option: ")
        
        if menuOption == '1':
            quiz()
        elif menuOption == '2':
            print("Goodbye!")
        
    






