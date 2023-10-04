from View.CurrentSession import CurrentSession

def goToSplashScreen():
    print("\t+-------------+\n"
          "\t|     ~~~     |\n"
          "\t| NPC MANAGER |\n"
          "\t|     ~~~     |\n"
          "\t+-------------+")

    print("Press enter to continue...")

    # load json from file
    session = CurrentSession()
    for npc in session.NPCList:
        print(npc.name)


    input()
