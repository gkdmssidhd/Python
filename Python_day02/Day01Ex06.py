

user_list = ['이하은','김얄롱','김모세','몰라']

print(user_list)
print(type(user_list))
# print(user_list[0])


for i, name in enumerate(user_list) :
    print(i, name)

print()
print("----------------------")

cnt = 0
# lenght -> len
while cnt < len(user_list) :
    # \t하면 한줄에 다나옴
    # sep="" 안에 뭐 넣어주면 구분자를 바꿔줄 수 있음.
    print(cnt, user_list[cnt], end="\t", sep=":")
    cnt+=1

print()
print("-----------------------")
# 2:2번부터 출력
# :2 0번부터 2번까지 출력
print(user_list[2:], "\t")