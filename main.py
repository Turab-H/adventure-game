from room import Room

from character import Character, Enemy, Friend

from random import randint

from game_info import game_info

from item import item



football_house_game = game_info("football_house_game")

living_room = Room("Living Room")

kitchen = Room("Kitchen")

dining_room = Room("Dining Room")

list_of_rooms = [living_room, kitchen, dining_room]

dining_room.setDescription("A well lit room with a broad glass table.")

living_room.setDescription("A vast cozy room with a wall mounted TV and 4 sofas.")

kitchen.setDescription("A modern kitchen with spotless tiles to match.")


kitchen.link_room(dining_room, "south")

dining_room.link_room(kitchen, "north")
dining_room.link_room(living_room, "west")

living_room.link_room(dining_room, "east")



Cristiano = Friend("Cristiano", "Football player", "signed Portugal kit!")

Cristiano.set_conversation("Siuuuu")


Messi = Enemy("Messi", "Football Player")

Messi.set_weakness("Penalties")

Messi.set_conversation("Give me penalties")



current_room = kitchen

living_room.character = Cristiano

kitchen.character = Messi

sword = item("Penalties", "7 damage")

dining_room.item = sword

GameOn = True





backpack = []


football_house_game.welcome()

game_info.info()

print("\n\n\n\nThere are " + str(Room.number_of_rooms) + " rooms to explore.\n" )


while GameOn:

    if Enemy.enemies_defeated > 0:

        GameOn = False
        
        break

    current_room.get_details()

    character_present = current_room.character

    print("\n")
    user_cmmnd = input("What direction would you like to move in?")

    if user_cmmnd in ["north", "south", "east", "west"]:

        current_room = current_room.move(user_cmmnd)
    
    elif user_cmmnd == "talk":

        character_present.talk()

        if isinstance(character_present, Friend):

            giftOrHighFiveNum = randint(1, 10)

            if giftOrHighFiveNum == 10:

                character_present.gift_process()
            
            else:

                character_present.high_five()

    elif user_cmmnd == "fight":

        weapon = input("Choose your combat item.")

        if weapon in backpack:

            if character_present.fight(weapon) == False:

                GameOn = False

        else:

            print("You don't have that item in your backpack")


    elif user_cmmnd == "take":

        if current_room.item != None:

            backpack.append(current_room.item.item_name)
            
            current_room.item = None

        else:

            print("There aren't any iitems in this room.")



game_info.author = "Turab"

game_info.credits()
        