class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            c=0
            if i not in d:
                c+=1
                d[i]=c
            elif i in d:
                d[i]+=1
                if d[i]>1:
                    return True
        return False