# 아 진짜 하기싫게 생김
import re 

def first(new_id):
    # 대문자를 다 소문자로 바꿈
    new_id = new_id.lower()
    return second(new_id)

def second(new_id):
    # 알파벳 소문자, 숫자, -, _, . 를 제외한 모든 문자 제거
    new_id = ''.join([char for char in new_id if char.isalnum() or char in ['-', '_', '.']])
    return third(new_id)

def third(new_id):
    # .이 2번 이상 연속된 부분을 하나의 .으로 치환
    new_id = re.sub(r'\.{2,}','.',new_id)
    return fourth(new_id)

def fourth(new_id):
    # .이 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')
    return fifth(new_id)

def fifth(new_id):
    # 빈 문자열이라면 a를 대입
    if not new_id:
        new_id = 'a'
    return sixth(new_id)

def sixth(new_id):
    # 길이가 16자 이상이면 15개까지만 남기고 나머지 제거, 만약 제거 후 .이 끝에 위치한다면 제거
    if len(new_id) >=16:
        new_id = new_id[:15].rstrip('.')
    return seventh(new_id)

def seventh(new_id):
    # 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복해서 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

def solution(new_id):
    answer = first(new_id) 
    return answer