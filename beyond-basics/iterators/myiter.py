
class MyRange():
    def __init__(self, end):
        self.i = 0
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.end:
            raise StopIteration
        ret = self.i
        self.i += 1
        return ret
    
    def __reversed__(self):
        return Reversed(self.end, 0)

class Reversed():
    def __init__(self, end, start):
        self.i = end - 1
        self.start = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.start:
            raise StopIteration
        ret = self.i
        self.i -=1
        return ret

for x in reversed(MyRange(10)):
    print(x)