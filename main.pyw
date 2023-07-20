from tkinter import *
from threading import Thread
from lector import *

root = Tk()
root.title("Python Nivel de Agua")
frame = Frame(root)
frame.pack(fill="both", expand="True")
frame.config(width="640", height="480")
reader = Loader(frame)
loaderThread = Thread(target=reader.read)
loaderThread.start()
root.mainloop()
reader.leave()