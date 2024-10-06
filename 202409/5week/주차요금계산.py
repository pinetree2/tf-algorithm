def park_fee(fees,time):
    if time <=fees[0]:
        return fees[1]
    else:
        return fees[1]+((time-fees[0])//fees[2])*fees[3]


def solution(fees, records):

    
    answer = [[0,0,0]]

    # records 를 다시 저장
    # 나눠서 담을 때, 시간을 숫자화 한다.
    result = []
    for record in records:
        parts = record.replace(":"," ").split()
        result.append([int(parts[0]),parts[1],parts[2]])

    result.sort(key=lambda x: x[0])

    # 입출차 기록을 보면서 시간을 계산해서 저장해둔다.
    for j in range(0,len(result)):
        time,car,io = result[j][0],result[j][1],result[j][2]
        num = time//100 + time%100
        
        # 각 차량번호에 해당하는 값이 나올때까지 찾는다. 
        if io == "IN":
            for i in range(1,len(result)):
                if result[i][1] == car:
                    if result[i][2] == 'OUT':
                        num = (result[i][0]//100 + result[i][0]%100) - num # 시간 계산 
                        fee = park_fee(fees,num)
                        answer.append([car,num,fee])
                        # result 에서 이 차량의 기록 삭제한다.
                        result.pop(i)
                    else: # 차량번호에 해당하는 값이 없다면, 그 차량은 아직 나가지 않은 것이다.
                        num = 2359 - num
                        fee = park_fee(fees,num)
                        answer.append([car,num,fee])
    
        # result 에서 이 차량의 기록 삭제한다.
        result.pop(j)
    
    return answer


### 시간이 부족하다... 일단 여기까지 풀겠다.
## 아직 제대로 못 한 부분 -> 시간을 16:00이라면 1600 으로 바꿔서 계산했기 때문에 이걸 다시 시간처럼 생각을 해서 결과를 내놔야하는데 지금.. 요상하게 계산하는중 