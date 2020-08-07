import os
import itertools
import time
from collections import defaultdict
class Ant():
    def __init__(self):
        # self.head_attached = True
        # self.torso_attached = True
        # self.end_attached = True
        # self.leg1_attached = True
        # self.leg2_attached = True
        # self.leg3_attached = True
        # self.leg4_attached = True
        # self.leg5_attached = True
        # self.leg6_attached = True
        # self.left_antenna_attached = True
        # self.right_antenna_attached = True
        # self.weight_milligram = 3
        # self.color = "Red"
        # self.awake = True
        self.alive = False
        self.hungry_meter = 0
        self.health = 100
        # self.working_strength = 100
        self.endurance = 0
        self.x = 0
        self.y = 0
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
        self.current_direction = "north"

    def print_commands(self):
        for command in self.commands_list:
            print(command)

    def hunger_check(self):
        if 10 < self.hungry_meter <= 30 and not alert1:
            print("""

            Ant is getting hungry

            """)
            alert1 = True
        elif 40 <= self.hungry_meter <= 60 and alert1 and not alert2:
            print("""

            Ant is hungry!

            """)
            alert2 = True
        elif 70 < self.hungry_meter <= 90 and alert2 and not alert3:
            print("""

            Ant is hungry and needs to eat now!

            """)

            alert3 = True
        elif self.hungry_meter >= 100:
            print("""

            Ant is dying...

            """)
            time.sleep(2)
            print("""

            Ant is dying...

            """)
            time.sleep(2)
            print("""

            Ant is dying...

            """)
            time.sleep(2)
            print("""

            Ant has died.

            """)
            self.command = "end"

    def move_forward_fast(self):
        if self.endurance <= 100:
            self.endurance += 20
            print(f"Ant has moved rapidly towards the {self.current_direction}")
            if self.hungry_meter <= 100:
                self.hungry_meter += 25
            else:
                self.hungry_meter >= 100
                self.hungry_meter = 100
                print("Ant is starving!")
            if self.current_direction == "north":
                self.y += 40
            elif self.current_direction == "west":
                self.x -= 40
            elif self.current_direction == "south":
                self.y -= 40
            else:
                self.x += 40
        else:
            self.endurance = 100
            print("Ant is tired and needs to rest.")

    def move_forward_slow(self):
        if self.endurance <= 0:
            self.endurance += 10
            self.hungry_meter += 15
            print(f"Ant moved slowly towards the {self.current_direction}.")
            if self.current_direction == "north":
                self.y += 20
            elif self.current_direction == "west":
                self.x -= 20
            elif self.current_direction == "south":
                self.y -= 20
            else:
                self.x += 20
        else:
            print("Ant is tired and needs to rest.")


        #for k in speed_cost:
            #if speed == k:
                #self.hungry_meter += speed_cost[k][0]
                #self.y += speed_cost[k][1]

        # if 0 < self.total_speed <= 30:
        # self.hungry_meter += 10
        # self.y += 2
        # elif 30 < self.total_speed <= 60:
        # self.hungry_meter += 30
        # self.y += 4
        # elif 60 < self.total_speed <= 100:
        # self.hungry_meter += 60
        # self.y += 6

    def move_backward(self):
        if self.endurance <= 0:
            self.endurance += 10
            self.hungry_meter += 15
            print(f"Ant moved backwards.")
            if self.current_direction == "north":
                self.y += 20
            elif self.current_direction == "west":
                self.x -= 20
            elif self.current_direction == "south":
                self.y -= 20
            else:
                self.x += 20
        else:
            print("Ant is tired and needs to rest.")

    def turn_left(self):
        orderlist = ["north", "west", "south", "east"]
        new_direction = ""

        try:
            for number in range(len(orderlist)):
                if self.current_direction == orderlist[number]:
                    new_direction = orderlist[number + 1]
                    print(f"Ant has turned left and is facing the {new_direction}.")
            self.current_direction = new_direction
        except IndexError:
            self.current_direction = "north"
            print(f"Ant has turned left and is facing the {self.current_direction}.")

    def turn_right(self):
        orderlist = ["north", "east", "south", "west"]
        new_direction = ""

        try:
            for number in range(len(orderlist)):
                if self.current_direction == orderlist[number]:
                    new_direction = orderlist[number + 1]
                    print(f"Ant has turned right and is facing the {new_direction}.")
            self.current_direction = new_direction
        except IndexError:
            self.current_direction = "north"
            print(f"Ant has turned right and is facing the {self.current_direction}.")

    def rest(self):
        for i in range(3):
            print("Ant is resting...")
            time.sleep(2)
        print("""Ant has fully recovered his endurance!        
        """)
        self.endurance = 0

    def eat(self):
        for i in range(3):
            print("Ant is eating...")
            time.sleep(2)
        print("""Ant is no longer hungry!
        """)
        self.hungry_meter = 0

    def location(self):
        local_details = f"""

        Ant is located at {self.x}, {self.y} and is facing the {self.current_direction}.

        """
        print(local_details)

    def status(self):
        status = f"""

        Endurance: {self.endurance}
        Hunger: Stomach is {self.hungry_meter}% empty.

        """
        print(status)
