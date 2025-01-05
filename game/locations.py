import random
from constants import SCROLLS, LOCATIONS

def get_random_location():
    location = random.choice(LOCATIONS)
    scroll = random.choice(SCROLLS)
    encrypted_scroll = scroll["encrypted"]
    return {
        "name": location,
        "scroll_name": scroll["name"],
        "scroll_content": scroll["content"],
        "encrypted_scroll": encrypted_scroll,
        "key_count": random.randint(2, 4),
        "keys": [scroll["key"]]
    }
