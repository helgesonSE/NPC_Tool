import ClearScreen
import time
import IsValidInput
import Models.NPCs
from Models.NPCs import *
from Data import session


def addNPC():
    typeOfNPC = 0
    name = ""
    hitPoints = 0
    guardPoints = 0
    attackSkill = 0
    defenceSkill = 0
    armour = 0
    description = ""
    inputWeapon = {"name": "", "damage": ""}

    ClearScreen.wipe()

    print("\nAdd NPC\n"
          "+-----+\n\n")

    while True:
        print("Select class of NPC - with a weapon or not.\n"
              "[1] Unarmed - [2] Armed\n")
        userInput = input()
        if IsValidInput.forMenu(userInput, str.isdecimal, 2):
            typeOfNPC = int(userInput)
            break
    print("Enter NPC name: ")
    name = input()
    print("Enter description: ")
    description = input()
    while True:
        print("Enter hit points (no-decimal number): ")
        userInput = input()
        if userInput.isdecimal():
            hitPoints = userInput
            break
    while True:
        print("Enter guard points (no-decimal number): ")
        userInput = input()
        if userInput.isdecimal():
            guardPoints = userInput
            break
    while True:
        print("Enter attack skill (no-decimal number): ")
        userInput = input()
        if userInput.isdecimal():
            attackSkill = userInput
            break
    while True:
        print("Enter defence skill (no-decimal number): ")
        userInput = input()
        if userInput.isdecimal():
            defenceSkill = userInput
            break
    while True:
        print("Enter armour rating (no-decimal number): ")
        userInput = input()
        if userInput.isdecimal():
            armour = userInput
            break
    if typeOfNPC == 2:
        print("Enter the name of a weapon: ")
        weaponName = input()
        while True:
            print("Enter the damage rating of the " + weaponName + " (no-decimal number): ")
            userInput = input()
            if userInput.isdecimal():
                weaponDamage = userInput
                inputWeapon = {"name": weaponName, "damage": weaponDamage}
                break
        npcInstance = ArmedNPC(
            BaseNPC.staticID,
            name,
            hitPoints,
            guardPoints,
            attackSkill,
            defenceSkill,
            armour,
            description,
            inputWeapon
        )
    else:
        npcInstance = BaseNPC(
            BaseNPC.staticID,
            name,
            hitPoints,
            guardPoints,
            attackSkill,
            defenceSkill,
            armour,
            description
        )
    Models.NPCs.BaseNPC.staticID += 1
    session.NPCList.append(npcInstance)

    # message to user, return to NPC management menu
    for npc in session.NPCList:
        print(str(npc.id).rjust(3, ' ') + " " + npc.name)


def editNPCs():
    #session.NPCList.sort(key=int(id))
    foundNPC = False

    while True:
        ClearScreen.wipe()
        print("Edit NPC\n"
              "+-----+\n\n")
        for npc in session.NPCList:
            print(str(npc.id).rjust(3, ' ') + " " + npc.name)

        print("\nEnter ID of the NPC you want to edit:\n")
        userInput = input()
        if not userInput.isdecimal():
            continue
        i = 0
        while (i < len(session.NPCList)):
            if session.NPCList[i].id == userInput:
                foundNPC = True
                break
            i += 1
        if not foundNPC:
            print("\nNo such ID exists.\n")
            time.sleep(3)
            break
        else:
            ClearScreen.wipe()
            print("Edit NPC\n"
                  "+-----+\n\n")

        session.NPCList[i].PrintValues(True)

        while True:
            print(f"\nSelect attribute to edit, enter [0] to go back: \n")
            userInput = input()
            if IsValidInput.forMenu(userInput, str.isdecimal, len(session.NPCList[i].NPCKeys)):
                menuSelect = int(userInput)
                if menuSelect == 0:
                    break
                else:
                    session.NPCList[i].NPCValues[menuSelect]
            else:
                print("\nYou entered an invalid command,\n"
                      f"please choose between 0 and {len(session.NPCList[i].NPCKeys)}.")
                time.sleep(3)
                continue



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
        if IsValidInput.forMenu(userInput, str.isdecimal, 2):
            menuSelect = int(userInput)

            if menuSelect == 1:
                addNPC()
                # goToManageNPCs()
            if menuSelect == 2:
                editNPCs()
                # editNPCs()
            if menuSelect == 0:
                break
        else:
            print("\nYou entered an invalid command,\n"
                  "please choose between 0, 1 and 2.")
            time.sleep(3)
            continue
