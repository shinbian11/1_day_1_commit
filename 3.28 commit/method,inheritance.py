#일반 유닛
class Unit:
    def __init__(self, name, hp):  #파이썬에서의 생성자 : __init__
        self.name = name
        self.hp = hp

#공격 유닛
class AttackUnit(Unit): # Unit클래스를 상속받는다.
    def __init__(self, name, hp, damage):  #파이썬에서의 생성자 : __init__
        Unit.__init__(self, name, hp) #Unit의 클래스를 싱속 받아서 초기화
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]\n'\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.\n'.format(self.name,self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

#메딕 : 의무병

#파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃',50,16)
firebat1.attack("5시")

#공격 2번 받았다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

#드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송하는 것 (공격은 불가)

#날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('\n{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(\
            name, location, self.flying_speed))

#공중 공격 유닛 클래스
#다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    #AttackUnit과 Flyable 다중상속
    #다중상속 받는 두 메서드의 안에 있는 모든 것을 다 사용가능하다.
    def __init__(self, name, hp, damage, flying_speed): #멤버변수 초기화
        AttackUnit.__init__(self, name,hp,damage)
        Flyable.__init__(self, flying_speed)

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.attack("3시")