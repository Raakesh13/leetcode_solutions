# def get_time(func):
#     import time
#     print(time.time())
#     return func


# @get_time
# def _sum(a, b):
#     return a+b


# print(_sum(10, 15))

class area:
    def __init__(self, side):
        self.side = side

    def _area(self):
        return self.side**2


class square(area):
    def __init__(self, side):
        super().__init__(side)

    def _area(self):
        return super()._area()*self.side


ob = square(5)
print(ob._area())
