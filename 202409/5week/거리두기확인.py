def solution(places):
    answer = []
    # 이게 .. 3중 for 문을 하는게 맞나?....
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    # 상하좌우
                    if i-1 >= 0 and place[i-1][j] == 'P':
                        answer.append(0)
                    if i+1 < 5 and place[i+1][j] == 'P':
                        answer.append(0)
                    if j-1 >= 0 and place[i][j-1] == 'P':
                        answer.append(0)
                    if j+1 < 5 and place[i][j+1] == 'P':
                        answer.append(0)
                    # 대각선
                    if i-1 >= 0 and j-1 >= 0 and place[i-1][j-1] == 'P':
                        answer.append(0)
                    if i-1 >= 0 and j+1 < 5 and place[i-1][j+1] == 'P':
                        answer.append(0)
                    if i+1 < 5 and j-1 >= 0 and place[i+1][j-1] == 'P':
                        answer.append(0)
                    if i+1 < 5 and j+1 < 5 and place[i+1][j+1] == 'P':
                        answer.append(0)

    ### 이렇게 하면 안되는것같은데 방법을 모르겠어 모르겠다. 미치겠다. 머리아프다. 포기다.

    return answer


