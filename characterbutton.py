from tkinter import *

class CharacterButton:

    def __init__(self, letter, index):
        self.letter = letter
        self.index = index
        self.state = False

    def button_click_on(self, index, result):

        if self.state is False:
            result[index] = 1
            print(result)
            self.state = True
            
        else:
            result[index] = 0
            print(result)
            self.state = False

    def button_creation(self, window, result):
        #return Button(self.window, self.letter, width=1, height=1, bg='white', command= lambda: self.button_click(self.index, result))
        return Button(window, text=self.letter, width=1, height=1, bg='white', command= lambda: self.button_click_on(self.index, result))