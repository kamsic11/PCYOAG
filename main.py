import os
import time 
import random
import sys
import pygame

# hello

pygame.init()                      #initialize pygame

# ---------------------------------------------------------
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

try:
    folder = "media"
    pygame.mixer.music.load(os.path.join(folder, 'ghost.mp3'))#load music
    ghost_laugh = pygame.mixer.Sound(os.path.join(folder,'ghost laugh.mp3'))  #load sound
    clock_noise = pygame.mixer.Sound(os.path.join(folder,'clock noise.mp3'))  #load sound
    door_sound = pygame.mixer.Sound(os.path.join(folder,'door sound.mp3'))  #load sound
    scream = pygame.mixer.Sound(os.path.join(folder,'scream.mp3'))  #load sound
    boo = pygame.mixer.Sound(os.path.join(folder,'boo.mp3'))  #load sound
    echo = pygame.mixer.Sound(os.path.join(folder,'echo.mp3'))  #load sound
    game_over = pygame.mixer.Sound(os.path.join(folder,'game over.mp3'))  #load sound
    congrats = pygame.mixer.Sound(os.path.join(folder,'congrats.mp3'))  #load sound





except:
    raise(UserWarning, "could not load or play soundfiles in 'media' folder :-(")




# ----------------------------------------------------
pygame.mixer.music.play(-1)       # play music on loop
# ----------------------------------------------------
# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to pause for readability
def sleep_pause(seconds):
    time.sleep(seconds)


# Function to get user's choice
def choose_option(num_options):
    while True:
        choice = input(f"Enter a number (1-{num_options}): ")
        if choice.isdigit() and 1 <= int(choice) <= num_options:
            return int(choice)
        print("Invalid choice, try again!")

 # ASCII ART

GHOST_ART = r"""
  .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'
"""


# Introduction
def introduction():
    global player_name
    clear_screen()
    print("\033[30;102mWelcome to 'The Ghost Who Loved Puns'!\033[0m")
    sleep_pause(1)

    print("Welcome, brave adventurer! You have just arrived at your new house, ")
    door_sound.play()
    print("which isn't so new and has an eerie atmosphere. The floorboards creak "
          "and there's a faint hint of something spooky in the air.")
    sleep_pause(2)

    print("\nAs the clock strikes midnight, you hear a strange noise—sort of sounds ")
    clock_noise.play()

    print("\nlike a giggle... You turn the corner, heart pounding, as you are supposed "
          "to be home alone and not expecting any visitors, and there, floating in front "
          "of you, is a ghost! You scream out of fear.")
    scream.play()
    sleep_pause(3)

    print("\nBut this isn't your average, soul-chilling specter. No, this ghost seems to have "
          "a weird obsession with…punny jokes! With a mischievous grin, it suddenly bursts out: "
          "'Boo! Or should I say… 'Boo-tiful evening, isn't it?'!'")
    boo.play()
    sleep_pause(3)

    print("\nYour task? Survive the night. Or perhaps, just maybe, find a way to make this "
          "laugh-loving ghost your friend.")
    print("Will you fall prey to the ghost's hilarious hauntings, or can you outwit the puns "
          "and escape? The choice is yours... just don't get caught in the pun-derworld!")
    sleep_pause(3)

    player_name = input("\nBefore we start, what is your name, brave adventurer? ")
    print(f"\nWelcome, {player_name}! Prepare for a night of spooky puns!")
    input("\nPress Enter to continue... ")
    level1()


# Function to skip the introduction
def skip_intro():
    clear_screen()
    print("Skipping introduction...")
    sleep_pause(1)
    start()


# Function to replay the introduction
def replay_intro():
    choice = input("Would you like to replay the introduction? (yes/no): ").strip().lower()
    if choice == "yes":
        clear_screen()
        player_name = introduction()  # Replay the introduction
        start()  # Start the game after replaying the intro
    else:
        start()


# Function to start the game
def start():
    clear_screen()
    print("\033[30;102mThe Ghost Who Loved Puns\033[0m")
    print("Your adventure begins...")
    sleep_pause(1)
    print("A spooky voice echoes through the hallway...")
    echo.play()
    level1()


# Punny Riddle Function
def punny_riddle():
    print("\nYou bravely accept the challenge!")
    print("\033[32m[Good Choice]\033[0m: The ghost is pleased with your bravery!")
    sleep_pause(2)
    level3()


# Level 1: The Creepy Hallway
def level1():
    clear_screen()
    print("\nLevel 1: The Creepy Hallway")
    print(GHOST_ART)
    sleep_pause(2)
    print("Ghost: 'I was going to tell you a joke, but it might go over your head!'")
    ghost_laugh.play()
    print("\U0001F602")
    print("What will you do?")
    print("1) Laugh along\n2) Run away\n3) Tell your own pun\n4) Ignore the ghost")
    choice = choose_option(4)

    if choice == 1:
        print("\nThe ghost smiles. 'Finally! Someone who appreciates my humor!'")
        print("\033[32m[Good Choice]\033[0m: The ghost lets you pass without issue.")
        sleep_pause(2)
        level2()
    elif choice == 2:
        bad_ending1()
    elif choice == 3:
        good_ending3()
    else:
        bad_ending3()


# Level 2: The Haunted Kitchen
def level2():
    clear_screen()
    print("\nLevel 2: The Haunted Kitchen")
    sleep_pause(2)
    print("The ghost challenges you to a pun battle!\n")
    print("1) Accept the challenge\n2) Try to escape\n3) Distract the ghost with a riddle\n4) Offer the ghost a snack")
    choice = choose_option(4)

    if choice == 1:
        punny_riddle()
    elif choice == 2:
        bad_ending2()
    elif choice == 3:
        good_ending4()
    elif choice == 4:
        level3()


# Punny Riddle
def punny_riddle():
    riddles = [
        {"question": "What did the ocean say to the beach?", "answer": "Nothing, it just waved."},
        {"question": "Why did the scarecrow win an award?", "answer": "Because he was outstanding in his field."},
        {"question": "Why don't skeletons fight each other?", "answer": "They don't have the guts."}
    ]
    riddle = random.choice(riddles)
    print(f"Ghost: 'Here's my riddle for you: {riddle['question']}'")
    player_answer = input("Your answer: ").strip().lower()
    if player_answer == riddle['answer'].lower():
        print("Correct! The ghost laughs and lets you pass.")
        level3()
    else:
        print("Wrong! The ghost laughs at your failed answer.")
        bad_ending2()


# Level 3: The Ghost's Punny Lair
def level3():
    clear_screen()
    print("\nLevel 3: The Ghost's Punny Lair")
    sleep_pause(2)
    print("The ghost laughs: 'I told you, I'm 'pun-derful!'")
    print(
        "1) Outwit the ghost\n2) Befriend the ghost\n3) Try to escape\n4) Challenge the ghost to a dance battle\n5) Join the ghost in telling puns forever")
    choice = choose_option(5)

    if choice == 1:
        good_ending1()
    elif choice == 2:
        good_ending2()
    elif choice == 3:
        bad_ending2()
    elif choice == 4:
        bad_ending5()
    else:
        good_ending5()


# Game Conclusion
def game_conclusion():
    print("\n\033[30;102mThank you for playing 'The Ghost Who Loved Puns'!\033[0m")
    sleep_pause(2)
    print("We hope you had a hauntingly fun time full of puns and laughter!")
    print("Until next time, stay 'pun-derful'!" + "\U0001F47B")
    congrats.play()


# Endings
def good_ending1():
    print(f"\n{player_name}, you outwitted the ghost with puns!" + "\U0001F389")
    sleep_pause(2)
    print("The ghost laughs so hard, it lets you go! You survived the night!")
    congtats.play()
    game_conclusion()
    play_again()


def good_ending2():
    print(f"\n{player_name}, you befriended the ghost!" + "\U0001F47B" + "\U00002764")
    sleep_pause(2)
    print("You now have a ghostly friend for life!")
    congats.play()
    game_conclusion()
    play_again()


def good_ending3():
    print(f"\n{player_name}, your pun made the ghost laugh so hard it let you go!" + "\U0001F602")
    congrats.play()
    sleep_pause(2)
    game_conclusion()
    play_again()


def good_ending4():
    print(f"\n{player_name}, your riddle confused the ghost, allowing you to escape!" + "\U0001F3C3")
    congrats.play()
    sleep_pause(2)
    game_conclusion()
    play_again()


def good_ending5():
    print(f"\n{player_name}, you and the ghost tell puns together forever!" + "\U0001F47B" + "\U0001F602")
    congrats.play()
    sleep_pause(2)
    print("Now you're an eternal pun master!")
    game_conclusion()
    play_again()


def bad_ending1():
    print(f"\nOh no, {player_name}! You're trapped in a pun-filled nightmare!" + "\U0001F628")
    game_over.play()

    sleep_pause(2)
    game_conclusion()
    play_again()


def bad_ending2():
    print(f"\n{player_name}, you failed to escape the ghost's lair!" + "\U0001F480")
    game_over.play()
    sleep_pause(2)
    game_conclusion()
    play_again()


def bad_ending3():
    print(f"\n{player_name}, ignoring the ghost made it mad! Now you're trapped forever!" + "\U0001F628")
    game_over.play()
    sleep_pause(2)
    game_conclusion()
    play_again()


def bad_ending5():
    print(f"\n{player_name}, the ghost won the dance battle and trapped you forever!" + "\U0001F57A" + "\U0001F47B")
    game_over.play()
    sleep_pause(2)
    game_conclusion()
    play_again()


def play_again():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice == "yes":
        introduction()
    else:
        print("Thanks for playing!")
        sys.exit()


# Start the game
def start_game():
    clear_screen()
    choice = input("Would you like to skip the introduction? (yes/no): ").strip().lower()
    if choice == "yes":
        global player_name
        player_name = input("Enter your name, brave adventurer: ")
        print(f"Welcome, {player_name}! Prepare for a night of spooky puns!")
        input("Press Enter to continue... ")
        level1()
    else:
        introduction()


if __name__ == "__main__":
    start_game()

if __name__ == "__main__":
    introduction()