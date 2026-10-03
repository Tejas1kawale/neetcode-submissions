class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMult = []
        suffixMult = []
        for i,num in enumerate(nums):
            if i == 0:
                prefixMult = [num]
                continue
            prefixMult.append(prefixMult[i-1] * num)
        
        for i,num in enumerate(reversed(nums)):
            if i == 0:
                suffixMult = [num]
                continue
            suffixMult.append(suffixMult[i-1] * num)
        
        suffixMult.reverse()
        #print(suffixMult)
        #print(prefixMult)
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans.append(suffixMult[i+1])
            elif i < n-1 :
                ans.append(prefixMult[i-1]* suffixMult[i+1])
            else:
                ans.append(prefixMult[i-1])
        return ans
