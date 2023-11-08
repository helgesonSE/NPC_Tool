import copy
from datetime import time
import ClearScreen
from AppMenus import ActionInterface
from Data import session

def selectNPCs():
    session.NPCList.sort(key=lambda x: x.id)    # Sorts by id.
    session.actionInterfaceNPCs.clear()         # In case we go back here, the list is cleared and ready.
    foundNPC = False                            # actionInfaceNPCs contains copied NPCs for the action interface.

    while True:
        ClearScreen.wipe()
        print("Select NPCs for Action Interface\n"
              "+------------------------------+\n\n")
        for npc in session.NPCList:
            print(str(npc.id).rjust(3, ' ') + " " + npc.name)

        print("\nEnter ID of the NPC you want to add a copy of,"
              "or enter [0] to go back to main menu:\n")
        if len(session.actionInterfaceNPCs) > 0:
            print("\nThe following NPCs are selected for the action interface:\n")
            for npc in session.actionInterfaceNPCs:
                print(str(npc.id).rjust(3, ' ') + " " + npc.name)
            if len(session.actionInterfaceNPCs) == 9:   # For ease of use the list doesn't go double digits.
                print("\nThe list is full. Enter [9] to move ahead to the action interface.\n")
            else:
                print("\nKeep adding, or enter [9] to move ahead to the action interface.\n")

        index = 0
        userInput = input()

        if userInput == "0":
            break
        elif userInput == "9" and len(session.actionInterfaceNPCs) > 0:
            ActionInterface.goToActionInterface()
            break
        elif len(session.actionInterfaceNPCs) == 9: # A full list only allows the first two options.
            continue
        while index < len(session.NPCList): # Another linear search. May change further on.
            if session.NPCList[index].id == userInput:
                actionNPC = copy.deepcopy(session.NPCList[index])   # Makes a copy of the NPC for manipulation.
                session.actionInterfaceNPCs.append(actionNPC)
                foundNPC = True
                break
            index += 1
        if not foundNPC:
            print("\nNo such ID exists.\n")
            time.sleep(3)

