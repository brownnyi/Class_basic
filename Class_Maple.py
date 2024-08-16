class Maple:
    def __init__(self, nick, ability):
        self.nick = nick
        self.ability = ability
    
    def attack(self):
        self.damage = (self.ability[0] * 1 + self.ability[1]*0.8 + self.ability[2]*0.2 + self.ability[3]* 0.5) // 1
        print(f'{self.nick}이/가 기본공격으로 {self.damage}만큼의 데미지를 입혔습니다.')
