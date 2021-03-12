
# 연습문제) 자바 시간에 만든 Circle 클래스를 구현 하라
# 생성자가 반지름 입력하면
# 넓이와 둘레의 길이를 계산
# 원의 둘레 = 반지름 * 2 *3.14
# 원의 넓이 = 반지름 * 반지름 * 3.14
import math

class Circle :
    #pass
    def __init__(self, r):
        self.r = r
        self.mkArea()
        self.mkLine()

    def mkArea(self) :
        self.area = math.pi * self.r ** 2

    def mkLine(self):
        self.line = 2 * math.pi * self.r

    def __str__(self):
        return f'area:{self.area}, line:{self.line}'

pizza = Circle(10)
print("pizza 크기 : ", pizza)
