import os
import random
import time
from colorama import Fore, Style

# Define a class to represent the fishing game.
class FishingGame:
    def __init__(self):
        # Initialize the player's gold and gems to 0.
        self.gold = 0
        self.gems = 0

        # Multipliers to adjust the game's difficulty and rewards.
        self.rarity_multiplier = 20  # Increases the rarity of the fish encountered.
        self.gold_multiplier = 1  # Adjusts the amount of gold earned per catch.
        self.bait_multiplier = 1  # Adjusts the chances of successfully catching a fish.

        # Initialize counters for how many of each rarity of fish the player has caught.
        self.rarity_counts = {
            "common": 0,
            "rare": 0,
            "epic": 0,
            "legendary": 0,
            "mythical": 0,
            "godly": 0,
            "eternal": 0
        }

        # Define data for each rarity type, including catch chance, color for display, and gold value range.
        self.rarity_data = {
            "common": {"chance": 35, "color": Fore.WHITE, "min_value": 3, "max_value": 20},
            "rare": {"chance": 12, "color": Fore.BLUE, "min_value": 21, "max_value": 45},
            "epic": {"chance": 5, "color": Fore.LIGHTMAGENTA_EX, "min_value": 46, "max_value": 85},
            "legendary": {"chance": 1.9, "color": Fore.MAGENTA, "min_value": 86, "max_value": 150},
            "mythical": {"chance": 0.4, "color": Fore.LIGHTBLUE_EX, "min_value": 151, "max_value": 230},
            "godly": {"chance": 0.1, "color": Fore.YELLOW, "min_value": 231, "max_value": 350},
            "eternal": {"chance": 0.05, "color": Fore.LIGHTYELLOW_EX, "min_value": 351, "max_value": 550},
        }

    # Function to clear the console screen, different commands for Windows and other OS.
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Function to handle what happens when a fish is caught.
    def fish_caught(self, rarity):
        # Get the data associated with the caught fish's rarity.
        data = self.rarity_data[rarity]
        # Print a message indicating the rarity of the fish caught.
        print(f"You got a {data['color']}{rarity.capitalize()}!{Style.RESET_ALL}")
        # Increment the counter for this fish rarity.
        self.rarity_counts[rarity] += 1
        # Return a random amount of gold based on the fish's rarity.
        return random.randint(data["min_value"], data["max_value"])

    # Function to add gold to the player's total and notify them.
    def give_gold(self, value):
        # Print the amount of gold earned.
        print(f"You got {value} gold!")
        # Add the gold value to the player's total gold.
        self.gold += value

    # Main function that handles the fishing process.
    def fishing(self):
        # Wait for player input to start fishing, showing their current gold amount.
        input(f"Press enter to cast your line. (You have {self.gold} gold) ")

        # Clear the screen before the fishing sequence starts.
        self.clear_screen()

        # Simulate the waiting time for a fish to bite.
        print("Waiting...")
        time.sleep(random.randint(2, 5))  # Random wait time between 2 to 5 seconds.
        self.clear_screen()

        # Print a suspenseful message indicating something is happening.
        print("Oh..?")
        time.sleep(2)  # Wait for 2 seconds for added suspense.
        self.clear_screen()

        # Determine if the fish escapes based on a random chance adjusted by the bait multiplier.
        if random.random() <= 1 / 3 * self.bait_multiplier:
            # If the fish escapes, inform the player and end the function early.
            print(Fore.RED + "The fish escaped!" + Style.RESET_ALL)
            return

        # Generate a random number to determine the rarity of the fish.
        rarity = random.random() * 100
        # Loop through the rarity data to find the first rarity that the random number qualifies for.
        for name, data in sorted(self.rarity_data.items(), key=lambda item: item[1]["chance"], reverse=True):
            # Check if the rarity is found by comparing to the rarity chance adjusted by the multiplier.
            if rarity >= data["chance"] * self.rarity_multiplier:
                # If a rarity is matched, call fish_caught to get the value and add the gold.
                value = self.fish_caught(name)
                self.give_gold(value)
                break  # Exit the loop once a fish is caught.

        # Random chance to find a treasure chest containing gems.
        if random.random() <= 0.01:
            # If treasure is found, randomly decide how many gems are inside.
            treasure = random.randint(2, 5)
            # Notify the player and add the gems to their total.
            print(Fore.LIGHTGREEN_EX + f"You found a treasure! ({treasure} gems)" + Style.RESET_ALL)
            self.gems += treasure

# The main function to start the game.
def main():
    # Create an instance of the FishingGame class.
    game = FishingGame()
    # Start an infinite loop to allow continuous fishing.
    while True:
        # Call the fishing method to let the player fish.
        game.fishing()

# Entry point of the program.
if __name__ == "__main__":
    main()  # Start the game by calling the main function.
