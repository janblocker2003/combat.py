#Angel Blocker
#TBC Project CompSci 120
#10/13/2025
#My Very Own combat.py

import tbc.py

def main():
    hero = Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    monster = Character("Monster", 20, 30, 5, 0)
    hero.printStats()
    monster.printStats()
    
    Character.fight(monster, hero)
    
if __name__ == "__main__":
    main()