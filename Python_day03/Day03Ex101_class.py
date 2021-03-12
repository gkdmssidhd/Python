
# 파이썬 객체와 클래스
# 딕셔너리와 객체는 비슷한 구조이다
# 딕셔너리 : 객체
#   키    :  필드, 속성(멤버변수) - 명사적
# value :value
# 기능 없다 : method(멤버함수) - 기능, 동사적

# 딕셔너리를 객체처럼 사용해보자.
# 딕셔너리는 [] 를 사용해서 하위멤버에 접근
# 객체는 . 으로 하위멤버에 접근
test = {"name": "HONG"}

#print(test["name"])
#print(test.get("name"))

#test.setName("KIM")
#name = test.getName("name")

def setA(name, self=test) :
    self[key] = name

def getA(key, self=test) :
    return self[key]

# 억지스러움
test['setA'] = setA
test['getA'] = getA

test['setA']("name", "KIM")
name = test['getA']("name")
print("name -> " ,name)

# 객체처럼 써본거지 딕셔너리를 이렇게 쓸 필요는 없다.