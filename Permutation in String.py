class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countT,windowT=[0]*26,[0]*26
        for i in range(len(s1)):
            countT[ord(s1[i])-ord('a')]+=1
            windowT[ord(s2[i])-ord('a')]+=1

        if countT==windowT:
            return True

        for i in range(len(s1),len(s2)):
            windowT[ord(s2[i-len(s1)])-ord('a')]-=1
            windowT[ord(s2[i])-ord('a')]+=1
            if countT==windowT:
                return True

        return False
            
