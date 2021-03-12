#앞에서 사용한 딕셔너리 구조를 class로 변경
# 클래스 선언은 class 키워드를 이용한다.

'''
class 클래스명 :
    생성자 메소드
    멤버메소드
    멤버필드
'''

class People :
    # 생성자 메소드 선언,
    # 생성자와 멤버메소드는 self 매개변수가 선언 되어야 한다.
    def __init__(self, name) :
        self.name = name

    def setName(self, name) :
        self.name = name

    def getName(self) :
        return self.name

    def greeting(self):
        return self.name + "님 하이"

# 객체생성인데 자바처럼 new는 없음
kim = People("kim")
pList = [kim, People("Lee"), People("park")]

pList[0].setName("HONG")

for person in pList :
    print("인사>>", person.greeting() )