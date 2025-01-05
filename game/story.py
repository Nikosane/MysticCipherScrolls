import time

def display_intro():
    print("\nWelcome to Mystic Cipher Scrolls!")
    time.sleep(1)
    print("In a world of ancient mysteries, your mission is to uncover hidden scrolls encrypted with powerful ciphers.")
    time.sleep(2)
    print("Prepare for challenges, puzzles, and an adventure through mystical locations.\n")

def display_outro():
    print("\nCongratulations, Adventurer!")
    time.sleep(1)
    print("You have uncovered all the ancient scrolls and restored the knowledge of the ancients.")
    time.sleep(2)
    print("Thank you for playing Mystic Cipher Scrolls. Until next time, farewell!")
    time.sleep(2)

def narrate_location(location_name):
    print(f"As you journey through the land, you arrive at {location_name}.")
    time.sleep(1)
    print("You feel a sense of mystery in the air. What secrets will this place reveal?\n")

def narrate_failure():
    print("The secrets of this scroll remain locked. Perhaps another attempt will unveil its mysteries.")
    time.sleep(1)

def narrate_success(scroll_name):
    print(f"Success! You have deciphered the scroll of {scroll_name} and unlocked its wisdom.")
    time.sleep(1)
