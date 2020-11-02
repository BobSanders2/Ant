import os
import itertools
import time
from collections import defaultdict
class Ant():
    def __init__(self):
        self.ant_status = {
            'alive': True,
            'hungry_meter': 0,
            'health': 100,
            'endurance': 0,
            'x': 0,
            'y': 0,
            'current_direction': 'north',
        }

    # def hunger_check(self):
    #     if 10 < self.ant_status['hungry_meter'] <= 30 and not alert1:
    #         print("""
    #
    #         Ant is getting hungry
    #
    #         """)
    #         alert1 = True
    #     elif 40 <= self.ant_status['hungry_meter'] <= 60 and alert1 and not alert2:
    #         print("""
    #
    #         Ant is hungry!
    #
    #         """)
    #         alert2 = True
    #     elif 70 < self.ant_status['hungry_meter'] <= 90 and alert2 and not alert3:
    #         print("""
    #
    #         Ant is hungry and needs to eat now!
    #
    #         """)
    #
    #         alert3 = True
    #     elif self.ant_status['hungry_meter'] >= 100:
    #         print("""
    #
    #         Ant is dying...
    #
    #         """)
    #         time.sleep(2)
    #         print("""
    #
    #         Ant is dying...
    #
    #         """)
    #         time.sleep(2)
    #         print("""
    #
    #         Ant is dying...
    #
    #         """)
    #         time.sleep(2)
    #         print("""
    #
    #         Ant has died.
    #
    #         """)
    #         self.command = "end"

    def move_forward_fast(self):
        if self.ant_status['endurance'] <= 100:
            self.ant_status['endurance'] += 20
            print(f"Ant has moved rapidly towards the {self.ant_status['current_direction']}")
            if self.ant_status['hungry_meter'] <= 100:
                self.ant_status['hungry_meter'] += 25
            else:
                self.ant_status['hungry_meter'] >= 100
                self.ant_status['hungry_meter'] = 100
                print("Ant is starving!")
            if self.ant_status['current_direction'] == "north":
                self.y += 2
            elif self.ant_status['current_direction'] == "west":
                self.x -= 2
            elif self.ant_status['current_direction'] == "south":
                self.y -= 2
            else:
                self.x += 2
        else:
            self.ant_status['endurance'] = 100
            print("Ant is tired and needs to rest.")

    def move_forward_slow(self):
        if self.ant_status['endurance'] <= 0:
            self.ant_status['endurance'] += 10
            self.ant_status['hungry_meter'] += 15
            print(f"Ant moved slowly towards the {self.ant_status['current_direction']}.")
            if self.ant_status['current_direction'] == "north":
                self.y += 20
            elif self.ant_status['current_direction'] == "west":
                self.x -= 20
            elif self.ant_status['current_direction'] == "south":
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
        if self.ant_status['endurance'] <= 0:
            self.ant_status['endurance'] += 10
            self.ant_status['hungry_meter'] += 15
            print(f"Ant moved backwards.")
            if self.ant_status['current_direction'] == "north":
                self.y += 20
            elif self.ant_status['current_direction'] == "west":
                self.x -= 20
            elif self.ant_status['current_direction'] == "south":
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
                if self.ant_status['current_direction'] == orderlist[number]:
                    new_direction = orderlist[number + 1]
                    print(f"Ant has turned left and is facing the {new_direction}.")
            self.ant_status['current_direction'] = new_direction
        except IndexError:
            self.ant_status['current_direction'] = "north"
            print(f"Ant has turned left and is facing the {self.ant_status['current_direction']}.")

    def turn_right(self):
        orderlist = ["north", "east", "south", "west"]
        new_direction = ""

        try:
            for number in range(len(orderlist)):
                if self.ant_status['current_direction'] == orderlist[number]:
                    new_direction = orderlist[number + 1]
                    print(f"Ant has turned right and is facing the {new_direction}.")
            self.ant_status['current_direction'] = new_direction
        except IndexError:
            self.ant_status['current_direction'] = "north"
            print(f"Ant has turned right and is facing the {self.ant_status['current_direction']}.")

    def rest(self):
        for i in range(3):
            print("Ant is resting...")
            time.sleep(2)
        print("""Ant has fully recovered his endurance!        
        """)
        self.ant_status['endurance'] = 0

    def eat(self):
        for i in range(3):
            print("Ant is eating...")
            time.sleep(2)
        print("""Ant is no longer hungry!
        """)
        self.ant_status['hungry_meter'] = 0

    def location(self):
        local_details = f"""

        Ant is located at {self.ant_status['x']}, {self.ant_status['y']} and is facing the {self.ant_status['current_direction']}.

        """
        print(local_details)

    def status(self):
        status = f"""

        Endurance: {self.ant_status['endurance']}
        Hunger: Stomach is {self.ant_status['hungry_meter']}% empty.

        """
        print(status)

    # def alive_check(self):
    #     if not self.ant_status['alive']:
    #         print("Ant has died")
    #         break
