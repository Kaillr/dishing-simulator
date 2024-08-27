import os
import random
import time
from colorama import Fore

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def giveGold():
    global gold
    print("You got " + str(value) + " gold!")
    gold += value

gold = 0
gems = 0
rarityMultiplier = 1
goldMultiplier = 1
baitMultiplier = 1

clear()

while True:
    input("Press enter to cast your line. (You have " + str(gold) + " gold) ")
        
    clear()

    rarity = random.random() * 100

    print("Waiting...")
    time.sleep(random.randint(2, 5))
    clear()

    print("Oh..?")
    time.sleep(2)
    clear()

    if random.random() <= 1/3 * baitMultiplier:
        print(Fore.RED + "The fish escaped!" + Fore.WHITE)
        value = 0
    else:
        if rarity >= 120 * rarityMultiplier: # Common
            print("You got a " + Fore.RED + "common!" + Fore.WHITE)
            value = random.randint(1, 20)
            
        elif rarity >= 20 * rarityMultiplier: # Rare
            print("You got a " + Fore.GREEN + "rare!" + Fore.WHITE) 
            value = random.randint(21, 50)
            
        elif rarity >= 10 * rarityMultiplier: # Epic
            print("You got an " + Fore.BLUE + "epic!" + Fore.WHITE)
            value = random.randint(51, 100)
            
        elif rarity >= 5 * rarityMultiplier: # Legendary
            print("You got a " + Fore.MAGENTA + "legendary!" + Fore.WHITE)
            value = random.randint(101, 200)
            
        elif rarity >= 2.5 * rarityMultiplier: # Mythic
            print("You got a " + Fore.YELLOW + "mythic!" + Fore.WHITE)
            value = random.randint(201, 500)
            
        elif rarity >= 1.25 * rarityMultiplier: # Goldy
            print("You got a " + Fore.CYAN + "goldy!" + Fore.WHITE)
            value = random.randint(501, 1000)
            
        elif rarity >= 0.625 * rarityMultiplier: # Celestial
            print("You got a " + Fore.LIGHTYELLOW_EX + "celestial!" + Fore.WHITE)
            value = random.randint(1001, 2000)
            
        elif rarity >= 0.3125 * rarityMultiplier: # Divine
            print("You got a " + Fore.LIGHTBLACK_EX + "divine!" + Fore.WHITE)
            value = random.randint(2001, 5000)
            
        elif rarity >= 0.15625 * rarityMultiplier: # Transcendent
            print("You got a " + Fore.LIGHTMAGENTA_EX + "transcendent!" + Fore.WHITE)
            value = random.randint(5001, 10000)
            
        elif rarity >= 0.078125 * rarityMultiplier: # Eternal
            print("You got an " + Fore.LIGHTCYAN_EX + "eternal!" + Fore.WHITE)
            value = random.randint(10001, 20000)
    if random.random() <= 1:
        treasure = random.randint(2, 5)
        print(Fore.LIGHTGREEN_EX + "You found a treasure!" + Fore.GREEN + "(" + str(treasure) + " gems)" + Fore.WHITE)
        gems += treasure
        
    
    giveGold()