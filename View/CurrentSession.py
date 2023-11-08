import json
from Models.NPCs import *
from Models.NPCs import NPC

class CurrentSession:

    def __init__(self):
        self.NPCList = self.loadNPCsToLists()
        self.actionInterfaceNPCs = []

    def loadNPCsToLists(self):
        jsonRead = open("Files/NPC_data.json", 'r', encoding='utf-8')
        jsonNPCs = json.load(jsonRead)
        jsonRead.close()

        _NPCList = []

        NPC.staticID = int(jsonNPCs["staticId"])

        for category, npc_list in jsonNPCs.items():
            for npc in npc_list:
                if category == "BaseNPC":   # Upon creation we make sure the incoming values are the correct type.
                    npcInstance = BaseNPC(  # Could use a failsafe. Also private variable signifiers are only used here.
                        npc['id'],
                        npc['name'],
                        int(npc['hitPoints']),
                        int(npc['guardPoints']),
                        int(npc['attackSkill']),
                        int(npc['defenceSkill']),
                        int(npc['armour']),
                        npc['description']
                        )
                elif category == "ArmedNPC":
                    npcInstance = ArmedNPC(
                        npc['id'],
                        npc['name'],
                        int(npc['hitPoints']),
                        int(npc['guardPoints']),
                        int(npc['attackSkill']),
                        int(npc['defenceSkill']),
                        int(npc['armour']),
                        npc['description'],
                        npc['weapon']
                    )
                else:
                    continue
                _NPCList.append(npcInstance)

        return _NPCList

    def writeNPCsToFile(self):  # We start with converting NPC objects into dicts.

        _baseNPCList = []
        _armedNPClist = []

        for npc in self.NPCList:
            npcDict = {
                "id": npc.id,
                "name": npc.name,
                "hitPoints": npc.hitPoints,
                "guardPoints": npc.guard,
                "attackSkill": npc.attackSkill,
                "defenceSkill": npc.defenceSkill,
                "armour": npc.armour,
                "description": npc.description
            }
            if isinstance(npc, ArmedNPC):
                npcDict["weapon"] = {"name": npc.weapon['name'], "damage": npc.weapon['damage']}
                _armedNPClist.append(npcDict)
            else:
                _baseNPCList.append(npcDict)

        npcData = {     # We make sure the structure yields the same result when written as a json.
            "staticId": str(NPC.staticID).rjust(4, '0'),
            "BaseNPC": _baseNPCList,
            "ArmedNPC": _armedNPClist
        }

        with open('Files/NPC_data_out.json', 'w', encoding='utf-8') as file:
            json.dump(npcData, file, ensure_ascii=False, indent=3)  # For testing purposes we write to a separate file.
