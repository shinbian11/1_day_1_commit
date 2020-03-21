#상속

class Parent():
    def print_last_name(self):
        print('KingKong')
class Child(Parent):  #Parent 클래스의 print_last_name 메서드를 상속받음!
    def print_first_name(self):
        print('Amy')
    def print_last_name(self):  #print_last_name 재정의! (overriding)
        print('Monkey')

amy = Child()
amy.print_first_name()
amy.print_last_name()

