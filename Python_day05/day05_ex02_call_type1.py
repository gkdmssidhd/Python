# 부르기 첫번째 방법
# as 로 줄여서 할 수 도 있음
# 줄이기 않고 import hello만 한다면 hello.say_hello
# 모듈을 만들면 외부에 있는 파일을 사용할 수 있다.

import hello as hel
import hello

# 이렇게 부를 수 도 있다.
from hello import say_hello

# hello파일에 있는 모든 함수를 다 가져와라
from hello import *


if __name__ =='__main__' :
    hello.say_hello("haeun")
    hel.say_hello2("mose")

    say_hello("Lee")
    say_hello2("chi")