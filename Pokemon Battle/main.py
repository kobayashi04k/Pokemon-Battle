import random
from function import *

# Class statement is used to store the data for the Pokemon's stats
# The Pokemon's Attack, Defense, HP, Speed, and Type are kept track of

class Pokemon_Stats():
    numPokemon = 0

    def __init__(self,name,HP,attack,defense,speed,type):
        Pokemon_Stats.numPokemon += 1
        self.name = name
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type = type

# The list of 18 digits numbers is used to determine damage modifiers (a.k.a Super, Not Very, No Effect, and Neutral Effect)
# Source: https://codegolf.stackexchange.com/questions/55823/its-super-effective

pokemonTypesModifier = [[2,2,2,2,2,1,2,0,1,2,2,2,2,2,2,2,2,2], # Normal 0
                        [4,2,1,1,2,4,1,0,4,2,2,2,2,1,4,2,4,1], # Fighting 1
                        [2,4,2,2,2,1,4,2,1,2,2,4,1,2,2,2,2,2], # Flying 2
                        [2,2,2,1,1,1,2,1,0,2,2,4,2,2,2,2,2,4], # Poison 3
                        [2,2,0,4,2,4,1,2,4,4,2,1,4,2,2,2,2,2], # Ground 4
                        [2,1,4,2,1,2,4,2,1,4,2,2,2,2,4,2,2,2], # Rock 5
                        [2,1,1,1,2,2,2,1,1,1,2,4,2,4,2,2,4,1], # Bug 6
                        [0,2,2,2,2,2,2,4,2,2,2,2,2,4,2,2,1,2], # Ghost 7
                        [2,2,2,2,2,4,2,2,1,1,1,2,1,2,4,2,2,4], # Steel 8
                        [2,2,2,2,2,1,4,2,4,1,1,4,2,2,4,1,2,2], # Fire 9
                        [2,2,2,2,4,4,2,2,2,4,1,1,2,2,2,1,2,2], # Water 10
                        [2,2,1,1,4,4,1,2,1,1,4,1,2,2,2,1,2,2], # Grass 11
                        [2,2,4,2,0,2,2,2,2,2,4,1,1,2,2,1,2,2], # Electric 12
                        [2,4,2,4,2,2,2,2,1,2,2,2,2,1,2,2,0,2], # Psychic 13
                        [2,2,4,2,4,2,2,2,1,1,1,4,2,2,1,4,2,2], # Ice 14
                        [2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,4,2,0], # Dragon 15
                        [2,1,2,2,2,2,2,4,2,2,2,2,2,4,2,2,1,1], # Dark 16
                        [2,4,2,1,2,2,2,2,1,1,2,2,2,2,2,4,4,2]] # Fairy 17

# Each Type has its own number labeled 0-17, which will be used later to determine damage modifiers
pokemonTypeNumbers = {"Normal":0,"Fighting":1,"Flying":2,"Poison":3,"Ground":4,"Rock":5,"Bug":6,"Ghost":7,"Steel":8,"Fire":9,"Water":10,"Grass":11,"Electric":12,"Psychic":13,"Ice":14,"Dragon":15,"Dark":16,"Fairy":17}


playerMaxHP = [50,80,55,70,60,90]
trainerMaxHP = [40,50,90,55,60,70]
# playerMovesDisplay and trainerMovesDisplay are only used to print out the player's choices for move
playerMovesDisplay = [["Tackle","Thundershock", "Agility", "Volt Tackle"], #Pikachu
                      ["Flamethrower","Wing Attack","Slash","Dragon Rage"], #Charizard
                      ["Gust","Confusion","Tackle","String Shot"], #Butterfree
                      ["Hydro Pump","Rapid Spin","Bite","Flash Cannon"], #Blastoise
                      ["Ice Beam","Agility","Aerial Ace","Steel Wing"], #Articuno
                      ["Psychic","Swift","Shadow Ball","Aura Sphere"]] #MewTwo

trainerMovesDisplay = [["Peck","Tackle","Gust","Quick Attack"], #Pidgey
                       ["Cut","Fury Cutter","Bug Bite","Air Cutter"], #Scyther
                       ["Body Slam","Dragon Breath","Ice Punch","Water Pulse"], #Dragonite
                       ["Thunderbolt","Mega Punch","Karate Chop","Fire Punch"], #Electabuzz
                       ["Earthquake","Double Kick","Megahorn","Poison Tail"], #Nidoking
                       ["Shadow Ball","Sludge Bomb","Dark Pulse","Thunderbolt"]] #Gengar


# playerMoves is a list of moves in which each dictionary is used to keep track of the moves' Name and Power
# The power of the moves is used to determine damage, and can be called with statements such as playerMoves['dictionaryIndex']['name of move']
playerMoves = [{"Tackle": 15,"Thundershock": 20, "Agility" : 2, "Volt Tackle": 25},
               {"Flamethrower":30,"Wing Attack":10,"Slash":15,"Dragon Rage":25},
               {"Gust":20,"Confusion":25,"Tackle":15,"String Shot":.75},
               {"Hydro Pump":40,"Rapid Spin":20,"Bite":25,"Flash Cannon":30},
               {"Ice Beam":35,"Agility":2,"Aerial Ace":25,"Steel Wing":20},
               {"Psychic":35,"Swift":20,"Shadow Ball":35,"Aura Sphere":30}]

trainerMoves = [{"Peck": 20,"Tackle": 15,"Gust":15,"Quick Attack":10},
                {"Cut":20,"Fury Cutter":15,"Bug Bite":20,"Air Cutter":20},
                {"Body Slam":25,"Dragon Breath":15,"Ice Punch":20,"Water Pulse":15},
                {"Thunderbolt":30,"Mega Punch":25,"Karate Chop":20,"Fire Punch":25},
                {"Earthquake":30,"Double Kick":15,"Megahorn":35,"Poison Tail":25},
                {"Shadow Ball":35,"Sludge Bomb":35,"Dark Pulse":35,"Thunderbolt":30}]


# Each Pokemon move has it owns typing labeled with a number. The value of each number can be figured out by using the list named "pokemonTypeNumbers"
playerMovesTypes = [{"Tackle": 0,"Thundershock": 12, "Agility" : 13, "Volt Tackle": 12},
                    {"Flamethrower":9,"Wing Attack":2,"Slash":0,"Dragon Rage":15},
                    {"Gust":2,"Confusion":13,"Tackle":0,"String Shot":6},
                    {"Hydro Pump": 10, "Rapid Spin": 0, "Bite": 16, "Flash Cannon": 8},
                    {"Ice Beam": 14, "Agility": 13, "Aerial Ace": 2, "Steel Wing": 8},
                    {"Psychic": 13, "Swift": 0, "Shadow Ball": 7, "Aura Sphere": 1}]

trainerMovesTypes = [{"Peck": 2,"Tackle": 0,"Gust":2,"Quick Attack":0},
                     {"Cut":0,"Fury Cutter":6,"Bug Bite":6,"Air Cutter":2},
                     {"Body Slam":0,"Dragon Breath":15,"Ice Punch":14,"Water Pulse":10},
                     {"Thunderbolt": 12, "Mega Punch": 0, "Karate Chop": 1, "Fire Punch": 9},
                     {"Earthquake": 4, "Double Kick": 1, "Megahorn": 6, "Poison Tail": 3},
                     {"Shadow Ball": 7, "Sludge Bomb": 3, "Dark Pulse": 16, "Thunderbolt": 12}]

# Two lists are used for Items
# itemsHeal is a dictionary where the Name of the Healing Item is matched with a Number representing how much it will Heal
# itemsAmount is a dictionary where the Name of the Healing Item is matched with a number representing Quantity
itemsHeal = {"Potions" : 20, "Super Potions" : 50}
itemsAmount = {"Potions" : 3, "Super Potions" : 1}

# The following lists are used to identify each Pokemon. This includes their names, stats, and typing
# The lists correspond with each other. Meaning, the First Index for all lists starting with "redPokemon" belong to "Pikachu", and so on
# Same for the Trainer's Team. The First Index for each List belongs to "Pidgey", and so on
redPokemonName = ["Pikachu","Charizard","Butterfree","Blastoise","Articuno","MewTwo"]
redPokemonTypes = ["Electric","Fire","Bug","Water","Ice","Psychic"]
redPokemonHP = [50,80,55,70,60,90]
redPokemonAttack = [20,35,20,30,55,100]
redPokemonDefense = [20,30,15,35,20,60]
redPokemonSpeed = [40,25,15,20,30,60]
redTeam = []
redNumPokemon = 6
trainerPokemonName = ["Pidgey","Scyther","Dragonite","Electabuzz","Nidoking","Gengar"]
trainerPokemonTypes = ["Flying","Bug","Dragon","Electric","Poison","Ghost"]
trainerPokemonHP = [40,50,90,55,60,70]
trainerPokemonAttack = [20,40,30,45,50,65]
trainerPokemonDefense = [15,20,50,40,30,45]
trainerPokemonSpeed = [30,45,20,25,20,80]
trainerTeam = []
trainerNumPokemon = 6
pokemonNumber = 0
trainerPokemonNum = 0

# The redAttack and trainerAttack boolean are used to keep track of if a player's turn occured. This was helpful for determining when a Battle Phase was over.
redAttack = False
trainerAttack = False

# Switch is a boolean used to determine if a Pokemon was switched out during Battle
switch = False


# The stats for the Pokemon are appended to the lists. redTeam is the Player's team, while trainerTeam is the Bot's.
for i in range(0,6):
    redTeam.append(Pokemon_Stats(redPokemonName[i],redPokemonHP[i],redPokemonAttack[i],redPokemonDefense[i],redPokemonSpeed[i],redPokemonTypes[i]))
    trainerTeam.append(Pokemon_Stats(trainerPokemonName[i], trainerPokemonHP[i], trainerPokemonAttack[i], trainerPokemonDefense[i],trainerPokemonSpeed[i],trainerPokemonTypes[i]))



print(trainerTeam[trainerPokemonNum].name,"HP:",trainerTeam[trainerPokemonNum].HP,"/",trainerMaxHP[trainerPokemonNum])
print(redTeam[pokemonNumber].name,"HP:",redTeam[pokemonNumber].HP,"/",playerMaxHP[pokemonNumber])



# A while loop is used so the Battle will continue to repeat until either the player's or the trainer's pokemon are all unable to battle
while trainerNumPokemon > 0 and redNumPokemon > 0:

    damageMod = 1

    print("What will Red do?")
    menuChoice = input("Fight | Pokemon | Items")
    # Fight is where the player chooses a Pokemon move to deal damage towards the opponent
    if menuChoice == "Fight":
        redAttack = False
        trainerAttack = False
        moveChoice = input(playerMovesDisplay[pokemonNumber])

        if redTeam[pokemonNumber].speed >= trainerTeam[trainerPokemonNum].speed:
            pturn = 0
        else:
            pturn = 1
        while redAttack == False or trainerAttack == False:

            if pturn == 0:
                if moveChoice in playerMoves[pokemonNumber]:
                    if moveChoice == "Agility":

                        redTeam[pokemonNumber].speed = agilityMove(redTeam[pokemonNumber].speed,playerMoves[pokemonNumber][moveChoice],redTeam[pokemonNumber].name)
                        redAttack = True
                        pturn = 1
                    elif moveChoice == "Volt Tackle":
                        damageMod = damageModifier(playerMovesTypes[pokemonNumber][moveChoice],pokemonTypeNumbers[trainerTeam[trainerPokemonNum].type],pokemonTypesModifier)
                        # If a pokemon uses a move of the same type as its actual type, then the damage of the move is multiplied by 1.5
                        if playerMovesTypes[pokemonNumber][moveChoice] == pokemonTypeNumbers[redTeam[pokemonNumber].type]:
                            stab = 1.5
                        else:
                            stab = 1
                        damage = round(((int(playerMoves[pokemonNumber][moveChoice]) * (redTeam[pokemonNumber].attack / trainerTeam[trainerPokemonNum].defense))* stab) * damageMod)



                        print(redTeam[pokemonNumber].name,"use",moveChoice,"!")
                        trainerTeam[trainerPokemonNum].HP -= damage
                        damageModifierText(damageMod)
                        redTeam[pokemonNumber].HP -= round(damage/2)
                        print("Pikachu has taken recoil damage")
                        if trainerTeam[trainerPokemonNum].HP <= 0:
                            trainerTeam[trainerPokemonNum].HP = 0
                            trainerNumPokemon -= 1
                            trainerAttack = True
                            if trainerNumPokemon > 0:
                                print(trainerTeam[trainerPokemonNum].name,"has fainted")
                                trainerPokemonNum += 1
                                print("Trainer Joey sent out",trainerTeam[trainerPokemonNum].name)
                            else:
                                print(trainerTeam[trainerPokemonNum].name, "has fainted")
                                print("Trainer Joey is out of usable Pokemon")

                        battleAftermathText(redTeam[pokemonNumber].name,redTeam[pokemonNumber].HP,playerMaxHP[pokemonNumber],trainerTeam[trainerPokemonNum].name,trainerTeam[trainerPokemonNum].HP,trainerMaxHP[trainerPokemonNum])
                        redAttack = True
                        pturn = 1
                    elif moveChoice == "String Shot":
                        trainerTeam[trainerPokemonNum].speed = trainerTeam[trainerPokemonNum].speed * playerMoves[pokemonNumber][moveChoice]
                        print(redTeam[pokemonNumber].name, "use String Shot")
                        print(trainerTeam[trainerPokemonNum].name,"'s speed was lowered")
                        redAttack = True
                        pturn = 1

                    else:

                        damageMod = damageModifier(playerMovesTypes[pokemonNumber][moveChoice],pokemonTypeNumbers[trainerTeam[trainerPokemonNum].type],pokemonTypesModifier)

                        if playerMovesTypes[pokemonNumber][moveChoice] == pokemonTypeNumbers[redTeam[pokemonNumber].type]:
                            stab = 1.5
                        else:
                            stab = 1

                        damage = round(((int(playerMoves[pokemonNumber][moveChoice]) * (redTeam[pokemonNumber].attack / trainerTeam[trainerPokemonNum].defense))* stab) * damageMod)

                        print(redTeam[pokemonNumber].name,"use",moveChoice,"!")
                        trainerTeam[trainerPokemonNum].HP -= damage
                        damageModifierText(damageMod)

                        if trainerTeam[trainerPokemonNum].HP <= 0:
                            trainerTeam[trainerPokemonNum].HP = 0
                            trainerNumPokemon -= 1
                            trainerAttack = True
                            if trainerNumPokemon > 0:

                                print(trainerTeam[trainerPokemonNum].name,"has fainted")
                                trainerPokemonNum += 1
                                print("Trainer Joey sent out",trainerTeam[trainerPokemonNum].name)

                            else:
                                print(trainerTeam[trainerPokemonNum].name, "has fainted")
                                print("Trainer Joey is out of usable Pokemon")


                        battleAftermathText(redTeam[pokemonNumber].name,redTeam[pokemonNumber].HP,playerMaxHP[pokemonNumber],trainerTeam[trainerPokemonNum].name,trainerTeam[trainerPokemonNum].HP,trainerMaxHP[trainerPokemonNum])

                        redAttack = True
                        pturn = 1

                else:
                    # If the player types an invalid move, then the code will run again
                    print("Invalid Move. Try Again.")
                    redAttack = True
                    trainerAttack = True

            elif pturn == 1:
                trainerChoiceRandom = random.randint(0,3)

                trainerChoice = trainerMovesDisplay[trainerPokemonNum][trainerChoiceRandom]

                damageMod = damageModifier(trainerMovesTypes[trainerPokemonNum][trainerChoice],
                                           pokemonTypeNumbers[redTeam[pokemonNumber].type],
                                           pokemonTypesModifier)

                if trainerMovesTypes[trainerPokemonNum][trainerChoice] == pokemonTypeNumbers[trainerTeam[trainerPokemonNum].type]:
                    stab = 1.5
                else:
                    stab = 1

                damage = round(((int(trainerMoves[trainerPokemonNum][trainerChoice])*(trainerTeam[trainerPokemonNum].attack/redTeam[pokemonNumber].defense)*stab)) * damageMod)

                print("Trainer's",trainerTeam[trainerPokemonNum].name,"used",trainerChoice,"!")
                redTeam[pokemonNumber].HP -= damage
                damageModifierText(damageMod)
                if redTeam[pokemonNumber].HP <= 0:
                    redTeam[pokemonNumber].HP = 0
                    print(redTeam[pokemonNumber].name,"has fainted")
                    redAttack = True


                    redNumPokemon -= 1
                    x = True
                    if redNumPokemon > 0:
                        # This segment is called when a Pokemon faints, so the player must choose a new Pokemon to send out
                        # x == True is used so the player has to choose a Pokemon that is Not Fainted.
                        while x == True:

                            print("Who will Red choose?")
                            pokemonSwitch = input("Pikachu | Charizard | Butterfree | Blastoise | Articuno | MewTwo")
                            x = pokemonXSwitch(pokemonSwitch, pokemonNumber, redTeam[0].HP, redTeam[1].HP,redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)
                            pokemonNumber = pokemonPokemonNumber(pokemonSwitch, pokemonNumber, redTeam[0].HP,redTeam[1].HP, redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)

                    else:
                        print("Red is out of usable Pokemon")

                battleAftermathText(redTeam[pokemonNumber].name, redTeam[pokemonNumber].HP, playerMaxHP[pokemonNumber],
                                    trainerTeam[trainerPokemonNum].name, trainerTeam[trainerPokemonNum].HP,
                                    trainerMaxHP[pokemonNumber])

                trainerAttack = True
                pturn = 0
    # Items allows for the trainer to heal their Pokemon using limited items. Note that using an item counts as a player's turn.
    elif menuChoice == "Items":

        print("Potions x" ,itemsAmount["Potions"], "| Super Potions x",itemsAmount["Super Potions"])
        itemChoice = input("What will Red use?")
        if itemChoice in itemsAmount:

            # If the player is about of the item that is chosen, the player will be unable to use it.
            if itemsAmount[itemChoice] == 0:
                print("You are out of",itemChoice)
            else:
                if redTeam[pokemonNumber].HP < playerMaxHP[pokemonNumber]:
                    itemsAmount[itemChoice] -= 1
                    redTeam[pokemonNumber].HP += itemsHeal[itemChoice]
                    if redTeam[pokemonNumber].HP > playerMaxHP[pokemonNumber]:
                        redTeam[pokemonNumber].HP = playerMaxHP[pokemonNumber]

                    print("Red used a",itemChoice)
                    battleAftermathText(redTeam[pokemonNumber].name, redTeam[pokemonNumber].HP,playerMaxHP[pokemonNumber],trainerTeam[trainerPokemonNum].name, trainerTeam[trainerPokemonNum].HP,trainerMaxHP[trainerPokemonNum])
                    trainerChoiceRandom = random.randint(0,3)
                    trainerChoice = trainerMovesDisplay[trainerPokemonNum][trainerChoiceRandom]

                    damageMod = damageModifier(trainerMovesTypes[trainerPokemonNum][trainerChoice],pokemonTypeNumbers[redTeam[pokemonNumber].type],pokemonTypesModifier)
                    if trainerMovesTypes[trainerPokemonNum][trainerChoice] == pokemonTypeNumbers[
                        trainerTeam[trainerPokemonNum].type]:
                        stab = 1.5
                    else:
                        stab = 1

                    damage = round(((int(trainerMoves[trainerPokemonNum][trainerChoice]) * (
                    trainerTeam[trainerPokemonNum].attack / redTeam[pokemonNumber].defense) * stab)) * damageMod)
                    damageModifierText(damageMod)
                    print("Trainer's", trainerTeam[trainerPokemonNum].name, "used", trainerChoice, "!")
                    redTeam[pokemonNumber].HP -= damage
                    damageModifierText(damageMod)
                    if redTeam[pokemonNumber].HP <= 0:
                        redTeam[pokemonNumber].HP = 0
                        print(redTeam[pokemonNumber].name, "has fainted")
                        redAttack = True

                        redNumPokemon -= 1
                        x = True
                        if redNumPokemon > 0:


                            while x == True:

                                print("Who will Red choose?")
                                pokemonSwitch = input("Pikachu | Charizard | Butterfree | Blastoise | Articuno | MewTwo")
                                x = pokemonXSwitch(pokemonSwitch, pokemonNumber, redTeam[0].HP, redTeam[1].HP,redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)
                                pokemonNumber = pokemonPokemonNumber(pokemonSwitch, pokemonNumber, redTeam[0].HP,redTeam[1].HP, redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)


                        else:
                            print("Red is out of usable Pokemon")

                    battleAftermathText(redTeam[pokemonNumber].name, redTeam[pokemonNumber].HP,
                                        playerMaxHP[pokemonNumber], trainerTeam[trainerPokemonNum].name,
                                        trainerTeam[trainerPokemonNum].HP, trainerMaxHP[pokemonNumber])

                    pturn = 0
                else:
                    print("It has no effect")


        else:
            print("Invalid Item. Try Again.")

    # Pokemon allows for the player to switch our his or her Pokemon during Battle. The player may not switch out to a Pokemon that is already in Battle or Fainted. Note that this option counts as the player's turn
    elif menuChoice == "Pokemon":
        pokemonSwitch = input("Pikachu | Charizard | Butterfree | Blastoise | Articuno | MewTwo")
        switch = pokemonMenuSwitch(pokemonSwitch,pokemonNumber,redTeam[0].HP,redTeam[1].HP,redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)
        pokemonNumber = pokemonPokemonNumber(pokemonSwitch,pokemonNumber,redTeam[0].HP,redTeam[1].HP,redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)

        if switch == True:
            # The trainer's choice of move is randomly chosen
            trainerChoiceRandom = random.randint(0, 3)
            trainerChoice = trainerMovesDisplay[trainerPokemonNum][trainerChoiceRandom]

            damageMod = damageModifier(trainerMovesTypes[trainerPokemonNum][trainerChoice],
                                       pokemonTypeNumbers[redTeam[pokemonNumber].type],
                                       pokemonTypesModifier)

            if trainerMovesTypes[trainerPokemonNum][trainerChoice] == pokemonTypeNumbers[
                trainerTeam[trainerPokemonNum].type]:
                stab = 1.5
            else:
                stab = 1

            damage = round(((int(trainerMoves[trainerPokemonNum][trainerChoice]) * (
            trainerTeam[trainerPokemonNum].attack / redTeam[pokemonNumber].defense) * stab)) * damageMod)

            print("Trainer's", trainerTeam[trainerPokemonNum].name, "used", trainerChoice, "!")
            redTeam[pokemonNumber].HP -= damage
            damageModifierText(damageMod)
            if redTeam[pokemonNumber].HP <= 0:
                redTeam[pokemonNumber].HP = 0
                print(redTeam[pokemonNumber].name, "has fainted")
                redAttack = True

                redNumPokemon -= 1
                x = True
                if redNumPokemon > 0:

                    while x == True:
                        print("Who will Red choose?")
                        pokemonSwitch = input("Pikachu | Charizard | Butterfree | Blastoise | Articuno | MewTwo")
                        x = pokemonXSwitch(pokemonSwitch,pokemonNumber,redTeam[0].HP,redTeam[1].HP,redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)
                        pokemonNumber = pokemonPokemonNumber(pokemonSwitch,pokemonNumber,redTeam[0].HP,redTeam[1].HP,redTeam[2].HP,redTeam[3].HP,redTeam[4].HP,redTeam[5].HP)
                else:
                    print("Red is out of usable Pokemon")
            battleAftermathText(redTeam[pokemonNumber].name, redTeam[pokemonNumber].HP, playerMaxHP[pokemonNumber],
                                trainerTeam[trainerPokemonNum].name, trainerTeam[trainerPokemonNum].HP,
                                trainerMaxHP[pokemonNumber])

            pturn = 0
            switch = False
        else:
            redAttack = True
            trainerAttack = True
if trainerNumPokemon == 0:
    print("Trainer Joey has lost")
elif redNumPokemon == 0:
    print("Red has lost")