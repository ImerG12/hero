import random

from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
           abilities: List
           armors: List
           name: String
           starting_health: Integer
           current_health: Integer
        '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health


    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner,
        #Hint: Look into random library, more specifically the choice method

    def add_ability(self, ability):
        ''' Add ability to abilities list
        '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
            '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
            '''

            # start our total out at 0
            total_damage = 0
            # loop through all of our hero's abilities
            for ability in self.abilities:
                # add the damage of each attack to our running total
                total_damage += ability.attack()
                # return the total damage
                return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self):
            '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
            '''
            # TODO: This method should run the block method on each armor in self.armors

            total_block = 0

            for armor in self.armor:

                total_block += armor.defend()

                return total_block

    def take_damage(self, damage):
           '''Updates self.current_health to reflect the damage minus the defense.
           '''
           # TODO: Create a method that updates self.current_health to the current
           # minus the the amount returned from calling self.defend(damage).

          





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
