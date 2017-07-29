from heapq import heappop, heappush

class Heapy:
    def __init__(self):
        self.highers = []
        self.lowers = []
        self.median = []

    def add_number(self, number):
        if len(self.lowers) == 0 or number < -1 * self.lowers[0]:
            heappush(self.lowers, -1 * number)
        else:
            heappush(self.highers, number)

    def balance(self):
        bigger = self.highers if len(self.highers) > len(self.lowers) else self.lowers
        smaller = self.highers if len(self.highers) < len(self.lowers) else self.lowers
        if len(bigger) - len(smaller) > 1:
            heappush(smaller, - heappop(bigger))

    def get_median(self):
        if len(self.highers) == len(self.lowers):
            return 1.0 * (self.highers[0] - self.lowers[0]) / 2
        elif len(self.highers) > len(self.lowers):
            return 1.0 * self.highers[0]
        else:
            return -1.0 * self.lowers[0]
