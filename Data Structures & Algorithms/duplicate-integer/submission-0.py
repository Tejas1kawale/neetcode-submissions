class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for num in nums:
         
            if num not in temp:
                print(num)
                temp[num] = 1
            else:
                return True
            
        return False