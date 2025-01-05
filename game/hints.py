import random

HINT_POOL = {
    "cipher": [
        "Remember, Caesar shifts letters by a fixed amount.",
        "Vigenère uses a keyword. Focus on recurring patterns.",
        "Substitution ciphers map each letter uniquely. Look for clues in the text!"
    ],
    "math": [
        "Break the problem into smaller parts.",
        "Check your calculations twice. Small mistakes can lead to big errors!",
        "Think about alternate ways to solve the puzzle."
    ],
    "word": [
        "Focus on common prefixes or suffixes.",
        "Look for familiar patterns in the scrambled letters.",
        "Use process of elimination to narrow down possible words."
    ]
}

def get_hint(challenge_type):
    return random.choice(HINT_POOL.get(challenge_type, ["Hints not available for this challenge."]))
