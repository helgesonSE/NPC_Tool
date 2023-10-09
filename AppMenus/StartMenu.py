import time
import ClearScreen
import IsValidInput
from AppMenus.ManageNPCs import goToManageNPCs
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
            "[3] Exit")

        userInput = input()
        if IsValidInput.forMenu(userInput, str.isdecimal, 3):
            menuSelect = int(userInput)
            if menuSelect == 1:
                goToManageNPCs()
            if menuSelect == 2:
                print()
                #goToSelectNPCsForAction
            if menuSelect == 3:
                break
        else:
            print("\nYou entered an invalid command,\n"
                  "please choose between 1, 2, or 3.")
            time.sleep(3)
            continue
