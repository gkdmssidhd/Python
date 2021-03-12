import pickle
from pprint import pprint

person1 = {
    "name" : "이하은",
    "height" : 161,
    "weight" : 48
}

person2 = {
    "name" : "이은",
    "height" : 163,
    "weight" : 48
}

people = [person1, person2]

# 객체니까 바이너리 코드로
with open("people.pickle", "wb") as f :
    pickle.dump(people, f)

# 로드
with open("people.pickle", "rb") as f:
    new_list = pickle.load(f)

# print(new_list)
# 예쁘게 출력되는 pprint
pprint(new_list)