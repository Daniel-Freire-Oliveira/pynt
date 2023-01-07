from tkinter import *
class Gui:
    exportColor = ()
    def __init__(self,master=None):
        self.titleContainer = Frame(master)
        self.titleContainer.pack()
        
        self.userContainer = Frame(master)
        self.userContainer.pack()
        
        self.finalContainer = Frame(master)
        self.finalContainer.pack()
        
        self.title = Label(self.titleContainer,text="Configs for pynt")
        self.title.pack()
        
        self.colorText = Label(self.userContainer,text="Set the Color in RGB, use commas ','")
        self.colorText.pack(side=LEFT)
        self.colorInput = Entry(self.userContainer)
        self.colorInput["width"] = 30
        self.colorInput.pack(side=LEFT)
        
        self.saveOptions = Button(self.finalContainer,text="Save")
        self.saveOptions["width"] = 12
        self.saveOptions["command"] = self.validateRgb
        self.saveOptions.pack()

    def validateRgb(self):
        colorRgb = self.colorInput.get()
        #file = open("./texture.py","w")
        #file.write(f"RGB = ({colorRgb})")
        import texture as tx
        tx.RGB = colorRgb
        self.title["text"]="value set now you can enjoy ._."
def init_gui():
    root = Tk()
    Gui(root)
    root.mainloop()
init_gui()