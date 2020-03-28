#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  #파이썬에서의 생성자 : __init__
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'\
              .format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit): # Unit클래스를 상속받는다.
    def __init__(self, name, hp, speed, damage):  #파이썬에서의 생성자 : __init__
        Unit.__init__(self, name, hp, speed) #Unit의 클래스를 싱속 받아서 초기화
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

#드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송하는 것 (공격은 불가)

#날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(\
            name, location, self.flying_speed))

#공중 공격 유닛 클래스
#다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    #AttackUnit과 Flyable 다중상속
    #다중상속 받는 두 메서드의 안에 있는 모든 것을 다 사용가능하다.
    def __init__(self, name, hp, damage, flying_speed): #멤버변수 초기화
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed는 0
        Flyable.__init__(self, flying_speed)

    def move(self,location): #Unit 클래스의 move()를 재정의
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

#서플라이 디폿 : 건물, 1개 건물 = 8만큼의 유닛을 생성 가능
supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

def game_start():
    print('새로운 게임을 시작합니다')
def game_over():
    pass
game_start()
game_over()
