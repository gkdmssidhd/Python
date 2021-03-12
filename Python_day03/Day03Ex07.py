
# 디폴트 매개변수
# 함수를 선언할때 매개변수의 기본값을 정해준다.
# 함수 호출시 디폴트 매개변수에 해당하는 인자를 생략 가능하다.
# 앞에 사용되는 매개변수가 디폴트라면 그 다음 매개변수는 모두 디폴트 매개변수.
# 앞에 사용되는 매개변수가 디폴트인데 뒤에 일반이면 오류
def showInfo(id, name="no-name", age=0) :
    print("id:", id)
    print("name:", name)
    print("age:", age)

showInfo("Kim")
# 함수 호출할때 매개변수를 지정해 준다.
showInfo(age=30, name="하은", id="LEE")