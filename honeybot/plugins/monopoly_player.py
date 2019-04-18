#player class

class Player:

    def __init__(self,name):
        #name will be the nickname in the IRC server
        #pot is the amount of money the player starts with
        #portfolio is an array with the indexes of the user's properties from the board spaces dict
        self.name = name
        self.pot = 1500
        self.portfolio = []
        self.position = 1
        self.imprisoned = False
        self.prison_time = 0

    def update_position(self,amount):
        passed_go = False
        self.position += amount
        if self.position > 40:
            passed_go = True
            self.position -= 40
            self.increasePot(200)
        elif self.position == 40:
            passed_go = True
            self.increasePot(200)
        return passed_go

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getPot(self):
        return str(self.pot)

    def increasePot(self,amount):
        self.pot += amount

    def reducePot(self,amount):
        self.pot -= amount

    def getPortfolio:
        return self.portfolio

    def checkWon():
        pass
