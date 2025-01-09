def solution(files):
    answer = []

    # files 배열을 보면서, HEAD,NUMBER,TAIL 을 나눠 저장한다?
    # HEAD 는 문자열
    # NUMBER 는 숫자 문자열 (처음 등장한 숫자 문자열 최대 5개까지만 저장함)
    # TAIL 은 나머지

    # new_files 구성은 [(HEAD,NUMBER,TAIL),...] 이런 형태로 저장하는게 좋을 것 같다.
    new_files = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        idx = 0

        # 일단 숫자가 나오기 전까지 string 은 head 에 저장한다.
        # 숫자가 나오면 number 에 저장한다. (최대 5개까지만)
        # 숫자가 끝나거나 5개 이상이 되면 나머지는 tail 에 저장한다.
        # 문제점 :head 에 영문자 말고 특수문자인 - 도 들어갈수있음 
        for i in range(len(file)):
            
            # 문제점 : tail 은 문자,숫자 다 되는데 head 와 number 이후에 남는거를 넣어야 하는거면,, number 가 채워졌을때는 tail로 저장되게하자
            if file[i].isalpha():
                if number == '':
                    head += file[i]
                    #number 가 존재하지 않는 경우는 제시되어있지 않으니 ㄱㅊ할듯
                else:
                    tail += file[i]
            elif file[i].isdigit():
                if len(number) < 5:
                    number += file[i]
                else:
                    tail += file[i]
            else:
                tail += file[i]
        new_files.append((head,number,tail))
    

    # new_files 를 정렬한다.
    # 1. HEAD 기준으로 정렬한다. 사전순, 대소문자 구분 안함 (근데 소문자로 만들면 안됨)
    # 2. head 가 같은 것이 존재하는 경우, number 숫자 순으로 정렬한다. (숫자 앞에 0 은 무시)
    # 3. head,number 가 같은 것이 존재하는 경우 원래 입력에 주어진 순서대로 정렬한다. 

    # head,number 가 같은 것이 존재하는 경우는 -> 고대로 둔다. 가 성립되어야 한다는거자낭 ? -> sorted 가 이를 만족한다고 함.
    new_files = sorted(new_files,key=lambda x : (x[0].lower(),int(x[1] if x[1] else 0)))
    for file in new_files:
        answer.append(file[0]+file[1]+file[2])


    return answer

#---
#이 모든게 정규 표현식을 쓰면 쉽게 해결된다.
#근데 난 정규표현식 진짜.. 어렵다... 쉣!

import re

def solution(files):
    def parse_file(file):
        # 정규 표현식으로 HEAD, NUMBER, TAIL 분리
        match = re.match(r"([a-zA-Z\s\-.]+)(\d{1,5})(.*)", file)
        head, number, tail = match.groups()
        return head, number, tail

    # 파일명에서 HEAD, NUMBER, TAIL로 분리하고, 이를 정렬
    sorted_files = sorted(files, key=lambda file: (parse_file(file)[0].lower(), int(parse_file(file)[1])))

    return sorted_files
