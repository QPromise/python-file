from abc import ABCMeta, abstractmethod

import random

class GuessGame(metaclass=ABCMeta):
    @abstractmethod
    def show(self, msg):
        pass

    @abstractmethod
    def user_input(self, prompt):
        pass

    def go(self):
        number = random.randint(0, 9)
        guess = -1
        while guess != number:
            guess = self.user_input('輸入數字：')

        self.show('猜中了！')

class ConsoleGame(GuessGame):
    def show(self, msg):
        print(msg)

    def user_input(self, prompt):
        return int(input(prompt))

game = ConsoleGame()
game.go()