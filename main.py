from AppMenus import StartMenu
from Models.NPCs import *
import ClearScreen
from View.CurrentSession import CurrentSession

Bengt = BaseNPC(3, "Bengt", 20, 23,
                70, 60,
                4, "Kraftig karl som knuffar dig med magen")

Ulfis = ArmedNPC(77, "Ulfis", 20, 20,
                 96, 20,
                 2, "Han är en barbar!", "Kniv")

print(Ulfis.defenceSkill)
print(Ulfis.weapon + "\n" + Ulfis.weapon)

print(Bengt.name)
print(Bengt.description)

# Call the function to clear the screen
ClearScreen.wipe()

# load json from file
session = CurrentSession()
# Testing to see that the NPC:s are loaded properly
for npc in session.NPCList:
    print(npc.name)
    if isinstance(npc, ArmedNPC):
        print(npc.weapon["name"] + "\n" + npc.weapon["damage"])

print("static ID: " + BaseNPC.staticID)

StartMenu.goToStartMenu()