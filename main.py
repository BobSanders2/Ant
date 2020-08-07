from Ant import Ant


class Mainloop(Ant):
    def __init(self):
        Ant.__init__(self)

    def mainloop(self):
        self.command = ""
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

        while self.command != "quit":
            if self.health <= 0:
                print("Ant has died.")
                break

            self.command = input(">>>")

            if self.command in self.commands_list:
                for values in self.commands_list:
                    if self.command == values:
                        self.commands_list[values]()
            else:
                print("That is not a command")

bob = Mainloop()
bob.mainloop()

