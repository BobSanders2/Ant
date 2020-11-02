class CommandManager():
    def __init__(self):
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

    def print_commands(self):
        for command in self.commands_list:
            print(command)

    def input(self, command):
