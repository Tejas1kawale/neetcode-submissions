class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s) - 1
        start = 0
        while start<= end:
            if s[start] == " " or not s[start].isalnum():
                start += 1
                continue
            elif s[end] == " " or not s[end].isalnum():
                end -= 1
                continue
            else:
               
                print("s[start] : ",s[start]," s[end] : ", s[end] )
                if s[start].lower() != s[end].lower():
                    return False
            start += 1
            end  -= 1
        return True
                    
