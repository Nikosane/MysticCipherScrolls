import random

def play_challenge():
    """
    Simulates a mini-game or challenge for the player to earn a cipher key.
    Returns True if the challenge is won, otherwise False.
    """
    print("\nChallenge: Solve a math puzzle to earn a key!")
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct_answer = a * b
    print(f"What is {a} * {b}?")
    try:
        player_answer = int(input("Your answer: "))
        if player_answer == correct_answer:
            print("Correct! You win the challenge.")
            return True
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False
