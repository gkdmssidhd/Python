
# 전역변수와 지역변수
# 변수의 scope가 있다.
# 함수에서 전역변수를 참조하는 것은 그냥 가능하다.
# 함수에서 전역변수의 값을 수정하기 위해서는 global 선언을 해야한다.
# global을 붙이지 않고 값을 변경하면 함수의 지역변수가 새로 만들어지는 것

a = 10

def setA() :
    # 전역 변수의 값을 변경하기 위해서 global 키워드 사용
    global a
    a = 200

print(a)

people = [
    {"num":1, 'name':"Kim", 'phone':"010-111-123"},
    {"num":2, 'name': "Song", 'phone': "010-121-333"},
    {"num":3, 'name': "Lee", 'phone': "010-134-213"}
]

num_seq = 3
def addDictPeople(name, phone) :
    # global 키워드
    global num_seq
    num_seq += 1
    people.append({"num":num_seq, 'name':name, 'phone':phone})

addDictPeople("ha", "010-9180-1234")
print("num seq =>", num_seq)
print(people[3])