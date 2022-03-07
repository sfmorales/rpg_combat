class Character:
    def __init__(self):
        self.health = 1000
        self.level = 1
        self.alive = True

    def attack(self, target):
        target.health -= 1
        target.dies()
    
    def dies(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
