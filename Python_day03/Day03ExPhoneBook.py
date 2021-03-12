
# 이름넣고 폰북 전화번호부 해서 검색 추가 삭제 CRUD

addrlist = [
    {"idx": 0, "name": 'HONG', "phone": '010-111-111', "addr": '서울'},
    {"idx": 1, "name": 'KIM', "phone": '010-111-111', "addr": '경기도 고양시'},
    {"idx": 2, "name": 'LEE', "phone": '010-111-111', "addr": '부산'}
]

# 메뉴 메소드 선언
def menu() :
    print("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
    no = int(input("선택 : "))
    return no

# 기능별 메소드 선언
def Data() :
    # 이름, 전화번호, 주소를 입력받아서 돌려주는 함수
    global idx
    idx += 1
    name = input("성명입력 : ")
    phone = input("전화번호입력 : ")
    addr = input("주소입력 : ")

    return {"idx":idx, "name":name, "phone":phone, "addr":addr}

# 입력 메소드
def inputData() :
    print("🍀입력 기능🍀")
    # 입력 기능
    data_value = Data()
    addrlist.append(data_value)
    print("데이터 입력 성공")
    
# 출력 메소드
def showData() :
    print("🍀출력 기능🍀")
    for person in addrlist :
        print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(person["idx"], person["name"], person["phone"], person["addr"]))

# 검색 메소드
def find_idx(addrlist, idx=None, name=None) :
    flag = 0
    if name != None :
        flag = 1

    for i, person in enumerate(addrlist) :
        if flag == 0 :
            if person["idx"] == idx :
                return i
        else :
            if person["name"] == name :
                return i
    return -1

def searchData() :
    print("🍀검색 기능🍀")
    searchName = input("검색 할 이름을 입력하세요 : ")
    index = find_idx(addrlist, name=searchName)
    person = addrlist[index]
    print("{: ^3}|{: ^6}|{: ^13}|{: ^9}".format(person["idx"], person["name"], person["phone"], person["addr"]))
    
def modifyData() :
    print("수정 기능")

def deleteData() :
    print("삭제 기능")
    # del addrList[1]
    del_idx = int(input("삭제 할 번호를 입력 하세요 : "))
    index = find_idx(addrList, idx=del_idx)
    if index != -1:
        del addrList[index]
        print("삭제 성공!")
    else:
        print("삭제 할 대상이 없습니다!")


factory = [inputData, showData, searchData, modifyData, deleteData]


def run(no):
    print("{}번이 선택되었습니다!".format(no))
    if no == 6:
        print(" 종료 ")
        exit(0)

    if no in range(1, len(factory) + 1):
        factory[no - 1]()
    else:
        print("해당 사항 없슴");


# 메인함수 선언
def main():
    while True:
        print("{:=^40}".format(" 주소록 "))
        no = menu();

        run(no)
        print("\n")


if __name__ == '__main__':
    main()