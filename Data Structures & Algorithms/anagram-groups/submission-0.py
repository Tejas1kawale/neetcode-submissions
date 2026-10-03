class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        MAP = {}
        strsTemp = []
        for i,str1 in enumerate(strs):
            strsTemp.append("".join(sorted(str1)))
        
        for i,str1 in enumerate(strsTemp):
            
            if str1 not in MAP:
                #print(MAP)
                MAP[str1] = []
                MAP[str1].append(i)
            else:
                MAP[str1].append(i)

        ans = []
        for key,values in MAP.items():
            temp = []
            for index in values:
                temp.append(strs[index])
            ans.append(temp)
        
        return ans