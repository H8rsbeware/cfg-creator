import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

HEADER = ("Verdana", 40)
SUBHEAD = ("Verdana", 25)
TEXT = ("Verdana", 18)

class tkApp(tk.CTk):
    def __init__(self, *args, **kwargs):

        tk.CTk.__init__(self, *args, **kwargs)
        mainFrame = tk.CTkFrame(self)
        mainFrame.pack(side="top", fill="both",expand=True)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        pages = (home, binds, viewmodel, hud, autoBuy, extras)
        for page in pages:
            frame = page(mainFrame, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.pushFrame(home)
    
    def pushFrame(self, content):
        frame = self.frames[content]
        frame.tkraise()



class home(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)

        pageName = tk.CTkLabel(self, text="Maker.cfg", font = HEADER)
        pageName.grid(row=0, column = 1, padx = 5, pady = 25)

        bindBtn = tk.CTkButton(self, text = "Binds", command = lambda : controller.pushFrame(binds), font = TEXT)
        viewBtn = tk.CTkButton(self, text = "View Model", command = lambda : controller.pushFrame(viewmodel), font = TEXT)
        hudBtn = tk.CTkButton(self, text = "HUD", command = lambda : controller.pushFrame(hud), font = TEXT)
        buyBtn = tk.CTkButton(self, text = "Auto Buy", command = lambda : controller.pushFrame(autoBuy), font = TEXT)
        xtraBtn = tk.CTkButton(self, text = "Extras", command = lambda : controller.pushFrame(extras), font = TEXT)
        bindBtn.grid(row=1, column=1, padx=50, pady=20, ipady=5, columnspan=2, sticky="nesw")
        viewBtn.grid(row=2, column=1, padx=50, pady=20, ipady=5, columnspan=2, sticky="nesw")
        hudBtn.grid(row=3, column=1, padx=50, pady=20, ipady=5, columnspan=2, sticky="nesw")
        buyBtn.grid(row=4, column=1, padx=50, pady=20, ipady=5, columnspan=2, sticky="nesw")
        xtraBtn.grid(row=5, column=1, padx=50, pady=20, ipady=5, columnspan=2, sticky="nesw")

       
        self.grid_columnconfigure(1, weight=1)
        


class cstmScrollFrame(tk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        canvas = tk.CTkCanvas(self , borderwidth=0, bg="grey13", highlightbackground="grey13")
        self.scrollFrame = tk.CTkFrame(canvas, border_width=0)
        scroll = tk.CTkScrollbar(self, command=canvas.yview)
        canvas.configure(yscrollcommand=scroll.set)

        self.scrollFrame.bind("<Configure>", lambda e : canvas.configure(scrollregion=canvas.bbox("all"), width=e.width))
        
        scroll.pack(side="right", fill="y", expand=False)
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0,0), window=self.scrollFrame, anchor="center")
        

class cstmBindSetting(tk.CTkFrame):
    
    def __init__(self, parent, name,*args, **kwargs):
        self.bind = tk.StringVar()
        super().__init__(parent, fg_color="grey13", corner_radius=0, *args, **kwargs)

        self.label = tk.CTkLabel(self, text = f"{name}\t", font = TEXT)
        self.entry = tk.CTkEntry(self, textvariable=self.bind)
        self.bind.trace("w", lambda *args : self.charLimit(self.bind))

        self.label.pack(side="left", padx=10, pady=5)
        self.entry.pack(side="right", padx=10, pady=5)
        
    # TODO : bind("<Key>", lambda e : checkKey(e, self.bind))  OR  just add options for those keys on right menu 
    # TODO : Allow any key on a key board to be clicked, but only store one
    
    def get(self):
        try:
            return str(self.entry.get())
        except ValueError:
            return None

    def charLimit(self, entry):
        val = entry.get()
        if len(val) > 1:
            val = ((entry.get()[-1]))
        entry.set(val.capitalize())
        
            

class binds(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        

    

        pageName = tk.CTkLabel(self, text="Maker.cfg Binds", font = SUBHEAD)
        pageName.grid(row=0, column = 0, padx = 10, pady = 10)

        returnBtn = tk.CTkButton(self, text = "Back", command = lambda : controller.pushFrame(home))
        returnBtn.grid(row=3, column=10, padx=10, pady=5, sticky="e")
        
        printBtn = tk.CTkButton(self, text = "Print", command = self.returnBinds)
        printBtn.grid(row=2, column=10, padx=10, pady=5, sticky="w")

        
        keyFrame = cstmScrollFrame(self)
        keyFrame.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nesw")



        self.fowardKey = cstmBindSetting(keyFrame.scrollFrame, "Foward").grid(row=1, sticky="nesw")
        self.backKey = cstmBindSetting(keyFrame.scrollFrame, "Backward").grid(row=2, sticky="nesw")
        self.leftKey = cstmBindSetting(keyFrame.scrollFrame, "Left").grid(row=3, sticky="nesw")
        self.rightKey = cstmBindSetting(keyFrame.scrollFrame, "Right").grid(row=4, sticky="nesw")

        self.heKey = cstmBindSetting(keyFrame.scrollFrame, "HE grenade").grid(row=5, sticky="nesw")
        self.mltvKey = cstmBindSetting(keyFrame.scrollFrame, "Incendiary").grid(row=6, sticky="nesw")
        self.fbKey = cstmBindSetting(keyFrame.scrollFrame, "Flashbang").grid(row=7, sticky="nesw") 
        self.dcyKey = cstmBindSetting(keyFrame.scrollFrame, "Decoy").grid(row=8, sticky="nesw")
        self.smkKey = cstmBindSetting(keyFrame.scrollFrame, "Smoke").grid(row=9, sticky="nesw")
        self.fakeKey  = cstmBindSetting(keyFrame.scrollFrame, "Fake nade").grid(row=10, sticky="nesw")

        self.plantKey = cstmBindSetting(keyFrame.scrollFrame, "Plant Bomb").grid(row=11, sticky="nesw")
        self.buyKey = cstmBindSetting(keyFrame.scrollFrame, "Buy Menu").grid(row=12, sticky="nesw")
        self.dropKey = cstmBindSetting(keyFrame.scrollFrame, "Drop").grid(row=13, sticky="nesw")
        self.useKey = cstmBindSetting(keyFrame.scrollFrame, "Defuse/Use").grid(row=14, sticky="nesw")
        self.swapKey = cstmBindSetting(keyFrame.scrollFrame, "Quick Switch").grid(row=11, sticky="nesw")

        
        
        # TODO : Create a dictonary to store binds 

        # TODO : Build the custom bind creator - Chain binds.

        bindFrame = cstmScrollFrame(self)
        bindFrame.grid(row=1, column=6, columnspan=5, padx=10, pady=10, sticky="nesw")
        

        self.grid_columnconfigure(1, weight=1)
        keyFrame.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def returnBinds(self):
          
        bindDict = {
            "movement": {
                "f": self.fowardKey,
                "b": self.backKey,
                "l": self.leftKey,
                "r": self.rightKey
            },
            "nades": {
                "he": self.heKey,
                "ml": self.mltvKey,
                "fb": self.fbKey,
                "dc": self.dcyKey,
                "sm": self.smkKey,
                "pt": self.fakeKey
            },
            "interaction": {
                "plt": self.plantKey,
                "buy": self.buyKey,
                "drp": self.dropKey,
                "use": self.useKey,
                "swp": self.swapKey
            }
        }
        print(bindDict)
        return bindDict



class viewmodel(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)

        pageName = tk.CTkLabel(self, text="Maker.cfg View Model", font = SUBHEAD)
        pageName.grid(row=0, column = 0, padx = 5, pady = 10)

        returnBtn = tk.CTkButton(self, text = "Back", command = lambda : controller.pushFrame(home))
        returnBtn.grid(row=0, column=1, sticky="e")

class hud(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)

        pageName = tk.CTkLabel(self, text="Maker.cfg HUD", font = HEADER)
        pageName.grid(row=0, column = 0, padx = 5, pady = 10)

        returnBtn = tk.CTkButton(self, text = "Back", command = lambda : controller.pushFrame(home))
        returnBtn.grid(row=1, column=1, sticky="s")

class autoBuy(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)

        pageName = tk.CTkLabel(self, text="Maker.cfg Auto Buy", font = HEADER)
        pageName.grid(row=0, column = 0, padx = 5, pady = 10)

        returnBtn = tk.CTkButton(self, text = "Back", command = lambda : controller.pushFrame(home))
        returnBtn.grid(row=1, column=1, sticky="s")

class extras(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)

        pageName = tk.CTkLabel(self, text="Maker.cfg Extras", font = HEADER)
        pageName.grid(row=0, column = 0, padx = 5, pady = 10)

        returnBtn = tk.CTkButton(self, text = "Back", command = lambda : controller.pushFrame(home))
        returnBtn.grid(row=1, column=1, sticky="s")



def main(args=None):
    app = tkApp()
    app.title('Maker.cfg')
    app.iconbitmap("./favicon.ico")
    app.minsize(620,500)
    app.mainloop()



if __name__ == "__main__":
    main()