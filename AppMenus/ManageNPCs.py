import ClearScreen
import time


def goToManageNPCs():
    ClearScreen.wipe()

    while True:
        print("NPC management\n"
              "+------------+\n\n"
              "1. Add NPC\n"
              "2. Edit NPC\n"
              "-----------\n"
              "3. Return to main menu\n\n")

        userInput = input()
        if userInput.isdecimal():
            menuSelect = int(userInput)

            if menuSelect > 0 or menuSelect < 4:

                if menuSelect == 1:
                    print()
                    # goToManageNPCs()

                if menuSelect == 2:
                    print()
                    # goToSelectNPCsForAction

                if menuSelect == 3:
                    break

        else:
            print("\nYou entered an invalid command,\n"
                  "please choose between 1, 2, or 3.")
            time.sleep(3)
            continue