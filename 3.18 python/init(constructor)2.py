class Dog:
    gender = 'female'
    def __init__(self,x):
        self.power = x
    def check_power(self):
        print(self.power, '입니다')

amy = Dog(15)   #x에 15 전달
lex = Dog(1)    #x에 1 전달

print(amy.gender)

amy.check_power()
lex.check_power()

