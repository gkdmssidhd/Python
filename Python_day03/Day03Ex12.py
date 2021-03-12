# 람다 표현식
# 람다 함수는 익명 함수이다.
'''
Lambda 매개변수 : 처리식

참일때 실행 if 조건 else 거짓일때 실행
'''
# 일반적인 파이썬 함수 선언
def maximun(x,y) :
    if x > y :
        return x
    else :
        return y
    
result = maximun(10, 20)
print("result =>", result)

# 위 함수를 Lambda 표현식으로 변경
result = (lambda x, y : x if x>y else y)(5, 10)
print("람다 실행 결과", result)
print("-"*20)
print("결과:", (lambda x, y : x if x>y else y)(8, 14))

# 람다 함수 응용
fish = ['파랑물고기이름뭐냐', '돔', '돌고래', '바다거북이', '니모를 찾아서']
# 그대로
fish.sort()
# 짧은 글씨에서 긴글씨로
fish.sort(key = lambda x:len(x))
print(fish)
print("-"*20)

fncList = [
    lambda msg: print("첫번째 함수", msg),
    lambda msg: print("두번째 함수", msg),
    lambda msg: print("세번째 함수", msg),
]

fncList[0]("hi")
fncList[1]("haeun")
fncList[2]("nice")

