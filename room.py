class Room:

    number_of_rooms = 0

    def __init__(self, room_name):

        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self._item = None

        Room.number_of_rooms = Room.number_of_rooms + 1

    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description



    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name



    def describe(self):
        print(f"{self.name}:\n\n{self.description}")

    

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(f"{self.name} has the following linked rooms: {repr(self.linked_rooms)}")

    
    
    def get_details(self):
        
        print(f"The {self.name} \n _____________")
        print(f"{self.description} \n")
        for direction in self.linked_rooms:
            print(f"The {self.linked_rooms[direction].name} is {direction}\n")

        character_present = self.character

        if character_present != None:

            character_present.describe()
        

        if self._item == None:

            print("There are no items here.")

        else:

            print(f"In this room there is: {self._item.item_name}. Description: {self._item.get_description()}")
    

    
    def set_character(self, characterToBeSet):

        self.character = characterToBeSet
    
    def get_character(self):

        return self.character
    


    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, new_item):

        self._item = new_item




    def move(self, direction):

        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cant go that way.")
            return self