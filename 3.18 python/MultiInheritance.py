#다중 상속

class Amy():
    def print_last_name(self):
        print('Monkey')
class lex():
    def print_first_name(self):
        print('lex')

class AmyLex(Amy,lex): #Amy와 lex를 둘다 상속 받음!
    pass   #내용이 없을땐 pass 사용!

ax = AmyLex()
ax.print_first_name() #lex
ax.print_last_name()  #Monkey
