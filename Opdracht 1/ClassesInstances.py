class Gunman :

    _health = 100
    _bullets = 50

    def __init__(self, hp, ammo ):
        self._health = hp
        self._bullets = ammo

    def Test(self):
        print("Hallo")
        print("Aantal kogels is: ", self._bullets)

    
