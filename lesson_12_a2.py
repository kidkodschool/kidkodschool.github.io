class Player:
    def attack(self):
        print(f'{self._class} attacks!')

class Barbarian(Player):
    def __init__(self, name):
        self._class = 'barbarian'
        self.name = name

class Mage(Player):
    def __init__(self, name):
        self._class = 'mage'
        self.name = name

barb_name = input('Your barbarian name: ')
mage_name = input('Your mage name: ')

barb = Barbarian(barb_name)
mage = Mage(mage_name)

game = True

while game:
    action = input('What character you choose to attack Mage or Barbarian: ').lower()
    if action == 'mage':
        mage.attack()
    elif action == 'barbarian':
        barb.attack()
    elif action == 'exit':
        game = False
    else:
        print('Try again or type exit to finish')


