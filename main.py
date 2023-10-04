from AppMenus import Startup
from Models.NPCs import *
import os


def clear_screen():
    os.system('cls')


Bengt = UnarmedNPC(3, "Bengt", 20, 23,
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
clear_screen()

Startup.goToSplashScreen()
