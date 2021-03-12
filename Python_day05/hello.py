
# 두개 메소드 만들어줌. 다른 파일에서 사용해보려고

def say_hello(name) :
    print('hello', name)

def say_hello2(name) :
    print('good morning', name)

# 이 안에서는 main이 되고 외부에서 부를때는 hello 이름이 나온다.
print("__name__ -> ", __name__)

# 메인 제어문 안에 넣어줘야 다른데서 외부를 전체 부를때 위에 애들은 출력이 안된다.
if __name__ == '__main__' :
    say_hello2("kim")
    say_hello("Lee")