from colorama import init, Fore, Style
import random
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

init()

# Define the shop menu function
def shop_menu():
    print(Fore.LIGHTYELLOW_EX + "*****************************************")
    print(Fore.LIGHTBLUE_EX + "Welcome to the shop!")
    print("Type fishshop to upgrade your fishing rod 🎣")
    print("Type baitshop to upgrade bait multiplier🪱")
    print("Type goldshop to upgrade gold multiplier🧈")
    print("Press enter to go back to fishing")
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)
def fish():
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE)
    print("Option 1:" + Fore.LIGHTGREEN_EX + " Fishingrod 1 cost" + Fore.LIGHTYELLOW_EX + " 750 gold" + Fore.WHITE)
    print("Option 2:" + Fore.LIGHTBLUE_EX + " Fishingrod 2 cost" + Fore.LIGHTYELLOW_EX + " 3000 gold" + Fore.WHITE)
    print("Option 3:" + Fore.LIGHTRED_EX + " Fishingrod 3 cost" + Fore.LIGHTYELLOW_EX + " 10000 gold" + Fore.WHITE)
    print("press 1,2 or 3 or next page to countinue")
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)

def bait():
    print(Fore.LIGHTYELLOW_EX + "*****************************************")
    print("The bait shop is closed cum tommorow at 19pm")
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)

def gold():
    print(Fore.LIGHTYELLOW_EX + "*****************************************")
    print("no more gold unfortunately")
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)

def fisha():
    name = random.choice(["scrap!", "bottle!", "cod!"])
    print("You got a " + Fore.WHITE + "Common " + name + Fore.WHITE) 



# Main loop to check user input
while True:
    user_input = input("Enter a command: ")
    if user_input == "shop":
        shop_menu()
    if user_input == "fishshop":
        fish()
    if user_input == "baitshop":
        bait()
    if user_input == "goldshop":
        gold()
    if user_input == "fisha":
        fisha()
    elif user_input == "":
        break
    else:
        print("Invalid command. Type 'shop' to enter the shop, or press Enter to exit.")


print("Exited.")
