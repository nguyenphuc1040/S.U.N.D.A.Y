
import tkinter
from PIL import Image, ImageTk, ImageSequence
import Sunday

AIsleep = "./UI/AIB.gif"

class App(tkinter.Frame):
    def __init__(self, parent=None):
       
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=350, height=348)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    (AIsleep)))]
        self.image = self.canvas.create_image(350/2,348/2, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(45, lambda: self.animate((counter+1) % len(self.sequence)))


AI = tkinter.Tk()

AI.geometry("350x348+300+350")
AI.resizable(0,0)
AI.overrideredirect(1)
AI.attributes("-alpha", 0.7)
app = App(AI)
AI.mainloop()
