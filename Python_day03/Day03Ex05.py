
# 함수에 여러 인수를 전달 하는 예제
# 호출시 여러개의 인수를 튜플형식으로 받기

def findMax(*args) :
    print('args 의 타입은', type(args))
    max = 0
    for num in args :
        if num > max :
            max = num
    return max


# 정해지지 않은 양의 인수를 전달한다.
maxnum = findMax(2,5,11,36,43,3)
print(maxnum)

maxnum = findMax(7,23,53)
print(maxnum)

maxnum = findMax(2000)
print(maxnum)

print("-"*20)

def mkVerticalTotal(*scoreList) :
    totalList = [];
    for list in scoreList :
        # 만약에 totalList에 index가 있다면 누적하고
        # 아니라면 list에 append() 해 준다.
        for i, score in enumerate(list) :
            try :
                totalList[i] += score
            # 예외
            except :
                totalList.append(score)

    return totalList
'''
[1,1,1]
[2,2,2]
[3,3,3,5]
------------
같은 라인들 더하는거
[6,6,6,5]
'''
totalList = mkVerticalTotal([1,1,1],[2,2,2],[3,3,3,5])
print(totalList)