from Ant import Ant
from environment import Environment

class Mainloop(Ant, Environment):
    def __init__(self):
        Ant.__init__(self)
        Environment.__init__(self)
        self.commands_list = {
            "status": self.status,
            "location": self.location,
            "move fast": self.move_forward_fast,
            "move slow": self.move_forward_slow,
            "move back": self.move_backward,
            "turn left": self.turn_left,
            "turn right": self.turn_right,
            "rest": self.rest,
            "eat": self.eat,
            "commands": self.print_commands,
        }

        self.env = self.generate_env()

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
            if not self.ant_status['alive']:
                print("Ant has died.")
                break

            self.command = input(">>>")

            if self.command in self.commands_list:
                self.commands_list[self.command]()
            else:
                print("That is not a command")

    def print_commands(self):
        for command in self.commands_list:
            print(command)

game = Mainloop()
game.mainloop()

