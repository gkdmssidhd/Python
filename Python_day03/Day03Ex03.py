
# 여러 값을 반환하는 함수
def fn() :
    return 10, 5, 30

a, b, c = fn()


print(a, b, c)

num1 = 100
num2 = 200

# 스왑 하기
(num1, num2) = (num2, num1)

print(num1, num2)
print(num2, num1)

def show_number(number) :
    print("전달 받은 숫자 : ", number)

show_number(5+1)

# 매개변수의 갯수와 수는 인자의 순서 갯수와 일치 해야 한다.
# 기본값 설정도 가능
def show_people(name, age=10) :
    print(f"name : {name}")
    print(f"agd : {age}")

# 매개변수와 인자의 갯수는 일치해야 한다. 위에는 2개 여기도 2개
# 매개변수 선언시에 기본값을 지정하면 인자를 생략 할 수 있다.
show_people("이하은")