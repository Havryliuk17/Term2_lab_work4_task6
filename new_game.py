'''Module for game'''
class Character:
    '''
    parent class for all characters
    '''
    def __init__(self, name, description) -> None:
        '''
        Inits class objects
        '''
        self.name = name
        self.description = description
        self.conversation = None
        self.chosen_fight = None
    def describe(self):
        '''
        Returns description of an enemy
        '''
        if self.name != None:
            vuvid = ''
            vuvid = vuvid + f'{self.name} is here !' + '\n'
            vuvid += f'{self.description}'
            print(vuvid)
    def set_conversation(self, phrase):
        '''
        Sets phrase for enemies conversation
        '''
        self.conversation = phrase
    
    def talk(self):
        '''
        Returns enemies phrase
        '''
        print(self.conversation)

class Enemy(Character):
    '''
    class for Enemies
    '''
    def __init__(self, name, description, defeat=[], weakness = None) -> None:
        '''
        inits class objects
        '''
        super().__init__(name, description)
        self.defeat = defeat
        self.weakness = weakness
    
    def __repr__(self) -> str:
        '''
        represent class objects
        '''
        return f'Enemy({self.name})'
    def set_weakness(self, weakness):
        '''
        Sets weakness for enemy
        '''
        self.weakness = weakness

    def fight(self, fight_with):
        self.chosen_fight = fight_with
        if self.weakness == self.chosen_fight:
            self.defeat.append(1)
            self.name = None
            return True
        return False
    
    def get_defeated(self):
        '''
        Counts number of defeated enemies 
        '''
        return len(self.defeat)
    
class Friend(Character):
    '''
    class for special characters that will help
    '''
    def __init__(self, name, description) -> None:
        '''
        inits class objects
        '''
        super().__init__(name, description)
    
    def __repr__(self) -> str:
        '''
        represent class objects
        '''
        return f'Friend({self.name}, {self.description})'
    
    def kill(self, enemy):
        '''
        kills enemies
        '''
        enemy.name = None
        return enemy.name


class Item:
    '''
    class for items
    '''
    def __init__(self, name, description = None) -> None:
        '''
        Inits class objects
        '''
        self.name= name
        self.description = description
    def set_description(self, description):
        '''
        Sets item's description
        '''
        self.description = description
    def __repr__(self) -> str:
        '''
        Represents class
        '''
        return f"Item('{self.name}')"
    def describe(self):
        '''
        Describes item
        '''
        vuvid = f'The [{self.name}] is here - {self.description}'
        print(vuvid)    
    def get_name(self):
        '''
        Returns item's name
        '''
        return self.name


class Building:
    '''
    Class for buildings, where player can hide
    '''
    def __init__(self, name) -> None:
        '''
        Inits class objects
        '''
        self.name = name

class Street:
    '''
    class for streets
    '''
    def __init__(self, street, description = None, enemy = None) -> None:
        '''
        Inits class objects
        '''
        self.street = street
        self.help = None
        self.item = None
        self.next_street = []
        self.to_go = []
        self.enemy = enemy
        self.description = description
        self.friend = None
    
    def set_friend(self, friend):
        self.friend = friend
    
    def __repr__(self) -> str:
        '''
        Represent class
        '''
        return f'Room("{self.street}")'
    def set_description(self, description):
        '''
        Returns description of the class
        '''
        self.description = description
    def set_character(self, monster):
        self.enemy = monster
    def link_room(self, to_go, to_turn)-> list:
        '''
        Returns list with available rooms to go
        '''
        self.next_street.append([self.street, to_go, to_turn])
        self.to_go = []
        for elem in self.next_street:
            if self.street in elem:
                self.to_go.append(elem[1:])

    def set_item(self, item):
        '''
        Sets available items for the room
        '''
        self.item = item

    def get_character(self):
        '''
        Returns enemie's name
        '''
        return self.enemy
    def get_item(self):
        '''
        Returns item's name
        '''
        return self.item
    
    def get_friend(self):
        '''
        returns friend's name
        '''
        return self.friend
    
    def move(self, command):
        '''
        Returns name of room to go
        '''
        for elem in self.to_go:
            if command in elem:
                return elem[0]
        return False

class Dvoryk(Street):
    '''
    special class for streets
    '''
    def __init__(self, street, building, description=None, enemy=None) -> None:
        '''
        Ints class objects
        '''
        super().__init__(street, description, enemy)
        self.building = building

    def get_details(self):
        '''
        Returns details of each room 
        '''
        vuvid = str(self.street) +'\n'
        vuvid += '----------------------------------------------------' +'\n'
        vuvid += vuvid+ str(self.description) + '\n'
        vuvid += f'There is {self.building.name}, you can hide there\n'
        if self.to_go != []:
            for elem in self.to_go[:-1]:
                vuvid += f'The {elem[0].street} is {elem[1]}' + '\n'
            vuvid += f'The {self.to_go[-1][0].street} is {self.to_go[-1][1]}'
        print(vuvid) 

    def hide(self):
        '''
        returns street that becomes current
        '''
        return self.to_go[0][0]

class Shosse(Street):
    '''
    Special class for streets
    '''
    def __init__(self, street, description=None, enemy=None) -> None:
        '''
        Inits class objects
        '''
        super().__init__(street, description, enemy)
    
    def get_details(self):
        '''
        Returns details of each room 
        '''
        vuvid = str(self.street) +'\n'
        vuvid += '----------------------------------------------------' +'\n'
        vuvid += vuvid+ str(self.description) + '\n'
        vuvid += 'There is a road, if you cross it you will go to another street\n'
        if self.to_go != []:
            for elem in self.to_go[:-1]:
                vuvid += f'The {elem[0].street} is {elem[1]}' + '\n'
            vuvid += f'The {self.to_go[-1][0].street} is {self.to_go[-1][1]}'
        print(vuvid) 

    def ride(self):
        '''
        returns street that become current
        '''
        return self.to_go[0][0]


hotel = Building('Hotel')
restaurant = Building("Restaurant")

kozelnutska = Dvoryk("kozelnutska", hotel)
kozelnutska.set_description("Quite, calm street with a lot of buildings")

stryuska = Shosse("stryuska")
stryuska.set_description("Busy street with a lot of cars.")

teatralna = Shosse("Teatralna")
teatralna.set_description("City center")

sadova = Dvoryk("Sadova", restaurant)
sadova.set_description("Quite street for IT guys")

kozelnutska.link_room(stryuska, "south")
stryuska.link_room(kozelnutska, "west")
stryuska.link_room(teatralna, "north")
teatralna.link_room(sadova, "east")
teatralna.link_room(stryuska, "south")
sadova.link_room(kozelnutska, 'east')

wizard = Enemy("Wizard", "man with a big glasses")
wizard.set_conversation("expecto patronum")
wizard.set_weakness("flowers")
kozelnutska.set_character(wizard)
doctor = Friend('Doctor', 'man with white gloves')
doctor.set_conversation("Just one small injection")
kozelnutska.set_friend(doctor)
stone = Item("stone")
stone.set_description("Really heavy stone'")
kozelnutska.set_item(stone)


actor = Enemy("Actor", "man with a red car")
actor.set_conversation("Sssss....I'm so bored...")
actor.set_weakness("book")
teatralna.set_character(actor)
fairy = Friend('Fairy', 'Woman with wings')
fairy.set_conversation("It is a wonderfull day")
teatralna.set_friend(fairy)
flowers = Item("flowers")
flowers.set_description("Amazing flowers")
teatralna.set_item(flowers)


clown = Enemy("Clown", "man with a red nose")
clown.set_conversation("I will tickle you")
clown.set_weakness("stone")
stryuska.set_character(clown)
princess = Friend('Princess', 'Girl with a crown')
princess.set_conversation("I love you")
stryuska.set_friend(princess)
book = Item("book")
book.set_description("Interesting book")
stryuska.set_item(book)

dragon = Enemy("Dragon", "big, green monster")
dragon.set_conversation("I will grill you")
dragon.set_weakness("dolls")
sadova.set_character(dragon)
dwarf = Friend('Dwarf', 'little and funny boy')
dwarf.set_conversation("Where is my gold")
sadova.set_friend(dwarf)
dolls = Item("dolls")
dolls.set_description("Pretty doll")
sadova.set_item(dolls)

current_street = kozelnutska
backpack = []

dead = False
live = 25
wallet = 25

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    

    item = current_street.get_item()
    if item is not None:
        item.describe()
    
    friend = current_street.get_friend()
    if friend is not None:
        friend.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direnction
        if current_street.move(command) != False:
            if current_street.move(command) == sadova:
                dead = True
                print("Congratulations! You won this game")
            current_street = current_street.move(command)

        else:
            print("Wrong direction")
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()

            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    print("Hooray, you won the fight!")
                    current_street.character = None
                    if inhabitant.get_defeated() == 3:
                        print("Congratulations, you have finished this game")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == 'help':
        print('Whom do you want to kill ?')
        kill = input()
        if kill == inhabitant.name:
            friend.kill(inhabitant)
            current_street.set_character(None)
        else:
            print("I can't help you")
    
    elif command == 'ride':
        if isinstance(current_street, Shosse) == True:
            current_street = current_street.ride()
            if wallet - 10 <=0:
                dead = True
                print('You are run out of money')
            wallet -=10
        else:
            print("You can't do this")

    elif command == 'hide':
        if isinstance(current_street, Dvoryk):
            current_street = current_street.hide()
            if live - 10 <=0:
                dead = True
                print('You are run out of live')
            live -=10
        else:
            print("You can't do this")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)