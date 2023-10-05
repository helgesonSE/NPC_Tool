import ClearScreen
import time

import IsValidInput


def addNPC():
    print("Add NPC\n"
          "+-----+\n\n")

    while True:
        print("Select class of NPC - with a weapon or not.\n"
              "[1] Unarmed - [2] Armed\n")
        userInput = input()

def goToManageNPCs():

    while True:
        ClearScreen.wipe()
        print("\n"
              "NPC management\n"
              "+------------+\n\n"
              "[1] Add NPC\n"
              "[2] Edit NPC\n"
              "-----------\n"
              "[3] Return to main menu\n")

        userInput = input()
        if IsValidInput.forMenu(userInput, str.isdecimal, 3):
            menuSelect = int(userInput)

            if menuSelect == 1:
                addNPC()
                # goToManageNPCs()

            if menuSelect == 2:
                print()
                # goToSelectNPCsForAction

            if menuSelect == 3:
                break

        else:
            print("\nYou entered an invalid command,\n"
                  "please choose between 1 and 2.")
            time.sleep(3)
            continue

