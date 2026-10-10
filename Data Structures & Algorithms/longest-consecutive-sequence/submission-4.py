class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        temp = {}
        minNumber = nums[0]
        maxNumber = nums[0]
        for num in nums:
            if num not in temp:
                temp[num] = 1
            minNumber = min(minNumber, num)
        
        ans = 0
        tempans= 0
        for num in nums:
            if num - 1 in temp:
                continue
            tempNum = num
            while True:
                if tempNum in temp:
                    tempans+=1
                else:
                    break
                tempNum += 1
            
            ans = max(tempans,ans)
            tempans = 0
        return ans

        