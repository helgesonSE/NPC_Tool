import json
from Models.NPCs import *


class CurrentSession:
    def __init__(self):
        self.NPCList = self.loadNPCsToLists()


    def loadNPCsToLists(self):
        jsonRead = open('Files/NPC_list.json', 'r')
        jsonNPCs = json.load(jsonRead)
        jsonRead.close()
        print(jsonNPCs)

        _NPCList = []

        for category, npc_list in jsonNPCs.items():
            for npc in npc_list:
                if category == "UnarmedNPC":
                    npcInstance = UnarmedNPC(
                        npc['id'],
                        npc['name'],
                        npc['hitPoints'],
                        npc['guard'],
                        npc['attackSkill'],
                        npc['defenceSkill'],
                        npc['armour'],
                        npc['description']
                        )
                else:
                    npcInstance = ArmedNPC(
                        npc['id'],
                        npc['name'],
                        npc['hitPoints'],
                        npc['guard'],
                        npc['attackSkill'],
                        npc['defenceSkill'],
                        npc['armour'],
                        npc['description'],
                        npc['weapon']
                    )
                _NPCList.append(npcInstance)

        return _NPCList
