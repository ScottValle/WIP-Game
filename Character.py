import movement, Shop


class PlayerCharacter:
    def __init__(self):
        self.name = ''
        self.coins = 5
        self.hp = 0
        self.mp = 0
        self.status = []
        self.location = 'start'
        self.photo = '▼'


myPlayer = PlayerCharacter()
