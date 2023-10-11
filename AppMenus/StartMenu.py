import time
import AppMenus.ManageNPCs
import ClearScreen
import IsValidInput
def goToStartMenu():

    print("\n"
          "\t+-------------+\n"
          "\t|     ~~~     |\n"
          "\t| NPC MANAGER |\n"
          "\t|     ~~~     |\n"
          "\t+-------------+")

    print("Press enter to continue...")
    input()

    while True:
        ClearScreen.wipe()
        print(
            "\nMAIN MENU\n"
            "+-------+\n\n"
            "[1] Manage NPC:s\n"
            "[2] Go to NPC action interface\n"
            "-----------------\n"
            "[0] Exit")

        userInput = input()
        if IsValidInput.forMenu(userInput, str.isdecimal, 2):
            menuSelect = int(userInput)
            if menuSelect == 1:
                AppMenus.ManageNPCs.goToManageNPCs()
            if menuSelect == 2:
                print()
            if menuSelect == 0:
                break
        else:
            print("\nYou entered an invalid command,\n"
                  "please choose between 0, 1, or 2.")
            time.sleep(3)
            continue
