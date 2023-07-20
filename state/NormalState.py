from .State import *

class NormalState():
    def drawPicture(self, frame):
        self.drawText(frame)
        
    def drawText(self, frame):
        self.width = frame.winfo_width()
        self.height = frame.winfo_height()
        self.aux = Image.open("I2.png").resize((self.width, self.height))
        self.imagen = ImageTk.PhotoImage(self.aux)
        Label(frame, image=self.imagen).place(x="0", y="0")