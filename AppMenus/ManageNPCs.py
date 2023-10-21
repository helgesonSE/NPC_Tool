import ClearScreen
import time
import ValidInput
from Models.NPCs import *
from Data import session, Attribute


def addNPC():
    newID = NPC.GetNewID()

    ClearScreen.wipe()
    print("\nAdd NPC\n"
          "+-----+\n\n")

    while True:
        print("Select class of NPC - with a weapon or not.\n"
              "[1] Unarmed - [2] Armed\n")
        userInput = input()
        if ValidInput.forMenu(userInput, str.isdecimal, 2):
            typeOfNPC = int(userInput)
            break
    # Each line goes to an input loop where we get the correct type of value from the user.
    name = enterValueForNPC(Attribute.Name)
    description = enterValueForNPC(Attribute.Description)
    hitPoints = enterValueForNPC(Attribute.HitPoints)
    guardPoints = enterValueForNPC(Attribute.GuardPoints)
    attackSkill = enterValueForNPC(Attribute.AttackSkill)
    defenceSkill = enterValueForNPC(Attribute.DefenceSkill)
    armour = enterValueForNPC(Attribute.Armour)
    if typeOfNPC == 2:  # A new NPC instance is created based on the entered values.
        inputWeapon = enterValueForNPC(Attribute.Weapon)

        npcInstance = ArmedNPC(newID, name, hitPoints, guardPoints, attackSkill,
                               defenceSkill, armour, description, inputWeapon)
    else:
        npcInstance = BaseNPC(newID, name, hitPoints, guardPoints, attackSkill,
                              defenceSkill, armour, description)

    session.NPCList.append(npcInstance)  # Adds the NPC to our list, for access.

    print(f"NPC {npcInstance.name} with ID {npcInstance.id} added.")
    time.sleep(3)


def editNPCs():
    session.NPCList.sort(key=lambda x: x.id)  # Sorts the list based on the id value.
    foundNPC = False

    while True:
        ClearScreen.wipe()
        print("Edit NPC\n"
              "+-----+\n\n")
        for npc in session.NPCList:
            print(str(npc.id).rjust(3, ' ') + " " + npc.name)

        print("\nEnter ID of the NPC you want to edit:\n")
        userInput = input()
        index = 0
        while index < len(session.NPCList):  # Linear search here for now. The list will likely never grow very large.
            if session.NPCList[index].id == userInput:
                foundNPC = True  # We found the NPC and can break from the loop.
                break
            index += 1
        if not foundNPC:
            print("\nNo such ID exists.\n")
            time.sleep(3)
            break
        else:
            ClearScreen.wipe()
            print("Edit NPC\n"
                  "+-----+\n\n")

        while True:
            session.NPCList[index].PrintValues(True)

            print("\nSelect attribute to edit.\n"
                  "-------\n"
                  "[9] Delete NPC\n"
                  "[0] exit dialogue: \n")

            userInput = input()
            if userInput == "9" or ValidInput.forMenu(userInput, str.isdecimal, #9 is an extra command here.
                                                      len(session.NPCList[index].NPCValues)):
                key = int(userInput)

                if key == 9:
                    print("\nNPC " + session.NPCList[index].name + " deleted.\n")
                    del session.NPCList[index]
                    time.sleep(3)
                    break
                elif key == 0:
                    break
                else:
                    session.NPCList[index].SetValue(key, enterValueForNPC(Attribute(key)))
            else:
                print("\nYou entered an invalid command,\n"
                      f"please choose between 0 and {len(session.NPCList[index].NPCValues)-1}, or 9.\n")
                time.sleep(3)
                continue
        break


def enterValueForNPC(key):  #Different dialogue and input checks based on what attribute is being changed.
    if key == Attribute.Name or key == Attribute.Description:
        print(f"Enter NPC {key.name}:")
        returnValue = input()
    elif key == Attribute.Weapon:
        print("Enter the name of the NPC:s weapon: ")
        weaponName = input()
        print("Enter the damage rating of the " + weaponName + " (no-decimal number): ")
        weaponDamage = ValidInput.forInt()
        returnValue = {"name": weaponName, "damage": weaponDamage}
    else:
        print(f"Enter NPC {Attribute(key).name} (no-decimal number): ")
        returnValue = ValidInput.forInt()
    return returnValue


def goToManageNPCs():
    while True:
        ClearScreen.wipe()
        print("\n"
              "NPC management\n"
              "+------------+\n\n"
              "[1] Add NPC\n"
              "[2] Edit NPC\n"
              "-----------\n"
              "[0] Return to main menu\n")

        userInput = input()
        if ValidInput.forMenu(userInput, str.isdecimal, 2):
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
