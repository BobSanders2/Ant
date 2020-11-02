import numpy
import random

class Environment():
    def __init__(self):
        self.sticks_list = []
        self.nectars_list = []
        self.leaves_list = []
        self.poisonleaves_list = []
        self.env = numpy.arange(25 * 25).reshape(25, 25)
        self.objectlist = [26, 46, 55, 61, 66, 102, 114, 121, 157, 187, 193, 202, 222, 231, 265, 284, 293, 302, 321, 362, 381, 391, 427, 434, 439, 447, 469, 534, 537, 542, 555, 576, 597]
        self.objectlist_set = []

    def generate_env(self):
        self.set_objects()
        return self.env

    def set_objects(self):
        self.pop_sticks()
        self.pop_nectar()
        self.pop_leaves()
        self.pop_poisonleaves()

    def set_env(self):
        self.set_objects()
        for i in self.sticks_list:
            x, y = numpy.where(self.env == i)
            self.env[self.env == i] = 666

        for i in self.nectars_list:
            x, y = numpy.where(self.env == i)
            self.env[self.env == i] = 777

        for i in self.leaves_list:
            x, y = numpy.where(self.env == i)
            self.env[self.env == i] = 888

        for i in self.poisonleaves_list:
            x, y = numpy.where(self.env == i)
            self.env[self.env == i] = 999

    def pop_sticks(self):
        direction = True
        while len(self.objectlist_set) <= random.randint(4, 8):
            i = random.choice(self.objectlist)
            if i not in self.objectlist_set and direction:
                direction = False
                self.objectlist_set.append(i)
                self.sticks_list.append(i)
                self.sticks_list.append(i + 1)
                temp = random.randint(0, 1)
                if temp != 0:
                    self.sticks_list.append(i + 2)
            elif i not in self.objectlist_set and not direction:
                direction = True
                self.objectlist_set.append(i)
                self.sticks_list.append(i)
                self.sticks_list.append(i + 25)
                temp = random.choice([0, 25])
                if temp != 0:
                    self.sticks_list.append(i + temp)
            else:
                pass

    def pop_nectar(self):
        while len(self.nectars_list) <= 9:
            i = random.choice(self.objectlist)
            if i not in self.objectlist_set:
                self.objectlist_set.append(i)
                self.nectars_list.append(i)
            else:
                pass

    def pop_leaves(self):
        while len(self.leaves_list) <= random.randint(8, 10):
            i = random.choice(self.objectlist)
            if i not in self.objectlist_set:
                self.objectlist_set.append(i)
                self.leaves_list.append(i)
            else:
                pass

    def pop_poisonleaves(self):
        while len(self.poisonleaves_list) <= random.randint(4, 7):
            i = random.choice(self.objectlist)
            if i not in self.objectlist_set:
                self.objectlist_set.append(i)
                self.poisonleaves_list.append(i)
            else:
                pass
