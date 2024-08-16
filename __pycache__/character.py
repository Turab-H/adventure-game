class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    


class Enemy(Character):
    

    #The number of enemies defeated

    enemies_defeated = 0


    #Creating the enemy

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

        self.weakness = None


    #Setting and getting weaknesses of the enemy

    def set_weakness(self, weakness):
        
        self.weakness = weakness

    def get_weakness(self):

        return self.weakness
    

    # Fighting the enemy

    def fight(self, combat_item):

        if combat_item == self.weakness:

            print("You crush " + self.name + " with the " + combat_item + "!")

            Enemy.enemies_defeated += 1
        
            return True
        
        else:
            print(self.name + " crushed you!")
            return False


class Friend(Character):

    def __init__(self, char_name, char_description, gift):
        super().__init__(char_name, char_description)

        self.gift = gift


    #A friendly character can high five you using this method, or you're high fiving them.

    def high_five(self):

        print(f"{self.name} high fived you!")

    
    def set_gift(self, gift):

        self.gift = gift

    
    def gift_process(self):

        print(f"{self.name} gave you a {self.gift}!")
    
    
