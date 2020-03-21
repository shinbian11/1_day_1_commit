class Duck_Hunting:
    ducks = 13
    def hunting(self):
        print('Catch!')
        self.ducks -= 1

    def CheckDucks(self):
        if self.ducks <=0:
            print('Good Dog!')
        else:
            print(str(self.ducks)+ ' Ducks left')

dog1 = Duck_Hunting()
dog1.hunting()
dog1.CheckDucks()
dog2 = Duck_Hunting()
dog2.CheckDucks()