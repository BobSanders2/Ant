import time

class Ant():
    def __init__(self):
        self.head_attached = True
        self.torso_attached = True
        self.end_attached = True
        self.leg1_attached = True
        self.leg2_attached = True
        self.leg3_attached = True
        self.leg4_attached = True
        self.leg5_attached = True
        self.leg6_attached = True
        self.left_antenna_attached = True
        self.right_antenna_attached = True
        self.weight_milligram = 3
        self.color = "Red"
        self.awake = True
        self.alive = True
        self.hungry_meter = 0
        self.working_strength = 100
        self.total_speed = 0


    def movement(self, speed):
        self.total_speed += speed
        if 0 < self.total_speed <= 30:
            self.hungry_meter += 10
        elif 30 < self.total_speed <= 60:
            self.hungry_meter += 30
        elif 60 < self.total_speed <= 100:
            self.hungry_meter += 60

    def status(self):
        status = f"""
        
        Ant is walking at a speed of {self.total_speed}.
        Ant is {self.hungry_meter}% hungry.
                
        """
        return status

bob = Ant()
bob.movement(90)
print(bob.status())