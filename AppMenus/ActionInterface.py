import time
import ClearScreen
import ValidInput
from Data import session

def goToActionInterface():

    while True:
        index = 0
        while index < len(session.actionInterfaceNPCs):
            print(f"\n[{index + 1}]\n")  #Prints our picked NPCs along with a number which is used to select one after this.
            session.actionInterfaceNPCs[index].PrintValues(False)
            index += 1

        print("\n\nSelect NPC [#] for actions, or enter [0] to go back to previous menu.\n")

        select = input()
        if ValidInput.forMenu(select, str.isdecimal, len(session.actionInterfaceNPCs)):
            select = int(select)
            if select == 0:
                break
            else:
                while True:
                    ClearScreen.wipe()
                    session.actionInterfaceNPCs[select-1].PrintValues(False)

                    print("\n\nSelect action: \n")
                    print("[1] Attack\n"
                          "[2] Take damage\n"
                          "------------\n"
                          "[0] Go back\n")

                    selectAction = input()
                    if ValidInput.forMenu(selectAction, str.isdecimal, 2):
                        selectAction = int(selectAction)
                        if selectAction == 0:
                            break
                        elif selectAction == 1:
                            print("\n\nEnter opposing defence roll (no-decimal number, 0-99):\n")
                            opposeRoll = ValidInput.forInt()
                            session.actionInterfaceNPCs[select - 1].Attack(opposeRoll)  #Stat manipulation made in-class.
                        elif selectAction == 2:
                            print("\n\nEnter attack roll (0-99):\n")
                            opposeRoll = ValidInput.forInt()
                            print("\n\nEnter damage roll (no-decimal number): :\n")
                            incomingDamage = ValidInput.forInt()
                            session.actionInterfaceNPCs[select - 1].Defend(opposeRoll, incomingDamage)

                    else:
                        print("\nYou entered an invalid command,\n"
                              "please choose between 0, 1, or 2.\n")
                    time.sleep(2)
