class item:

    def __init__(self, name, description) -> None:
        
        self._name = name
        self.description = description


    @property
    def item_name(self):
        return self._name
    
    @item_name.setter
    def name(self, new_name):

        self._name = new_name


    def get_description(self):

        return self.description
    
    def set_description(self, new_description):

        self.description = new_description



item1 = item("sword", "7 damage")

print(f"{item1.get_description} + {item1.item_name}")