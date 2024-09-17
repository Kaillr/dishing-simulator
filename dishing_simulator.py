import os
import sys
import json
import random
import time
from colorama import init, Fore, Style
import msvcrt

# Initialize variables
gold = 0
gems = 0

totalGold = 0
totalGems = 0
totalCasts = 0
totalEscaped = 0

rarityMultiplier = 1
goldMultiplier = 1
baitMultiplier = 1
rodLvl = 0

common = 0
rare = 0
epic = 0
legendary = 0
mythical = 0
godly = 0
eternal = 0

startup = True

save_file = "save_data.json"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def flush_input():
    """Flush the input buffer."""
    while msvcrt.kbhit():
        msvcrt.getch()

def save_game():
    """Save the game state to a JSON file."""
    data = {
        'gold': gold,
        'gems': gems,
        'totalGold': totalGold,
        'totalGems': totalGems,
        'totalCasts': totalCasts,
        'totalEscaped': totalEscaped,
        'rarityMultiplier': rarityMultiplier,
        'goldMultiplier': goldMultiplier,
        'baitMultiplier': baitMultiplier,
        'rodLvl': rodLvl,
        'common': common,
        'rare': rare,
        'epic': epic,
        'legendary': legendary,
        'mythical': mythical,
        'godly': godly,
        'eternal': eternal
    }
    
    with open(save_file, 'w') as file:
        json.dump(data, file)

def load_game():
    """Load the game state from a JSON file."""
    global gold, gems, totalGold, totalGems, totalCasts, totalEscaped
    global rarityMultiplier, goldMultiplier, baitMultiplier, rodLvl
    global common, rare, epic, legendary, mythical, godly, eternal
    
    if os.path.exists(save_file):
        with open(save_file, 'r') as file:
            data = json.load(file)
        
        gold = data.get('gold', 0)
        gems = data.get('gems', 0)
        totalGold = data.get('totalGold', 0)
        totalGems = data.get('totalGems', 0)
        totalCasts = data.get('totalCasts', 0)
        totalEscaped = data.get('totalEscaped', 0)
        rarityMultiplier = data.get('rarityMultiplier', 1)
        goldMultiplier = data.get('goldMultiplier', 1)
        baitMultiplier = data.get('baitMultiplier', 1)
        rodLvl = data.get('rodLvl', 0)
        common = data.get('common', 0)
        rare = data.get('rare', 0)
        epic = data.get('epic', 0)
        legendary = data.get('legendary', 0)
        mythical = data.get('mythical', 0)
        godly = data.get('godly', 0)
        eternal = data.get('eternal', 0)
    else:
        print("Welcome to Dishing Simulator!")

def giveGold():
    global gold
    global totalGold
    print("You got " + str(value) + " gold!")
    gold += value
    totalGold += value
    fishing()

def menuSelect(command):
    if command == "shop" or command == "store":
        shop()
    elif command == "rod":
        upgradeRod()
    elif command == "bait":
        upgradeBait()
    elif command == "stats" or command == "stat" or command == "statistics":
        stats()
    elif command == "restart" or command == "relaunch" or command == "r":
        restart()
    elif command == "exit" or command == "quit" or command == "q":
        exit()
    elif command == "help" or command == "commands":
        help()
    elif command == "rebirth":
        rebirth()
    elif command == "save":
        save_game()
    elif command == "load":
        load_game()
    elif command == "":
        fishing
    else:
        print("Invalid command, type 'help' for a list of commands.")
        input()

def shop():
    clear()
    print(Fore.LIGHTYELLOW_EX + "*****************************************")
    print(Fore.LIGHTBLUE_EX + "Welcome to the shop!")
    print("Type 'rod' to buy fishing rods 🎣")
    print("Type 'bait' to buy better baits 🪱")
    print("Type 'gold' to upgrade gold multiplier🧈")
    print("Press enter to go back to fishing")
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)
    command = input()
    shopSelect(command)
    
def shopSelect(command):
    if command == "rod":
        upgradeRod()
    elif command == "bait":
        upgradeBait()

def upgradeBait():
    clear()
    print(Fore.LIGHTYELLOW_EX + "******************************************************************************" + Fore.WHITE + Style.RESET_ALL)
    print("Option 1:" + Fore.LIGHTGREEN_EX + " whorms: " + Fore.LIGHTYELLOW_EX + " 1000 gold" + Fore.WHITE)
    print("Option 2:" + Fore.LIGHTBLUE_EX + " long whorms:      " + Fore.LIGHTYELLOW_EX + " 5000 gold" + Fore.WHITE)
    print("Option 3:" + Fore.LIGHTRED_EX + " snakes :            " + Fore.LIGHTYELLOW_EX + " 13000 gold" + Fore.WHITE)
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)
    print("Press enter to go back to the fishies")

def upgradeRod():
        clear()
        print("-------------------------------------")
        print("Welcome to the Fishing Rod Shop!" + "\n")
        print("1." + Fore.LIGHTGREEN_EX + " Adventures Fishingrod: " + (" (Owned)" if rodLvl >= 1 else " (750 gold)") + Fore.WHITE)
        print("2." + Fore.LIGHTBLUE_EX + " steel Fishingrod:     " + (" (Owned)" if rodLvl >= 2 else " (3000 gold)" + Fore.WHITE))
        print("3." + Fore.LIGHTRED_EX + " AquaStrike:          " + Fore.LIGHTYELLOW_EX + (" (Owned)" if rodLvl >= 3 else " (10000 gold)") + Fore.WHITE)
        print("-------------------------------------")
        print("Press enter to go back to the fishies")
        command = input()
        buyRod(command)
        
def buyRod(command):
    global gold, rodLvl, rarityMultiplier
    
    if command == "":
        shop()
    elif command == "1":
        if rodLvl < 1:
            if gold >= 750:
                gold -= 750
                rarityMultiplier = 1.1
                rodLvl = 1
                save_game()
                print( Fore.GREEN + " Succsess!" + Fore.WHITE + " Thank you for Purching the Adventures Fishingrod!")
            else:
                print( Fore.RED + "You do not have enough gold!")
        else:
            print("You already have this rod!")
            
    elif command == "2":
        if rodLvl < 2:
            if gold >= 500:
                gold -= 500
                rodLvl = 2
                print( Fore.GREEN + " Succsess!" + Fore.WHITE + " Thank you for Purching the Steel Fishingrod!")
            else:
                print( Fore.RED + "You do not have enough gold!")
        else:
            print("You already have this rod!")
                
        

def stats():
    clear()
    print("Here are your fishing stats:" + "\n")
    
    print(Fore.WHITE + "Common: " + Fore.WHITE + str(common))
    print(Fore.BLUE + "Rare: " + Fore.WHITE + str(rare))
    print(Fore.LIGHTMAGENTA_EX + "Epic: " + Fore.WHITE + str(epic))
    print(Fore.MAGENTA + "Legendary: " + Fore.WHITE + str(legendary))
    print(Fore.LIGHTBLUE_EX + "Mythical: " + Fore.WHITE + str(mythical))
    print(Fore.YELLOW + "Godly: " + Fore.WHITE + str(godly))
    print(Fore.LIGHTYELLOW_EX + "Eternal: " + Fore.WHITE + str(eternal) + "\n")
    
    print("Total Gems: " + str(totalGems))
    print("Total Gold: " + str(totalGold) + "\n")
    
    print("Total amount of casts: " + str(totalCasts) + "\n")
    
    print("Press enter to go back to fishing")
    input()

def help():
    clear()
    print("Welcome to dishing simulator, catch the fishies, upgrade your gear, explore different dimensions!")
    print("Type 'shop' to access the shop, 'stats' to see your stats, 'exit' to exit the game.")
    print("Press enter to go back to fishing")
    input()

def exit():
    quit()

def restart():
    os.execv(sys.executable, [sys.executable] + sys.argv)

def rebirth():
    if input("Are you sure you want to rebirth? (y/n) ") != "y":
        return
    else:
        rebirthConfirm()

def rebirthConfirm():    
    global gold, gems, totalGold, totalGems, totalCasts, totalEscaped
    global value, rodLvl, rarityMultiplier, goldMultiplier, baitMultiplier
    global common, rare, epic, legendary, mythical, godly, eternal
    
    gold = 0
    gems = 0
    totalGold = 0
    totalGems = 0
    totalCasts = 0
    totalEscaped = 0
    value = 0
    rodLvl = 0
    rarityMultiplier = 1
    goldMultiplier = 1
    baitMultiplier = 1
    common = 0
    rare = 0
    epic = 0
    legendary = 0
    mythical = 0
    godly = 0
    eternal = 0            
    
    clear()
    print("You have been reborn!")
    input()
    fishing()

def fishing():
    global gold, totalGold, gems, totalGems, totalCasts, value, rodLvl, rarityMultiplier, goldMultiplier, baitMultiplier, common, rare, epic, legendary, mythical, godly, eternal, startup

    
    global startup
    if startup == True:
        load_game()
        startup = False
    else:
        save_game()
    
    flush_input()
    
    command = ""
    
    command = input("Press enter to cast your line. (You have " + str(gold) + " gold) ")
    menuSelect(command)
    
    clear()
    
    rarity = random.random() * 100

    totalCasts += 1

    print("Waiting...")
    time.sleep(random.randint(3, 6) / (baitMultiplier))
    
    print("Oh..?")
    time.sleep(2)
    clear()
    
    print("Reeling...")
    time.sleep(random.randint(6, 10) / (rodLvl / 5 + 1))
    clear()

    if random.random() <= 1/3 * baitMultiplier:
        fishescape_index = random.choice(["Giant Sea Bass", "Splitfin", "Sellable Laptop", "Stingray", "Goblin Shark", "Zebra Pleco", "Smalltooth Sawfish", "Snapper", "Sunfish", "Red Hand Fish", "Plastic Bag", "Bonefish", "Coalfish", "Scrap", "Bottle", "Cod"])
        escaped = random.choice([" escaped", " got wrecked", " sailed away", " vanished", " disappeared"])
        print(Fore.RED + fishescape_index + escaped + Fore.WHITE)
        value = 0
    else:
        rarity = random.random() * 100
        if rarity < 0.1 * rarityMultiplier and rodLvl >= 4: # Eternal
            eternal_index = random.choice(["Giant sea bass"])
            print("You got an " + Fore.LIGHTYELLOW_EX + "Eternal " + Fore.WHITE + eternal_index)
            eternal += 1
            value = random.randint(351, 550)
            
        elif rarity <= 0.4 * rarityMultiplier and rodLvl >= 3: # Godly
            Godly_index = random.choice(["Splitfin", "sellable laptop", "Stingray"])
            print("You got a " + Fore.YELLOW + "Godly " + Fore.WHITE + Godly_index)
            godly += 1
            value = random.randint(231, 350)
            
        elif rarity <= 1.9 * rarityMultiplier and rodLvl >= 2: # Mythical
            Mythical_index = random.choice(["goblin shark!", "zebra pleco!", "Smalltooth Sawfish!"])
            print("You got a " + Fore.LIGHTBLUE_EX + "Mythical " + Fore.WHITE + Mythical_index)
            mythical += 1
            value = random.randint(151, 230)
            
        elif rarity <= 5 * rarityMultiplier and rodLvl >= 1: # Legendary
            Legendary_index = random.choice(["snapper!", "sunfish!", "red hand fish!"])
            print("You got a " + Fore.MAGENTA + "Legendary " + Legendary_index +  Fore.WHITE)
            legendary += 1
            value = random.randint(86, 150)
            
        elif rarity <= 12 * rarityMultiplier: # Epic
            Epic_index = random.choice(["ray!", "sailfish!", "salmon!"])
            print("You got a " + Fore.LIGHTMAGENTA_EX + "Epic " + Epic_index + Fore.WHITE)
            epic += 1
            value = random.randint(46, 85)
            
        elif rarity <= 35 * rarityMultiplier: # Rare
            Rare_index =  random.choice(["plastic bag!", "Bonefish!", "coalfish!"])
            print("You got a " + Fore.BLUE + "Rare " + Rare_index + Fore.WHITE) 
            rare += 1
            value = random.randint(21, 45)
            
        elif rarity <= 100 * rarityMultiplier: # Common
            Commen_index = random.choice(["scrap", "bottle", "cod"])
            print("You got a " + Fore.WHITE + "Common " + Commen_index + Fore.WHITE)
            common += 1
            value = random.randint(3, 20)
    if random.random() <= 0.01:
        treasure = random.randint(2, 5)
        print(Fore.LIGHTGREEN_EX + "You found a treasure!" + Fore.GREEN + "(" + str(treasure) + " gems)" + Fore.WHITE)
        gems += treasure
        totalGems += treasure
        
    giveGold()

clear()

fishing()
