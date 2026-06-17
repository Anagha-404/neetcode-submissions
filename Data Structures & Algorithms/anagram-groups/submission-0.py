class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L=[]
        seen = set()
        for i in range(len(strs)):
            if i in seen:
                continue
            l=[]
            
            l.append(strs[i])
            for j in range(i+1,len(strs)):
                
                if sorted(strs[i])==sorted(strs[j]):
                    l.append(strs[j])
                    seen.add(j)
            L.append(l)
        return L