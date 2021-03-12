import  random
from random import *

#1 보다 작은 실수인 난수
# random.random()
num = random()
print("random.random() =>", num)

# 인수로 주어진 a,b 사이의 난수
num = uniform(4, 6)
print("uniform =>", num)

# 0부터 인수로 주어진 범위 안에서 난수 발생
num = randrange(5)
print("randrange => ", num)

num = randrange(105, 110, 2)
print("randrange => ", num)

# 리스트에서 랜덤한 위치의 값을 뽑아 온다.
num = choice(list(range(5,11)))
print("choice =>", num)

#
