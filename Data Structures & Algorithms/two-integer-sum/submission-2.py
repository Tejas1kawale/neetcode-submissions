class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,num in enumerate(nums):
            if num not in temp:
                temp[num] = i
            elif num == target - num:
                temp[num] = i
        
        for i,num in enumerate(nums):
            search = target - num
            if search in temp and i != temp[search]:
                return [i, temp[search]]

        

            
