
# This function returns the value for switch. If the player does switch, switch is True. Else, switch is False.
def pokemonMenuSwitch(switch,num,r1,r2,r3,r4,r5,r6):
    if switch == "Pikachu" and num != 0 and r1 > 0:
        print("Pikachu I choose you!")
        return True

    elif switch == "Charizard" and num != 1 and r2 > 0:

        print("Charizard I choose you!")
        return True
    elif switch == "Butterfree" and num != 2 and r3 > 0:

        print("Butterfree I choose you!")
        return True

    elif switch == "Blastoise" and num != 3 and r4 > 0:

        print("Blastoise I choose you!")
        return True
    elif switch == "Articuno" and num != 4 and r5 > 0:

        print("Articuno I choose you!")
        return True

    elif switch == "MewTwo" and num != 5 and r6 > 0:

        print("MewTwo I choose you!")
        return True

    else:

        print(switch, "is not available")
        return False

# This function is to determine which Pokemon is sent out. The numbers 0,1, and 2 represent indexes.
def pokemonPokemonNumber(switch,num,r1,r2,r3,r4,r5,r6):
    if switch == "Pikachu" and num != 0 and r1 > 0:
        return 0
    elif switch == "Charizard" and num != 1 and r2 > 0:
        return 1
    elif switch == "Butterfree" and num != 2 and r3 > 0:
        return 2
    elif switch == "Blastoise" and num != 3 and r4 > 0:
        return 3
    elif switch == "Articuno" and num != 4 and r5 > 0:
        return 4
    elif switch == "MewTwo" and num != 5 and r6 > 0:
        return 5


# This function is used when a Pokemon is fainted. Unlike the first one, the player has to switch in a Pokemon.
def pokemonXSwitch(switch,num,r1,r2,r3,r4,r5,r6):
    if switch == "Pikachu" and num != 0 and r1 > 0:
        print("Pikachu I choose you!")
        return False
    elif switch == "Charizard" and num != 1 and r2 > 0:
        print("Charizard I choose you!")
        return False
    elif switch == "Butterfree" and num != 2 and r3 > 0:
        print("Butterfree I choose you!")
        return False
    elif switch == "Blastoise" and num != 3 and r4 > 0:
        print("Blastoise I choose you!")
        return False
    elif switch == "Articuno" and num != 4 and r5 > 0:
        print("Articuno I choose you!")
        return False
    elif switch == "MewTwo" and num != 5 and r6 > 0:
        print("MewTwo I choose you!")
        return False

    else:

        print(switch, "is not available")
        return True


# This function is used to determine the damage modifier of a move. This number is multiplied with the actual damage.
# This is calculated by using the list of numbers representing types, the Pokemon's Type, and the Pokemon's Move's Type
# First, from the list of types, the list with the same number as the move's Type's number is selected
# Then, with the list, the index number in the list that is the same as the Pokemon's Type's Number is selected
# Finally, the number that is selected is divided 2 to obtain the damage modifier
def damageModifier(moveTypeNumber,pokemonTypeNumber,typeList):
    modList = typeList[moveTypeNumber]
    damageModi = modList[pokemonTypeNumber] / 2
    return damageModi


# This function prints out if the move was Super Effective, Not very effective, or had no effect
def damageModifierText(damageMod):
    if damageMod >= 2:
        print("It's Super Effective")
    elif damageMod == 0:
        print("It had no effect")
    elif damageMod == 0.5:
        print("It's not very effective")


# This function is used for the move agility, which doubles the speed of the user
def agilityMove(speed,move,name):
    speed = speed * move
    print(name, "use Agility")
    print(name, "'s speed rose sharply")
    return speed

# This function is called when the trainer's Pokemon faints. The program works so the trainer will send out the next Pokemon in his team
def trainerSendsOutPokemon(name,numberOfPokemon):
    print(name, "has fainted")

    numberOfPokemon -= 1

    print("Trainer Joey has sent out", name)

    return numberOfPokemon

# This function prints the Player's HP and Trainer's HP after one has taken damage
def battleAftermathText(redName,redHp,redMaxHp,trainerName,trainerHp,trainerMaxHp):
    print("-----------------------")
    print(trainerName, "HP:", trainerHp, "/",trainerMaxHp)
    print(redName, "HP:", redHp, "/", redMaxHp)





