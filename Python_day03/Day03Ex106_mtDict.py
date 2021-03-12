
class MyDict(dict) :
    def __init__(self):
        #상속 받은 클래스는 부모의 생성자 호출 반드시 필요
        super().__init__()


    def setAttribute(self, key, value) :
        self[key] = value

    def getAttribute(self, key) :
        return self[key]

    def size(self) :
        return len(self)

mydict = MyDict()
mydict.setAttribute("name", "이하은")
mydict.setAttribute("address", "주소")

print("성명: ", mydict.getAttribute("name"))
print("주소: ", mydict.getAttribute("address"))

print("크기: ", mydict.size())

# 과제
# 주소록 프로그램 구현
# 번호, 성명, 전화, 주소 저장
# CRUD 가 되도록 구현 한다.(클래스, 자료구조를 많이 활용)