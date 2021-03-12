
# read 는 r
with open("io_test.txt", "r", encoding="UTF-8") as fp:
    data = fp.read()
    print(data)

# while 문으로
with open("io_test.txt", "r", encoding="UTF-8") as fp:
    while True :
        data = fp.read()
        print(data[:-1])
        if not data :
            break
            
# read lines
with open("io_test.txt", "r", encoding="UTF-8") as fp:
    lines = fp.readlines()
    print(lines)
    for line in lines :
        print(line[:-1])