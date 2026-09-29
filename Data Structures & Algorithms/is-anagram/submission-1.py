class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = {}
        for character in s:
            if character not in temp1:
                temp1[character] = 1
            else:
                temp1[character] += 1

        temp2 = {}    
        for character in t:
            if character not in temp2:
                temp2[character] = 1
            else:
                temp2[character] += 1
        
        for key,value in temp1.items():
            if key not in temp2: return False
            if temp1[key] != temp2[key]:
                return False
                
        for key,value in temp2.items():
            if key not in temp1: return False
            if temp1[key] != temp2[key]:
                return False
        return True
            