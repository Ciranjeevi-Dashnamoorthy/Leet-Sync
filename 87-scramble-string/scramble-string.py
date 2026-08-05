class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from collections import Counter
        n=len(s1)

        @cache
        def check(s1,s2):
            print(s1,s2)

            if s1==s2:
                return True
            
            if len(s1)!=len(s2) or Counter(s1)!=Counter(s2):
                return False
            n=len(s1)
            
            for i in range(1,n):

                if check(s1[i:],s2[i:]) and check(s1[:i],s2[:i]):
                    return True
                
                if check(s1[:i],s2[-i:]) and check(s1[i:],s2[:-i]):
                    return True
            return False
        
        return check(s1,s2)
                

                
