# 메뉴와 반복문을 이용해서
# 입력, 출력, 검색, 수정 삭제 기능을 구현한다.
# 국어, 영어, 수학 성적을 입력 받아서
# 총점, 평균, 학점을 출력하는 프로그램 구현.
# 함수를 최대한 많이 만들고 list를 활용한다.

# 국 영 수를 입력받고
# 국영수의 총점
# 국영수의 평균
# 결과가 나오게

user_list = []

print(user_list)
print(type(user_list))

user_name = input("성명 입력>> ")
korean = int(input("국어점수 입력 >> "))
English = int(input("영어점수 입력 >> "))
math = int(input("수학점수 입력 >> "))

str = """
성명 : {0}
국어 : {1}
영어 : {2}
수학 : {3}
""".format(user_name, korean, English, math)

print(str)

print("성명 : " + user_name)
print("국어 : " + str(korean))
print("영어 : " + str(English))
print("수학 : " + str(math))

all =  sum(korean, English, math)
AVG = sum(korean, English, math)/3

print(all, AVG)