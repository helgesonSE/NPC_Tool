import time
import ClearScreen
from AppMenus import *
from Models.NPCs import *
from View.CurrentSession import CurrentSession

def goToStartMenu():
    print("\n"
          "\t+-------------+\n"
          "\t|     ~~~     |\n"
          "\t| NPC MANAGER |\n"
          "\t|     ~~~     |\n"
          "\t+-------------+")

    print("Press enter to continue...")

    # load json from file
    session = CurrentSession()
    # Testing to see that the NPC:s are loaded properly
    for npc in session.NPCList:
        print(npc.name)
        if isinstance(npc, ArmedNPC):
            print(npc.weapon["name"] + "\n" + npc.weapon["damage"])

    input()
    ClearScreen.wipe()

    while True:
        print(
            "\nMAIN MENU\n"
            "+-------+\n\n"
            "1. Manage NPC:s\n"
            "2. Go to NPC action interface\n"
            "-----------------\n"
            "3. Exit")

        userInput = input()
        if userInput.isdecimal():
            menuSelect = int(userInput)

            if menuSelect > 0 or menuSelect < 4:

                if menuSelect == 1:

                    print()
                    #goToManageNPCs()

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
