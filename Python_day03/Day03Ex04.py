
# 반환값(return)을 사용하는 함수
# 함수에서 처리한 결과 값을 함수가 호출된 지점으로 돌려줄 수 있다.
# 함수는 처리할 인수를 전달 받고 그 결과를 반환하는 일을 한다.

# 두개의 정수를 입력받아서 비교 후 더 큰 수를 반환 해 주는 함수 선언 예제
# arguments(매개변수)와 return을 모두 사용하는 함수
def get_max(num1, num2) :
    if num1 > num2:
        maxnum = num1;
    else :
        maxnum = num2;

    return maxnum

a= 3
b = 9
c = 20
result = get_max(a, get_max(b,c))
# format 문자로 값 담기
print(f"더 큰 수는 {result} 입니다.")

# key의 목록과 value의 목록을 전달 받아서 
# dictionary 구조를 만들고 그 결과를 반환하는 함수

def mk_dict(keys, valuse) :
    if len(keys) != len(valuse) :
        print("key 리스트와 value 리스트의 길이가 다르다!")
        return

    # 딕셔너리 구조로 만들어준다.
    new_dict = dict()
    for i, key in enumerate(keys) :
        new_dict[key] =valuse[i]

    # 딕셔너리 구조 반환
    return new_dict

keys = ['고양이','배아파','쉬는시간 좀 '];
values = ['10', '2', '3']
dict1 = mk_dict(keys, values)
print(dict1)