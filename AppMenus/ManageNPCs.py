import ClearScreen
import time
import IsValidInput
from Models.NPCs import *
from Data import session, Keys


def addNPC():
    newID = NPC.GetNewID()

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

    name = enterValueForNPC(Keys.Name)
    description = enterValueForNPC(Keys.Description)
    hitPoints = enterValueForNPC(Keys.HitPoints)
    guardPoints = enterValueForNPC(Keys.GuardPoints)
    attackSkill = enterValueForNPC(Keys.AttackSkill)
    defenceSkill = enterValueForNPC(Keys.DefenceSkill)
    armour = enterValueForNPC(Keys.Armour)
    if typeOfNPC == 2:
        inputWeapon = enterValueForNPC(Keys.Weapon)

        npcInstance = ArmedNPC(newID, name, hitPoints, guardPoints, attackSkill,
                               defenceSkill, armour, description, inputWeapon)
    else:
        npcInstance = BaseNPC(newID, name, hitPoints, guardPoints, attackSkill,
                              defenceSkill, armour, description)

    session.NPCList.append(npcInstance)

    print(f"NPC {npcInstance.name} with ID {npcInstance.id} added.")
    time.sleep(3)

def editNPCs():
    session.NPCList.sort(key=lambda x: x.id)
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
        while i < len(session.NPCList):
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
        while True:
            session.NPCList[i].PrintValues(True)

            print("\nSelect attribute to edit.\n"
                  "-------\n"
                  "[9] Delete NPC\n"
                  "[0] exit dialogue: \n")
            userInput = input()
            if userInput == "9" or IsValidInput.forMenu(userInput, str.isdecimal, len(session.NPCList[i].NPCKeys)):
                keySelect = int(userInput)

                if keySelect == 9:
                    print("\nNPC " + session.NPCList[i].name + " deleted.\n")
                    del session.NPCList[i]
                    time.sleep(3)
                    break
                elif keySelect == 0:
                    break
                else:
                    #keySelect -= 1
                    if keySelect == 8:
                        replacementWeapon = enterValueForNPC(Keys(keySelect))
                        session.NPCList[i].NPCValues[keySelect]["name"] = replacementWeapon["name"]
                        session.NPCList[i].NPCValues[keySelect]["damage"] = replacementWeapon["damage"]
                    else:
                        session.NPCList[i].NPCValues[keySelect] = enterValueForNPC(Keys(keySelect))
                        # while True:
                        #     print("Enter a new value for " + session.NPCList[i].NPCKeys[keySelect])
                        #     userInput = input()
                        #     if keySelect != (0 or 1):
                        #         session.NPCList[i].NPCValues[keySelect] = userInput
                        #         break
                        #     else:
                        #         if userInput.isdecimal():
                        #             session.NPCList[i].NPCValues[keySelect] = userInput
                        #             break
            else:
                print("\nYou entered an invalid command,\n"
                      f"please choose between 0 and {len(session.NPCList[i].NPCKeys)}.\n")
                time.sleep(3)
                continue
        break

def enterValueForNPC(key):
    returnValue = None
    if key == (Keys.Name or Keys.Description):
        print(f"Enter NPC {key.name}:")
        returnValue = input()
    elif key == Keys.Weapon:
        print("Enter the name of the NPC:s weapon: ")
        weaponName = input()
        while True:
            print("Enter the damage rating of the " + weaponName + " (no-decimal number): ")
            userInput = input()
            if userInput.isdecimal():
                weaponDamage = userInput
                break
        returnValue = {"name": weaponName, "damage": weaponDamage}
    else:
        print(f"Enter NPC {Keys(key).name} (no-decimal number): ")
        userInput = input()
        if userInput.isdecimal():
            returnValue = userInput
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
