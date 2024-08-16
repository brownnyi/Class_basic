class Maple:
    def __init__(self, nick, ability):
        self.nick = nick
        self.ability = ability
    
    def attack(self):
        self.damage = (self.ability[0] * 1 + self.ability[1]*0.8 + self.ability[2]*0.2 + self.ability[3]* 0.5) // 1
        print(f'{self.nick}이/가 기본공격으로 {self.damage}만큼의 데미지를 입혔습니다.')

#ability는 리스트로 저장을 하는데 리스트의 원소의 능력치 순서는 [STR, DEX, INT, LUK]순으로 저장을 한다.
character1 = Maple('여름',[4,4,12,4])
print(character1.nick)
print(character1.ability)

#RESULT
여름
[4,4,12,4]

character1.attack()

#RESULT
여름이/가 기본공격으로 11.0만큼의 데미지를 입혔습니다.
