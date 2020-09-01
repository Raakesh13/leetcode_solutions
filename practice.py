from abc import ABC, abstractmethod


class Area(ABC):

    def __init__(self):
        pass

    def getArea(self, abstractmethod):
        pass


class Square(Area):
    __num = 10
    num2 = 15

    def __init__(self, side):
        super().__init__()
        self.side = side

    def getArea(self):
        # return super().getArea(abstractmethod)
        return self.side**2

    @classmethod
    def get_num(cls, num1=None):
        if num1:
            cls.__num = num1
        return cls.__num, cls.num2

    @staticmethod
    def get_time():
        import time
        return time.localtime()


ob = Square(25)
area = Square.getArea(ob)
print(area)
print(ob.get_num(22))
Square.__num = 20
Square.num2 = 50
print(Square.get_num())
print(Square.get_time())
