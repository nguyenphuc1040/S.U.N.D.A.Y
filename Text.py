import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
AIsleep = "./UI/AIB.gif"
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.INi()
        self.animate(1) 
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def INi(self):
        self.canvas = tk.Canvas(width=350, height=348)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    (AIsleep)))]
        self.image = self.canvas.create_image(350/2,348/2, image=self.sequence[0])
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.master.after(45, lambda: self.animate((counter+1) % len(self.sequence)))
root = tk.Tk()
root.geometry("350x348+300+350")
app = Application(master=root)
app.mainloop()
print('A')