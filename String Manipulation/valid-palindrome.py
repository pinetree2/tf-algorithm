import sys 
# 대소문자 여부 구분 x, 영문자, 숫자만을 대상으로 함 
s = sys.stdin.readline()

class Solution:
    def isPalindrome(self,s:str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) !=strs.pop():
                return False 
        
        return True
    

obj = Solution()
print(obj.isPalindrome(s))  # True
