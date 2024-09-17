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
    print("------------------------------------------" + Fore.WHITE)
    print("Option 1:" + Fore.LIGHTGREEN_EX + " Adventures Fishingrod: " + Fore.LIGHTYELLOW_EX + " 750 gold" + Fore.WHITE)
    print("Option 2:" + Fore.LIGHTBLUE_EX + " steel Fishingrod:      " + Fore.LIGHTYELLOW_EX + " 3000 gold" + Fore.WHITE)
    print("Option 3:" + Fore.LIGHTRED_EX + " AquaStrike:            " + Fore.LIGHTYELLOW_EX + " 10000 gold" + Fore.WHITE)
    print("press 1,2,3 or type 'page 2' to countinue")
    print("-----------------------------------------" + Fore.WHITE + Style.RESET_ALL)

def fishrod_1():
    print(Fore.LIGHTYELLOW_EX + "***************************************************")
    print(" Succsess! Thank you for Purching the Adventures Fishingrod!")
    print(Fore.LIGHTYELLOW_EX + "***************************************************" + Fore.WHITE + Style.RESET_ALL)

def fishrod_2():
    print(Fore.LIGHTYELLOW_EX + "***************************************************")
    print(" Succsess! Thank you for Purching the steel Fishingrod:!")
    print(Fore.LIGHTYELLOW_EX + "***************************************************" + Fore.WHITE + Style.RESET_ALL)

def fishrod_3():
    print(Fore.LIGHTYELLOW_EX + "***************************************************")
    print(" Succsess! Thank you for Purching the AquaStrike!")
    print(Fore.LIGHTYELLOW_EX + "***************************************************" + Fore.WHITE + Style.RESET_ALL)

def bait():
    print(Fore.LIGHTYELLOW_EX + "*****************************************")
    print("Option 1:" + Fore.LIGHTGREEN_EX + " whorms: " + Fore.LIGHTYELLOW_EX + " 1000 gold" + Fore.WHITE)
    print("Option 2:" + Fore.LIGHTBLUE_EX + " long whorms:      " + Fore.LIGHTYELLOW_EX + " 5000 gold" + Fore.WHITE)
    print("Option 3:" + Fore.LIGHTRED_EX + " snakes :            " + Fore.LIGHTYELLOW_EX + " 13000 gold" + Fore.WHITE)
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)

def bait_1():
    print(Fore.LIGHTYELLOW_EX + "***************************************************")
    print(" Succsess! Thank you for Purching the whorms!")
    print(Fore.LIGHTYELLOW_EX + "***************************************************" + Fore.WHITE + Style.RESET_ALL)

def bait_2():
    print(Fore.LIGHTYELLOW_EX + "***************************************************")
    print(" Succsess! Thank you for Purching the long whorms!")
    print(Fore.LIGHTYELLOW_EX + "***************************************************" + Fore.WHITE + Style.RESET_ALL)

def bait_3():
    print(Fore.LIGHTYELLOW_EX + "***************************************************")
    print(" Succsess! Thank you for Purching the snakes!")
    print(Fore.LIGHTYELLOW_EX + "***************************************************" + Fore.WHITE + Style.RESET_ALL)

def gold():
    print(Fore.LIGHTYELLOW_EX + "*****************************************")
    print("no more gold unfortunately")
    print(Fore.LIGHTYELLOW_EX + "*****************************************" + Fore.WHITE + Style.RESET_ALL)



#while shop it open=true annd option 1


# Main loop to check user input **********
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
    if user_input == "1":
        bait_1()
    if user_input == "2":
        bait_2()
    if user_input == "3":
        bait_3()
    elif user_input == "":
        break
    else:
        print("go back?")


if shop_menu == True:
    if user_input == "1":
        fishrod_1()
    if user_input == "2":
        fishrod_2()
    if user_input == "3":
        fishrod_3()
    else:
        print("Invalid command. Type 'shop' to enter the shop, or press Enter to exit.")

print("Exited.")
