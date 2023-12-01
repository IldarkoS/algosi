import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        return False

    def startNext(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.time = time
        self.pages = random.randint(1,20)

    def getPages(self):
        return self.pages

    def getTime(self):
        return self.time

    def waitTime(self, current_time):
        return current_time - self.time