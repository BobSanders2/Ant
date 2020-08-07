from Ant import Ant

class Mainloop(Ant):
    def __init(self):
        Ant.__init__(self)
        self.command = ""

    def mainloop(self):
        print("""
        ===================================================
        ===================================================
        ===================================================
    
        Welcome to the Ant Game!
    
        ===================================================
        ===================================================
        ===================================================
    
        For a list of commands, type commands
    
        """)
        for values in self.commands_list:
            if self.command == values:
                self.commands_list[values]()

bob = Mainloop()
bob.mainloop()

