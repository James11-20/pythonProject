class Character:
    def __int__(self):
        self.npc_type = 'monster'
        self.hp = 100
        self.weapon = 'sword'
        self.drop = 'red_gem'
        self.defence_factor = 0.345

    def take_damage(self,number):
        self.hp -= number

    def heal(self,number):
        self.hp += number
