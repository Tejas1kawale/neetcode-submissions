import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = []
        t = {}
        for i, num in enumerate(nums):
            if num not in t:
                t[num] = 1
            else:
                t[num] += 1

        for key, value in t.items():
            heapq.heappush(temp, ( -value, key ))
        
        ans = []
        while temp and k>0:
            repeated, value = heapq.heappop(temp)
            ans.append(value)
            k -= 1
        
        return ans