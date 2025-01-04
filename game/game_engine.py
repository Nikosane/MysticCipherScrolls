import random
from cipher_tools import encrypt_text, decrypt_text
from locations import get_random_location
from challenges import play_challenge
from inventory import Inventory
from story import display_intro, display_outro

class MysticCipherScrollsGame:
    def __init__(self):
        self.inventory = Inventory()
        self.current_location = None

    def start_game(self):
        display_intro()
        while not self.inventory.all_scrolls_collected():
            self.current_location = get_random_location()
            print(f"\nYou have arrived at {self.current_location['name']}.")

            # Collect keys through challenges
            for i in range(self.current_location['key_count']):
                print(f"Challenge {i + 1} to earn a cipher key!")
                if play_challenge():
                    key = self.current_location['keys'][i]
                    self.inventory.add_key(key)
                    print(f"You earned a new key: {key}!")
                else:
                    print("You failed the challenge. Try again!")

            # Attempt to decode the scroll
            print("\nDecoding the scroll...")
            encrypted_message = self.current_location['encrypted_scroll']
            for key in self.inventory.keys:
                decrypted_message = decrypt_text(encrypted_message, key)
                if decrypted_message == self.current_location['scroll_content']:
                    print(f"Success! You decoded the scroll: {decrypted_message}")
                    self.inventory.add_scroll(self.current_location['scroll_name'])
                    break
            else:
                print("Failed to decode the scroll. Move to the next location.")

        display_outro()

if __name__ == "__main__":
    game = MysticCipherScrollsGame()
    game.start_game()
