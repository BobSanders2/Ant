import os
import itertools
import time


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
        self.max_hungry_meter = 100
        self.hungry_meter = 0
        # self.working_strength = 100
        self.total_speed = ""
        self.x = 0
        self.y = 0
        self.commands_list = {
            "status": self.status,
            "location": self.location
            "move forward fast": [self.move_forward, 20]
            "move forward slowly": [self.move_forward, 10]
            "move back": self.move_backward,
            "turn left": self.turn_left,
            "turn right": self.turn_right
        }

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

    def move_forward(self, speed):
        #speed = input(">>>")
        speed_cost = {"fast": [20, 6], "slow": [10, 2]}

        if speed == 20 and self.total_speed == 0:
            self.total_speed = 20
            self.y += 2
        elif speed == 20 and self.total_speed == 10:
            self.total_speed = 40
            self.y += 4
        elif speed == 10 and self.total_speed == 0:
            self.total_speed = 10
            self.y += 1
        else:
            print("Cannot move any faster")

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



    def location(self):
        local_details = f"""

        Ant is located at {self.x}, {self.y}.

        """
        print(local_details)

    def status(self):
        status = f"""

        Ant is walking at a speed of {self.total_speed}.
        Ant is {self.hungry_meter}% hungry.

        """
        print(status)