import ClearScreen
import time
import IsValidInput
from Models.NPCs import *


def addNPC():
    import main
    typeOfNPC = 0
    name = ""
    hitPoints = 0
    guardPoints = 0
    attackSkill = 0
    defenceSkill = 0
    armour = 0
    description = ""
    inputWeapon = {"name": "", "damage": ""}

    print("Add NPC\n"
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
    main.session.NPCList.append(npcInstance)
    for npc in main.session.NPCList:
        print(npc.name)

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

