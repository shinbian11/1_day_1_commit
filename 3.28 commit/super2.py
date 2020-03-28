class Unit:
    def __init__(self):
        print('Unit 생성자')
class Flyable:
    def __init__(self):
        print('Flyable 생성자')
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()

#다중상속을 할 때 super()를 사용하면 단 하나만 초기화가 가능!
#즉 다중상속을 할떄는 super()말고 각각 __init__함수 사용해서 초기화 하는걸 추천
