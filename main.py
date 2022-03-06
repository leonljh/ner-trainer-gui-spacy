from tkinter import *
from turtle import onclick

from pandas import array 
import Const
from characterbutton import CharacterButton
from trainingdataaccess import *


window = Tk()
datagrabber = TrainingDataAccess()
window.geometry("1000x800")
test = 'Apple is looking at buying U.S. startup for $6 million testing 123123'

r = 0
c = 0
array_result = [0] * len(test)

def print_result():
    print(array_result)

width =  40 #geometry / button width

letter_index = 0

for b in range(len(test)):
    b = CharacterButton(test[letter_index], letter_index)
    b = b.button_creation(window, array_result)
    letter_index += 1
    
    b.grid(row=r, column=c, sticky=N+S+E+W)
    c+=1
    if c ==width:
        r+=1
        c=0

end_button = Button(window, text="See Output", width=5,height=1, bg="green", command=print_result)
end_button.grid(row=10, column= 10,sticky=N+S+E+W)


#example dataset: ('I like London and Berlin.', {'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]})
#tuple0 = text, tuple1 = dictionary { "entities" : [list0 = index, grp]}

window.mainloop()