import tkinter as tk
import Const
from trainingdataaccess import TrainingDataAccess


window = tk.Tk()
datagrabber = TrainingDataAccess()

title_label = tk.Label(text="Hello World lmao")
title_label.pack()


window.mainloop()