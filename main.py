import repetitive as r 
z = 1
while z == 1:
    z = 0
    print(" ")
    print("Instead of using yes or no, use y and n.".center(150))
    import random
    While_1 = 1
    print(" ")
    print("Welcome to Dungeoneer,".center(150))
    while While_1 == 1:
        While_1 = 0
        print(" ")
        print("Would you like to play?".center(150))
        While_2 = 1
        play = input(" ")
        while While_2 == 1:
            gc = 0 
            enemy = "sleeping"
            chest_1 = "unopened"
            chest_2 = "unopened"
            chest_3 = "unopened"
            chest_4 = "unopened"
            enemyl_1 = 15
            rats = 15
            While_3 = 0
            mlife = 15
            proficiency_1 = 0
            proficiency_2 = 0
            While_2 = 0
            text1_1 = 1
            text1_2 = 1
            text1_3 = 1
            text1_4 = 1
            text1_5 = 1
            While_5 = 0
            u1p = 1
            u2p = 1
            task = 0
            map1 = 0
            map2 = 0
            gh = 30
            gcamp = 0
            goblinchiefhead = 0
            reward = 0
            constantdamage = 0
            enemye = 0
            map3 = 0
            dodge = 0
            necromancerl_1 = 15
            nse = 0
            nseh = 0
            if play == "y":
                print("Ok then. lets get started.".center(150))
                print("What race would you like to be?".center(150))
                print ("Human(1), Elf(2), Dwarf(3), or Halfling(4)".center(150))
                race = input (" ")
                if race == "1" or "2" or "3" or "4":
                    print ("Ok then, what class would you like to be?".center(150))
                    print ("Mage(1), Ranger(2), Warrior(3), or Rogue(4)?".center(150))
                    Class = input (" ")
                    if race == "1":
                        race = "Human "
                        proficiency_1 = proficiency_1 + 1
                        proficiency_2 = proficiency_2 + 1
                        mlife = mlife + 1
                    if race == "2":
                        race = "Elven "
                        proficiency_2 = proficiency_2 + 2
                        mlife = mlife - 3
                    if race == "3":
                        race = "Dwarven  "
                        proficiency_1 = proficiency_1 + 2
                        mlife = mlife + 2
                    if race == "4":
                      race = "Halfling "
                      proficiency_1 = proficiency_1 + 1
                      proficiency_2 = proficiency_2 + 3
                      mlife = mlife - 1
                      dodge = dodge + 5
                    if Class == "1":
                        Class = "Mage?"
                    if Class == "2":
                        Class = "Ranger?"
                    if Class == "3":
                        Class = "Warrior?"
                    if Class == "4":
                        Class = "Rogue?"
                    if Class == "Mage?":
                        melee_attack = "summon an ethereal sword over your staff and stab your opponent with it(1)"
                        ranged_attack = "summon an ice shard to impale your opponent with?(2)"
                        weapon_melee =  "staff "
                        weapon_ranged = "magical tome "
                        proficiency_1 = proficiency_1 + 3
                        proficiency_2 = proficiency_2 + 3
                        mlife = mlife + 3
                    if Class == "Ranger?":
                        melee_attack = "grab a saxe knife off your belt to stab your opponent with(1)"
                        ranged_attack = "Shoot your opponent wih an arrow?(2)"
                        weapon_ranged = "bow "
                        weapon_melee = "saxe "
                        proficiency_1 = proficiency_1 + 2
                        proficiency_2 = proficiency_2 + 4
                        mlife = mlife + 2
                    if Class == "Warrior?":
                        melee_attack = "pull out your sword to attack your opponent with(1)"
                        ranged_attack = "throw a javelin at your opponent?(2)"
                        weapon_melee = "sword "
                        weapon_ranged = "javelin "
                        proficiency_1 = proficiency_1 + 4
                        proficiency_2 = proficiency_2 + 2
                        mlife = mlife + 1
                    if Class == "Rogue?":
                        melee_attack = "pull out dual daggers to stab your enemies with(1)"
                        ranged_attack = "shoot your enemies with your crossbow(2)"
                        weapon_melee =  "Dual Dagggers "
                        weapon_ranged = "crossbow "
                        proficiency_1 = proficiency_1 + 3
                        proficiency_2 = proficiency_2 + 5
                        mlife = mlife - 4
                        dodge = dodge + 10
                    life = mlife
                    print ("So you want to be a(n) ".center(150))
                    print (race.center(150))
                    print (Class.center(150))
                    character = input(" ")
                    if character == "y":
                        print ("In that case, you start outside a dungeon.".center(150))
                        print("A little backstory info is that you angered a tribe of goblins, and now they are chasing you.".center(150))
                        print("Something that I thought that I should mention.".center(150))
                        print ("Do you go inside?".center(150))
                        dungeon = input(" ")
                        if dungeon == "y":
                            print ("You walk inside the dungeon, and the goblins that were chasing you are too afraid to go inside.".center(150))
                            While_3 = 1
                        while While_3 == 1:
                            print ("Which direction do you go? Left(1), Forward(2), Right(3) or Outside(4)?".center(150))
                            While_3 = 0
                            direction_1 = input(" ")
                            if direction_1 == "1":
                                print ("You walk through the door on your left.".center(150))
                                if text1_2 == 1:
                                    text1_2 = 0
                                    print ("Before you walk in you see a troll sleeping on the floor.".center(150))
                                while enemyl_1 >= 1:
                                    if enemy == "drowzy":
                                        enemy = "awake"
                                    print("Do you".center(150))
                                    print(melee_attack.center(150))
                                    print("or, do you ".center(150))
                                    print(ranged_attack.center(150))
                                    attack = input(" ")
                                    if attack == "1":
                                        if Class == "Rogue?":
                                            poison = random.randint(1,10)
                                            if poison >= 9:
                                                print("As you attack your enemy, you poison them.".center(150))
                                                enemye = "constantdamage"
                                        if enemy == "awake":
                                            print ("You slash at the troll, hitting him for minor damage.".center(150))
                                            enemyl_1 = enemyl_1 - proficiency_1
                                        elif enemy == "sleeping":
                                            print("You silently walk over to the troll. You manage to get a good slash at him before he wakes.".center(150))
                                            enemy = "drowzy"
                                            proficiency_1 = proficiency_1 + 2
                                            enemyl_1 = enemyl_1 - proficiency_1
                                            proficiency_1 = proficiency_1 - 2
                                    elif attack == "2":
                                        chance = random.randint(1, 100)
                                        if chance >= 85:
                                            if Class == "Rogue?":
                                                poison = random.randint(1,10)
                                                if poison >= 9:
                                                    print("As you attack your enemy, you poison them.".center(150))
                                                    enemye = "constantdamage"
                                            if enemy == "awake":
                                                print ("You manage to hit the troll in the eye, killing him instantly.".center(150))
                                                enemyl_1 = 0
                                            if enemy == "sleeping":
                                                print("The troll roll's over in his sleep, allowing you to hit him in between the eye's, killing him instantly".center(150))
                                                enemyl_1 = 0
                                        elif chance >= 65:
                                            if Class == "Rogue?":
                                                poison = random.randint(1,10)
                                                if poison >= 9:
                                                    print("As you attack your enemy, you poison them.".center(150))
                                                    enemye = "constantdamage"
                                            if enemy == "awake":
                                                print ("You barely miss the troll's eye, hitting his cheek.".center(150))
                                                proficiency_2 = proficiency_2 + 2
                                                enemyl_1 = enemyl_1 - proficiency_2
                                                proficiency_2 = proficiency_2 - 2
                                            if enemy == "sleeping":
                                                print ("You barely miss the troll's eye and hit his face, and he wakes up(Obviously)".center(150))
                                                enemy = "drowzy"
                                                proficiency_2 = proficiency_2 + 2
                                                enemyl_1 = enemyl_1 - proficiency_2
                                                proficiency_2 = proficiency_2 - 2
                                        elif chance >= 26:
                                            if Class == "Rogue?":
                                                poison = random.randint(1,10)
                                                if poison >= 9:
                                                    print("As you attack your enemy, you poison them.".center(150))
                                                    enemye = "constantdamage"
                                            if enemy == "awake":
                                                print ("The troll almost dodges it, but you barely manage to hit him.".center(150))
                                                enemyl_1 = enemyl_1 - proficiency_2
                                            if enemy == "sleeping":
                                                print ("You almost miss, and end up hitting the troll in the side. He wakes up(Obviously).".center(150))
                                                enemy = "drowzy"
                                                proficiency_2 = proficiency_2
                                                enemyl_1 = enemyl_1 - proficiency_2
                                                proficiency_2 = proficiency_2
                                        elif chance <= 25:
                                            if enemy == "awake":
                                                print ("The troll easily dodges it.".center(150))
                                            elif enemy == "sleeping":
                                                print ("You barely miss the troll. He wakes at the sound.".center(150))
                                                enemy = "drowzy"
                                    if enemye == "constantdamage":
                                        enemyeh = random.randint(1,10)
                                        if enemyeh == 10:
                                            print("The enemy recovers from the poison.".center(150))
                                            enemye = 0
                                    if enemye == "constantdamage":
                                        enemyl_1 = enemyl_1 - 3
                                        print("The troll takes damage from the poison.".center(150))
                                    if enemy == "awake":    
                                        if enemyl_1 >= 1:
                                            enemya_1 = random.randint(1, 100)
                                            if enemya_1 - dodge >= 95:
                                                print("The troll is enraged, and uses all of his strength to attack you, and kills you instantly.".center(150))
                                                life = 0
                                            elif enemya_1 >= 80:
                                                print("The troll charges at you, and hits you in the chest, hurting you quite a bit.".center(150))
                                                life = life - 4
                                            elif enemya_1 - dodge >= 55:
                                                print("The troll attacks you, and he ends up only hitting your leg.".center(150))
                                                life = life - 2
                                            elif enemya_1 - dodge >= 26:
                                                print("The troll attacks you, and you almost dodge him, but he still managed to hit you.".center(150))
                                                life = life - 1
                                            else:
                                                print("The troll charges at you, but you easily sidestep him.".center(150))
                                            if life <= 0:
                                                print ("Looks like you died. Oh well.".center(150))
                                                print ("Do you wish to start over?".center(150))
                                                again = input(" ")
                                                if again == "y":
                                                    While_2 = 1
                                                    enemyl_1 = 0
                                    if  enemyl_1<= 0:
                                        print ("Good job. You killed the troll.".center(150))
                                        While_4 = 1
                                        while While_4 == 1:
                                            While_4 = 0
                                            print ("Do you want to continue to the next room(1), loot the dead troll(2) or go to the first room(3)".center(150))
                                            again_2 = input(" ")
                                            if again_2 == "1":
                                                print("You walk through the door in front of you.".center(150))
                                                if text1_3 == 1:
                                                    text1_3 = 0
                                                    print("As you walk through the door, you get ambushed by a swarm of rats.".center(150))
                                                    while rats >= 1:
                                                        if rats == 15:
                                                            rat1a = random.randint(1,100)
                                                            if rat1a - dodge >= 50:
                                                                print("One of the rats bites you.".center(150))
                                                                life = life - 1
                                                            elif rat1a - dodge <= 50: 
                                                                print("One of the rats attacks you, but misses".center(150))
                                                        if rats >= 12:
                                                            rat2a = random.randint(1,2)
                                                            if rat2a - dodge  >= 50:
                                                                print("One of the rats bites you.".center(150))
                                                                life = life - 1
                                                            elif rat2a - dodge  <= 50: 
                                                                print("One of the rats attacks you, but misses".center(150))
                                                        if rats >= 9:
                                                            rat3a = random.randint(1,2)
                                                            if rat3a - dodge  >= 50:
                                                                print("One of the rats bites you.".center(150))
                                                                life = life - 1
                                                            elif rat3a - dodge  <= 50: 
                                                                print("One of the rats attacks you, but misses".center(150))
                                                        if rats >= 6:
                                                            rat4a = random.randint(1,2)
                                                            if rat4a - dodge  >= 50:
                                                                print("One of the rats bites you.".center(150))
                                                                life = life - 1
                                                            elif rat4a - dodge  <= 50: 
                                                                print("One of the rats attacks you, but misses".center(150))
                                                        if rats >= 3:
                                                            rat5a = random.randint(1,2)
                                                            if rat5a - dodge  >= 50:
                                                                print("One of the rats bites you.".center(150))
                                                                life = life - 1
                                                            elif rat5a - dodge  <= 50: 
                                                                print("One of the rats attacks you, but misses".center(150))
                                                        if life >= 1:
                                                            print("What do you do?".center(150))
                                                            print("Do you".center(150))
                                                            print(melee_attack.center(150))
                                                            print("or, do you ".center(150))
                                                            print(ranged_attack.center(150))
                                                            attack = input(" ")
                                                            if attack == "1":
                                                                print("You cut one of the rats in half.".center(150))
                                                                rats = rats - 3
                                                            elif attack == "2":
                                                                attackattack = random.randint(1,10)
                                                                if attackattack == 10:
                                                                    print("You skewer two of the rats at once.".center(150))
                                                                    rats = rats - 6
                                                                elif attackattack <= 9:
                                                                    print("You skewer one of the rats.".center(150))
                                                                    rats = rats - 3
                                                        if life <= 0:
                                                            print("Looks like you died. Oh well.".center(150))
                                                            print("Do you wish to start over?".center(150))
                                                            again = input(" ")
                                                            if again == "y":
                                                                rats = 0 
                                                                While_2 = 1
                                                        elif rats <= 0:
                                                            print("You managed to kill the swarm of rats.".center(150))
                                                            print("What do you do now?".center(150))
                                                            exploring = 1
                                                            while exploring == 1:
                                                                exploring = 0
                                                                print("Do you explore the room(1), loot the rats(2), or go back a room(3)?".center(150))
                                                                explore = input(" ")
                                                                if explore == "1":
                                                                    print("As you explore the room you notice a skeleton next to a book in the corner. Do you read the book?".center(150))
                                                                    book = input("")
                                                                    if book == "y":
                                                                        print("You read the book, which turns out to be a diary. Apparently the person who wrote this book was in a situation simaller to yours.".center(150))
                                                                        print("In the book it says that he was being chased by a horde of goblins, and went inside to seak refuge.".center(150))
                                                                        print("He says that after spending some time inside the dungeon, he went to go check if the goblins left, and they did.".center(150))
                                                                        print("I wonder if our horde of goblins have left yet... ".center(150))
                                                                        input(" ")
                                                                        exploring = 1
                                                                    elif book == "n":
                                                                        print("You decide against reading the book. I would personally read it, but thats up to you.".center(150))
                                                                        exploring = 1
                                                                elif explore == "2":
                                                                    if chest_3 == "unopened":
                                                                        print("You cautiously walk over the the pile of dead rats, looking for gold.".center(150))
                                                                        print("You uncover 50 gold coins.".center(150))
                                                                        gc = gc + 50
                                                                        r.gold(gc)
                                                                        exploring = 1
                                                                        chest_3 = "a"
                                                                    elif chest_3 == "a":
                                                                        print("You search the pile of dead rats again, and find 10 more gold coins.".center(150))
                                                                        gc = gc + 10
                                                                        r.gold(gc)
                                                                        chest_3 = "opened"
                                                                        exploring = 1
                                                                    elif chest_3 == "opened":
                                                                        print("You alread looted these rats!".center(150))
                                                                        exploring = 1 
                                                                elif explore == "3":
                                                                    print("You decide to walk back into the troll room.".center(150))
                                                                    While_4 = 1 
                                            if again_2 == "3":
                                                print("You walk back into the main room.".center(150))
                                                While_3 = 1
                                            elif again_2 == "2":
                                                if chest_2 == "unopened":
                                                    print("You cautiously walk over to the dead troll, and search his dead body for gold. You find 50 gold coins.".center(150))
                                                    gc = gc + 50
                                                    chest_2 = "opened"
                                                    r.gold(gc)
                                                elif chest_2 == "opened":
                                                    print("You already looted this troll!".center(150))
                                                While_4 = 1
                            elif direction_1 == "2":
                                print("You are about to walk through the door straight ahead of you, when you see a necklace on a pedastal in the middle of the room.".center(150))
                                print("Do you continue into the room?".center(150))
                                traproom = 1
                                while traproom == 1: 
                                    Walk = input(" ")
                                    if Walk == "y":
                                        if text1_4 == 1:
                                            text1_4 = 0
                                            print("As you are about to walk into the room, you notice pressure plates on the floor.".center(150))
                                        elif text1_4 == 0: 
                                            print("As you walk into the room, you accidentally step on a pressure plate.".center(150))
                                            print("Hundreds of spikes come down from the ceiling, impaling you and killing you instantly.".center(150))
                                            print("I tried to warn you.".center(150))
                                            print("Do you wish to start over?".center(150))
                                            death = 1
                                            while death == 1:
                                                again = input(" ")
                                                if again == "y":
                                                    While_2 = 1
                                                    traproom = 0
                                                    death = 0
                                    elif Walk == "n":
                                        traproom = 0
                                        While_3 = 1
                                        if text1_4 == 1:
                                            print ("As you walk away from the room, you notice that there were pressure plates on the floor of that room.".center(150))
                                            print("Probably shouldn't go back there.".center(150))
                                        elif text1_4 == 0:
                                            print("I don't know why you went back into this room in the first place.".center(150))
                                        While_3 = 1
                            elif direction_1 == "3":
                                print("You walk through the door to the right of you.".center(150))
                                print("In the middle of the room there is a chest.".center(150))
                                print("Do you open the chest(1) or go to your last room(2)?".center(150))
                                Open = input(" ")
                                if Open == "1":
                                    if chest_1 == "unopened": 
                                        print("You open the chest, and in it you find 100 gold coins.".center(150))
                                        gc = gc + 100
                                        chest_1 = "opened"
                                        r.gold(gc)
                                    elif chest_1 == "opened":
                                        print("You already opened this chest!".center(150))
                                elif Open == "2":
                                    print("You decide against opening the chest, most likely thinking that the chest is really a mimic.".center(150))
                                print("You walk out of the chest room and into the main room.".center(150))
                                While_3 = 1
                            elif direction_1 == "4":
                                if enemyl_1 <= 0:
                                    if text1_1 == 1:
                                        text1_1 = 0
                                        print("While you were busy inside the dungeon, the goblins seem to have left.".center(150))
                                    print("You cautiously walk out of the dungeon into the forest that surrounds the dungeon.".center(150))
                                    forest = 1
                                    while forest == 1:
                                        forest = 0
                                        print("Do you want to try to travel to a town(1) or go back inside the dungeon(2)".center(150))
                                        town_1 = input(" ")
                                        if town_1 == "1":
                                            treasure_walk = random.randint(1,100)
                                            if chest_3 == "unopened":
                                                if treasure_walk == 10:
                                                    print("On your way to the town, you find a pile of 100 gold coins.".center(150))
                                                    gc = gc + 100
                                                    r.gold(gc)
                                                    chest_3 = "opened"
                                            print("You walk to the nearest town, which is named Riverrun.".center(150))
                                            print("This town has a blacksmith, where you can upgrade your weapons. They also have a tavern, where you can get new quests.".center(150))
                                            While_5 = 1
                                        while While_5 == 1:
                                            While_5 = 0
                                            if map1 == 1:
                                                print("Where would you like to go? Blacksmith(1), Tavern(2), the first Dungeon(3), or West(4)".center(150))
                                                building_choice = input(" ")
                                                if building_choice == "4":
                                                    print("You start walking toward the indicated point on the map.".center(150))
                                                    input(" ")
                                                    print("After a while, you find the camp that the goblins are staying in.".center(150))
                                                    print("Do you sneak in(1) or do you run in like a madman(2)?".center(150))
                                                    gcc = input(" ")
                                                    if gcc == "1":
                                                        print("You sneakily creep over to the goblin camp.".center(150))
                                                        print("You instantly kill one of the goblins before anyone know that you're there.".center(150))
                                                        gh = gh - 5
                                                        print("The goblin chief screams something, and the goblins start to run toward you.".center(150))
                                                    if gcc == "2":
                                                        print("You run into the camp screaming like a madman.".center(150))
                                                        print("The goblins look surprised, and the chief screams something.".center(150))
                                                        print("What do you do?".center(150))
                                                    while gh >= 1:
                                                        print("Do you".center(150))
                                                        print(melee_attack.center(150))
                                                        print("or, do you ".center(150))
                                                        print(ranged_attack.center(150))
                                                        attack = input(" ")
                                                        if attack == "1":
                                                            print("You slash at the horde of goblins.".center(150))
                                                            gh = gh - proficiency_1
                                                        elif attack == "2":
                                                            ragh = random.randint(1,10)
                                                            if ragh >= 9:
                                                                print("You shoot at the horde of goblins, and hit one in the face.".center(150))
                                                                proficiency_2 = proficiency_2 + 2
                                                                gh = gh - proficiency_2
                                                                proficiency_2 = proficiency_2 - 2
                                                            elif ragh >= 6:
                                                                print("You shoot at the horde of goblins, and hit a goblin.".center(150))
                                                                gh = gh - proficiency_2
                                                            elif ragh >=4:
                                                                print("You shoot at the horde of goblins, and barely hit a goblin.".center(150))
                                                                proficiency_2 = proficiency_2 - 2
                                                                gh = gh - proficiency_2
                                                                proficiency_2 = proficiency_2 + 2
                                                            elif ragh <= 3:
                                                                print("You shoot at the horde of goblins and barely miss.".center(150))
                                                        if gh >= 30:
                                                            gh1 = random.randint(1,6)
                                                            if gh1 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh1 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh1 <= 3:
                                                                    print("One of the goblins attack you, but miss.".center(150))
                                                        if gh >= 25:
                                                            gh2 = random.randint(1,6)
                                                            if gh2 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh2 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh2 <= 3:
                                                                print("One of the goblins attack you, but miss.".center(150))
                                                        if gh >= 20:
                                                            gh3 = random.randint(1,6)
                                                            if gh3 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh3 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh3 <= 3:
                                                                print("One of the goblins attack you, but miss.".center(150))
                                                        if gh >= 15:
                                                            gh4 = random.randint(1,6)
                                                            if gh4 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh4 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh4 <= 3:
                                                                print("One of the goblins attack you, but miss.".center(150))
                                                        if gh >= 10:
                                                            gh5 = random.randint(1,6)
                                                            if gh5 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh5 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh5 <= 3:
                                                                print("One of the goblins attack you, but miss.".center(150))
                                                        if gh >= 5:
                                                            gh6 = random.randint(1,6)
                                                            if gh6 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh6 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh6 <= 3:
                                                                print("One of the goblins attack you, but miss.".center(150))
                                                        if gh >= 1:
                                                            gh7 = random.randint(1,6)
                                                            if gh7 == 6:
                                                                print("One of the goblins slashes at you with their dagger.".center(150))
                                                                life = life - 3
                                                            elif gh7 >= 4:
                                                                print("One of the goblins kicks you.".center(150))
                                                                life = life - 1
                                                            elif gh7 <= 3:
                                                                print("One of the goblins attack you, but miss.".center(150))
                                                        if life <= 0:
                                                            print("Looks like you died.".center(150))
                                                            print("Do you wish to start over?".center(150))
                                                            again = input(" ")
                                                            if again == "y":
                                                                While_2 = 1
                                                                life = 1
                                                        elif gh <= 0:
                                                            print("Good job. You managed to kill all of the goblin grunts.".center(150))
                                                            print("You look at the goblin chief, and shoot him in the head.".center(150))
                                                            print("You then take the head to prove that you killed the chief.".center(150))
                                                            goblinchiefhead = "gained"
                                                            gcd = 1
                                                            while gcd == 1:
                                                                if text1_5 == 1:
                                                                    text1_5 = 0
                                                                    print("Do you go back to the town(1), or do you search the camp(2)?".center(150))
                                                                elif text1_5 == 0:
                                                                    print("Do you go back to the town(1)?".center(150))
                                                                cf = input(" ")
                                                                if cf == "1":
                                                                    print("You walk back to Riverrun.".center(150))
                                                                    gcd = 0
                                                                    While_3 = 1
                                                                    map1 = 0
                                                                if cf == "2":
                                                                    if u2p == 1:
                                                                        print("You look around the camp and you find a weapon.".center(150))
                                                                        print("You find a...".center(150))
                                                                        input(" ")
                                                                        print(weapon_ranged.center(150))
                                                                        u2p = u2p + 1 
                                                                        proficiency_1 = proficiency_1 + 1 
                                                                        gcamp = "looted"
                                                                    elif gcamp == 0:
                                                                        print("You search the camp and find 50 gold.".center(150))
                                                                        gc = gc + 50
                                                                        r.gold(gc)
                                            if map2 == 1:
                                                print("Where would you like to go? Blacksmith(1), Tavern(2), the first Dungeon(3), or East(4)?".center(150))
                                                building_choice = input(" ")
                                                if building_choice == "4":
                                                    print("You decide to walk to the indicated point on the map.")
                                                    input("")
                                                    print("You now stand in a field. What do you do?")
                                            if map3 == 1:
                                                print("Where would you like to go? Blacksmith(1), Tavern(2), the first Dungeon(3), or South(4)".center(150))
                                                building_choice = input(" ")
                                                if building_choice == "4":
                                                    print("You walk to the gates of the graveyard".center(150))
                                                    print("Do you go back to the town(1) or go into the graveyard(2)?".center(150))
                                                    walk = input(" ")
                                                    if walk == "2":
                                                        print("You walk in to the erie graveyard".center(150))
                                                        if Class == "Warrior?":
                                                            print("You think you see something in the shadows. So you pulled out your sword and ready your shield".center(150))
                                                        if Class == "Rogue?":
                                                            print("You reconize the form of a ememy and ready your dagger and crossbow".center(150))
                                                        if Class == "Mage?":
                                                            print("You sense something close. So you ready your staff and spells.".center(150))
                                                        if Class == "Ranger?":
                                                            print("You sense something ahead, and you nock your bow.")
                                                        print("Do you flee back to the town(1) or forage ahead(2)?".center(150))
                                                        forageahead = input(" ")
                                                        if forageahead == "2":
                                                            print("You forage ahead".center(150))
                                                            print ("And find a obelisk".center(150))
                                                            print("While examining the obelisk you see a necromancer!".center(150))
                                                            print("Do you (1)Charge at the Necromancer or (2)Crouch next to the obelisk to avoid detection?".center(150))
                                                            necromancer1 = input(" ")
                                                            if necromancer1 == "1":
                                                                necro = "surprised"
                                                                while necromancerl_1 >= 15:
                                                                    print("Do you".center(150))
                                                                    print(melee_attack.center(150))
                                                                    print("or, do you ".center(150))
                                                                    print(ranged_attack.center(150))
                                                                    attack = input(" ")
                                                                    necro = 2
                                                                    if attack == "1":
                                                                        if Class == "Rogue?":
                                                                            poison = random.randint(1,10)
                                                                            if poison >= 9:
                                                                                sne = "constantdamage"
                                                                        mattacknecro1 = random.randint(1,10)
                                                                        if mattacknecro1 >= 8:
                                                                            proficiency_1 = proficiency_1 - 1
                                                                            necromancerl_1 = necromancerl_1 - proficiency_1
                                                                            proficiency_1 = proficiency_1 + 1
                                                                            if Class == "Warrior?":
                                                                                print("You slash your sword at the necromancer dealing minor damage.".center(150))
                                                                            if Class == "Rogue?":
                                                                                print("You stab at the necromancer with your dagger dealing minor damage.".center(150)) # <------Minor dmg section
                                                                            if Class == "Mage?":
                                                                                print("You use your staff to hit the necromancer dealing minor damage".center(150))
                                                                            if Class == "Ranger?":
                                                                                print("You stab at the necromancer dealing minor damage.".center(150))
                                                                        elif mattacknecro1 >= 5:
                                                                            necromancerl_1 = necromancerl_1 - proficiency_1
                                                                            if Class == "Warrior?":
                                                                                print("You pierce the necromancer hitting a major artery".center(150))
                                                                            if Class == "Rogue?":
                                                                                print("You stab the necromancer in the stomach".center(150)) #<----------Medium dmg section
                                                                            if Class == "Mage?":
                                                                                print("You hit the necromancer".center(150))
                                                                            if Class == "ranger?":
                                                                                print("You stab the necromancer in the arm.".center(150))
                                                                        elif mattacknecro1 >= 3:
                                                                            proficiency_1 = proficiency_1 + 2
                                                                            necromancerl_1 = necromancerl_1 - proficiency_1
                                                                            proficiency_1 = proficiency_1 - 2
                                                                            if Class == "Warrior?":
                                                                                print("You slash across the necromancer's chest hitting the heart in the proccess, dealing major damage.".center(150))
                                                                            if Class == "Rogue?":
                                                                                print("You stab the necromancer in the eye, dealing major damage.".center(150))
                                                                            if Class == "Mage?":
                                                                                print("You hit the necromancer on the head, dealing major damage.".center(150))
                                                                            if Class == "Ranger?":
                                                                                print("You stab the necromancer's lungs, dealing major damage.".center(150))
                                                                            if mattacknecro1 >= 2: 
                                                                                print("You miss the necromancer completely.".center(150))
                                                                    if attack == "2":
                                                                        rattacknecro1 = random.randint(1,10)
                                                                        if rattacknecro1 >= 8:
                                                                            proficiency_2 = proficiency_2 - 1
                                                                            necromancerl_1 = necromancerl_1 - proficiency_2
                                                                            proficiency_2 = proficiency_2 + 1
                                                                            if Class == "Warrior?":
                                                                                print("You throw your javelin at the necromancer and almost miss.".center(150))
                                                                            if Class == "Rogue?":
                                                                                print("You shoot at the necromancer and almost miss.".center(150)) # <------Minor dmg section
                                                                            if Class == "Mage?":
                                                                                print("You shoot an ice shard at the necromancer, and almost miss.".center(150))
                                                                            if Class == "Ranger?":
                                                                                print("You shoot at the necromancer, and almost miss.".center(150))
                                                                        elif rattacknecro1 >= 5:
                                                                            necromancerl_1 = necromancerl_1 - proficiency_2
                                                                            if Class == "Warrior?":
                                                                                print("You throw your javelin at the necromancer and hit him.".center(150))
                                                                            if Class == "Rogue?":
                                                                                print("You shoot the necromancer.".center(150)) #<----------Medium dmg section
                                                                            if Class == "Mage?":
                                                                                print("You hit the necromancer with an ice shard.".center(150))
                                                                            if Class == "Ranger?":
                                                                                print("You shoot the necromancer with your bow.".center(150))
                                                                        elif rattacknecro1 >= 3:
                                                                            proficiency_2 = proficiency_2 + 2
                                                                            necromancerl_1 = necromancerl_1 - proficiency_2
                                                                            proficiency_2 = proficiency_2 - 2
                                                                            if Class == "Warrior?":
                                                                                print("You hit the necromancer near the heart, and deal major damage.".center(150)) 
                                                                            if Class == "Rogue?":
                                                                                print("You shoot at the necromancer and hit his face.".center(150))
                                                                            if Class == "Mage?":
                                                                                print("You hit the necromancer's face with an ice shard.".center(150))
                                                                            if Class == "Ranger?":
                                                                                print("You shoot and hit the necromancer's face.".center(150))
                                                                        elif rattacknecro1 <= 2: 
                                                                            print("You miss the necromancer completely.".center(150))
                                                                    if necromancerl_1 >= 1:
                                                                      if necro <= 1:
                                                                        necroa = random.randint(1,100)
                                                                        if necroa - dodge >= 81 :
                                                                          print("The necromancer stabs you in the chest, dealing major damage.")
                                                                          life = life - 6
                                                                        elif necroa - dodge <= 20 :
                                                                          print("The necromancer attacks you, but misses.")
                                                                        elif necroa <= 51:
                                                                          print("The necromancer stabs you.")
                                                                          life = life - 4
                                                                        elif necroa - dodge >= 21 :
                                                                          print("The necromancer stabbed you, dealing minor damage.")
                                                                          life = life - 2
                                                                    if necro == 2:
                                                                      print("The necromancer turns around surprised.")
                                                                      necro = 1
                                                                    if nse == "constantdamage":
                                                                      nseh = random.randint(1,5)
                                                                      if nseh == 5:
                                                                        print("The necromancer recovers from the poison.".center(150))
                                                                      elif nseh <= 4:
                                                                        print("The necromancer takes damage from the poison.".center(150))
                                                                        necromancerl_1 = necromancerl_1 - 3
                                                            if necromancer1 == "2":
                                                                print("Crouching next to the obelisk you see a few necromacncers chanting".center(150))
                                                                print("Do you go back for renforcements(1) or attack them head on(2)".center(150))
                                                                reinforce = input(" ")
                                                                if reinforce == "1":
                                                                    print("You decide to go back to town to get reinforcements.".center(150))
                                                        if forageahead == "1":
                                                            print("You flee back to the town.".center(150))
                                                            While_5 = 1
                                                    if walk == "1":
                                                        print("You decide to walk back to the town.".center(150))
                                                        While_5 = 1
                                            else:
                                                print("Where would you like to go? Blacksmith(1), Tavern(2), or back to the Dungeon(3)".center(150))
                                                building_choice = input(" ")
                                            if building_choice == "1":
                                                print("You walk into the Blacksmith.".center(150))
                                                print("You walk over to the blacksmith, and he looks up at you and asks,".center(150))
                                                print("What do you want?".center(150))
                                                building_1 = 1
                                                while building_1 == 1:
                                                    print("Do you ask to get a new weapon(1), ask to upgrade your weapon(2), or do you leave(3)?".center(150))
                                                    weapon_1 = input(" ")
                                                    if weapon_1 == "1":
                                                        print("Do you want a new melee weapon(1) or a new ranged weapon(2)?".center(150))
                                                        new_weapon = input(" ")
                                                        if new_weapon == "1":
                                                            print("A new ".center(150))
                                                            print (weapon_melee.center(150))
                                                            print("will cost you 200 gold coins. Do you want to buy it?".center(150))
                                                            buy_weapon = input(" ")
                                                            if buy_weapon == "y":
                                                                if gc >= 200:
                                                                    print("Ok".center(150))
                                                                    gc = gc - 200
                                                                    print("You now have ".center(150))
                                                                    print(str(gc).center(150))
                                                                    print("gold coins.".center(150))
                                                                    proficiency_1 = proficiency_1 + 1
                                                                    u1p = u1p + 1
                                                                elif gc <= 199:
                                                                    print("You don't have enough money to buy this!".center(150))
                                                                    building_1 = 1
                                                            elif buy_weapon == "n":
                                                                print("Ok then.".center(150))
                                                                building_1 = 1
                                                        elif new_weapon == "2":
                                                            print ("A new ".center(150))
                                                            print (weapon_ranged.center(150))
                                                            print ("Will cost you 200 gold coins. Do you want to buy it?".center(150))
                                                            buy_weapon = input(" ")
                                                            if buy_weapon == "y":
                                                                if gc >= 200:
                                                                    print ("Ok".center(150))
                                                                    gc = gc -200
                                                                    r.gold(gc)
                                                                    proficiency_2 = proficiency_2 + 1
                                                                    u2p = u2p + 1
                                                                elif gc <= 199:
                                                                    print("You don't have enough money to buy this!".center(150))
                                                                    building_1 = 1
                                                            elif buy_weapon == "n":
                                                                print("Ok then.".center(150))
                                                                building_1 = 1
                                                    elif weapon_1 == "2":
                                                        print("Which weapon do you want to upgrade? Melee(1) or Ranged(2)".center(150))
                                                        wc = input(" ")
                                                        if wc == "1":
                                                            print("Upgrading your weapon will cost 100 gold coins. Do you want to upgrade it?".center(150))
                                                            upgrade_weapon = input(" ")
                                                            if upgrade_weapon == "y":
                                                                if gc >= 100:
                                                                    print("Ok".center(150))
                                                                    gc = gc - 100
                                                                    r.gold(gc)
                                                                    proficiency_1 = proficiency_1 + u1p
                                                                elif gc <= 99:
                                                                    print("You don't have enough money for this!".center(150))
                                                        elif wc == "2":
                                                            print("Upgrading your weapon will cost 100 gold coins. Do you want to upgrade it?".center(150))
                                                            upgrade_weapon = input(" ")
                                                            if upgrade_weapon == "y":
                                                                if gc >= 100:
                                                                    print("Ok".center(150))
                                                                    gc = gc - 100
                                                                    r.gold(gc)
                                                                    proficiency_2 = proficiency_2 + u2p
                                                                elif gc <= 99:
                                                                    print("You don't have enough money for this!".center(150))
                                                    elif weapon_1 == "3":
                                                        print("Goodbye then.".center(150))
                                                        While_5 = 1
                                                        building_1 = 0
                                            if building_choice == "2":
                                                print("You walk into the tavern.".center(150))
                                                print("You walk up to the bartender.".center(150))
                                                building_2 = 1
                                                while building_2 == 1:
                                                    print("Do you ask him for food(1), ask about quests(2), or leave(3)?".center(150))
                                                    tc = input(" ")
                                                    if tc == "1":
                                                        print("The bartender says that a plateful of food will cost you 10 gold coins.".center(150))
                                                        print("Do you buy the food?".center(150))
                                                        buyfood = input(" ")
                                                        if buyfood =="y":
                                                            if gc >= 10:
                                                                print("Ok".center(150))
                                                                gc = gc - 10
                                                                r.gold(gc)
                                                                print("As you eat the food, you feel your wounds slowly heal.".center(150))
                                                                life = mlife
                                                            elif gc <= 49:
                                                                print("You don't have enough money for this!".center(150))
                                                        elif buyfood == "n":
                                                            print("Ok".center(150))
                                                    elif tc == "2":
                                                        if task == 0:
                                                            task = random.randint(1,1)
                                                            if task == 1:
                                                                print("Actually, I do.".center(150))
                                                                print("There is a goblin camp somewhere west of Riverrun. They are currently camping in a field.".center(150))
                                                                print("If you could kill the goblin leader, I would be willing to pay you 300 gold coins.".center(150))
                                                                print("Do you take the quest?".center(150))
                                                                goblinquest = input(" ")
                                                                if goblinquest == "y":
                                                                    print("The bartender gives you a map of where the goblin camp is.".center(150))
                                                                    map1 = 1
                                                                else:
                                                                    print("The bartender says that this is the only job that he has right now.".center(150))
                                                            if task == 2:
                                                                print("Actually, I do.".center(150))
                                                                print("People recently have been disapearing somewhere east of riverrun.".center(150))
                                                                print("If you could find the problem and fix it, I would be willing to pay you 300 gold coins.".center(150))
                                                                print("Do you take the quest?".center(150))
                                                                missingquest = input(" ")
                                                                if missingquest == "y":
                                                                    print("The bartender gives you a map of where the people have been dissapearing.".center(150))                                                            
                                                                    map2 = 1
                                                            if task == 3:
                                                                print("Actually, I do.".center(150))
                                                                print("There has been word of Necromancer's in the graveyard south of riverrun.".center(150))
                                                                print("If you could kill or ward off the Necromancer's, I would be willing to pay you 300 gold coins".center(150))
                                                                print("Do you take the quest?".center(150))
                                                                necromancerquest = input(" ")
                                                                if necromancerquest == "y":
                                                                    print("The bartender gives you a map with directions to the graveyard.".center(150))
                                                                    map3 = 1 
                                                        elif task == 1:
                                                            if map1 == 1:
                                                                if goblinchiefhead == "gained":
                                                                    if reward == 0:
                                                                        print("You actually did it! The bartender says.".center(150))
                                                                        print("Here is your reward, as promised. He gives you 300 gold coins".center(150))
                                                                        gc = gc + 300
                                                                        print("You now have ".center(150))
                                                                        print(str(gc).center(150))
                                                                        print("gold coins.".center(150))
                                                                        reward = "gained"
                                                                    elif reward == "gained":
                                                                        print("You already collected your reward!".center(150))
                                                                if goblinchiefhead == 0:
                                                                  print("Did you kill the goblin leader yet?".center(150))
                                                            if map1 == 0:
                                                                print("Do you want to take the quest now?".center(150))
                                                        elif task == 2:
                                                            if map2 == 0:
                                                                print("Do you want to take the quest now?".center(150))
                                                            elif map2 == 1:
                                                                print("Did you fix the issue yet?".center(150))
                                                        elif task == 3:
                                                            if map3 == 0:
                                                                print("Do you want to take the quest now?".center(150))
                                                                q3 = input(" ")
                                                                if q3 == "y":
                                                                    print("The bartender gives you a map with directions to the graveyard.".center(150))
                                                                    map3 = 1 
                                                    elif tc == "3":
                                                        print("The bartender says goodbye as you walk out of the tavern.".center(150))
                                                        building_2 = 0
                                                        While_5 = 1
                                            if building_choice == "3":
                                                print("You walk back toward the forest surrounding the dungeon.".center(150))
                                                forest = 1
                                            if building_choice == 5:
                                                print("You walk east of the town.".center(150))
                                        if town_1 == "2":
                                            print("You walk back into the dungeon.".center(150))
                                            While_3 = 1
                                elif enemyl_1 >= 1:
                                    print("You walk outside into the horde of goblins, and the one closest to you chops your head off.".center(150))
                                    print("Maybe you should wait a bit longer before you go outside...")
                                    print ("Do you wish to start over?".center(150))
                                    death = 1
                                    while death == 1:
                                        again = input(" ")
                                        if again == "y":
                                            While_2 = 1
                                            death = 0
                            else:
                                print("I'm afraid that isn't an option.")
                                While_3 = 1
                        if dungeon == "n":
                            print("You walk away from the dungeon into the horde of goblins that were chasing you.".center(150))
                            goblindeath = random.randint(1,10)
                            if goblindeath >= 1:
                                print("One of their shoots an arrow through your eye.".center(150))
                                life = 0
                                print("Do you wish to start over?".center(150))
                                while goblindeath == 1:
                                    again = input(" ")
                                    if again == "y":
                                        again = 0
                                        While_2 = 1
                                        goblindeath = 0
                    if character == "n":
                        While_2 = 1
            else:
                print ("Im afraid that wasn't an option.".center(150))
                While_1 = 1