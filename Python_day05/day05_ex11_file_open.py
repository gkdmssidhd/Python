# 쓰기모드로 open 하면 파일이 없을때 파일 생성
# 읽기 모드에서 파일이 없으면 오류!

#fp = open("io_test.txt", "w", encoding="UTF-8")

#fp.write("Hello world\n")
#fp.write("건강한 나라 대한민국은 개소리\n")
#fp.write("그지같은 개발공부~\n")

# fp.close()

# with 구문은 w 오픈을 자동으로 close 해줌
with open("io_test.txt", "w", encoding="UTF-8") as fp :
    fp.write("Hello world\n")
    fp.write("오늘은 수요일~\n")
    fp.write("개발공부 으아~\n")