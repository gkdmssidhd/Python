
# 파일자체 가져오면 앞에 경로 생략가능
from Day03Ex104 import Washer

# 이거는 경로 해줘야함
#import Day03Ex104

class SamsungWasher (Washer) :
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name

    def info(self):
        print(self.__str__())

    def __str__(self):
        return f'{self.maker}, {self.name}, {self.size}'

samsungWasher = SamsungWasher(10, "Samsung" , "그랑데")
print(samsungWasher)
samsungWasher.washing()