from AppMenus import StartMenu
from Models.NPCs import *
import ClearScreen

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

StartMenu.goToStartMenu()