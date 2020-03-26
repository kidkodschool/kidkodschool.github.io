character_class = ['pirate', 'mage', 'druid']
items = ['sword', 'staff', 'pistol', 'shield']
potion = ['health', 'mana']

def create_character(name, char_class, char_items, char_potions):
    return {name: {char_class: {'items': char_items, 'potions': char_potions}}}

character_name = input('Choose name of your character: ')

choose_class = input(f'Choose class of your character: {" ".join(character_class)} ')

if choose_class not in character_class:
    choose_class = input(f'Wrong choice, try again: {" ".join(character_class)} ')

choose_item = input(f'Choose item to take with you: {" ".join(items)} ')

if choose_item not in items:
    choose_item = input(f'Wrong choice, try again: {" ".join(items)} ')

choose_potion = input(f'Choose potion to take with you: {" ".join(potion)} ')

if choose_potion not in potion:
    choose_potion = input(f'Wrong choice, try again: {" ".join(potion)} ')


character = create_character(character_name, choose_class, choose_item, choose_potion)

print(f'Character created as dictionary {character}')


