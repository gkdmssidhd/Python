
'''
filter 두번째 인자로 주어진 iterable에서 조건에 맞지 않는 항목 제거
리스트에서 제거 할 항목을 기능으로 만들어서 사용 한다.
'''
# 10으로 나눠서 0이 되는거
def choose(a) :
    if a%10 == 0:
        return a

lis = [10,25,30,35,50]

new_lis = list(filter(choose, lis))

print(new_lis)
print("-"*30)

# 두번째 방법
new_lis2 = list()

for a in lis :
    if a%10 == 0:
        new_lis2.append(a)

print(new_lis2)