# 연습문제

# 반지름을 입력받아서 둘레의 길이와 면적을 구한다.
import math

r =int(input("반지름 입력 >>"))
round = 0;
area = 0;

#연산하기
round = 2 * math.pi * r
area = math.pi * r**2

#출력하기
print("반지름이 {} 인 원의 면적은 {}이고 둘레는 {}이다.".format(r, area, round))