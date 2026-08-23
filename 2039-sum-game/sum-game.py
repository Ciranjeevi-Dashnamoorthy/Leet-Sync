class Solution:
    def sumGame(self, s: str) -> bool:

        """
        Observation:

        if there is odd moves, means Alice always wins

        Think of even moves, where Bob has chance to win , only little , but think 
        of a way
        
        split into two diff parts , the mark on the both sides 
        that is min(m1,m2) can be satisfied by assigning same values as alice hcooses

        then the rem - s1-s2 , the actual sum btw 1 and 2 required to make up

        what do we do

        each two pair can make a guarentee if sum 9 -- why if a chooses 3 , b chooses 6 ,(0,9) etc

        if the diff is mod 9 then only we can satisfy else NO

        """
        s1,s2=0,0
        m1,m2=0,0
        n=len(s)
        for i in range(n):
            if i<n//2:
                if s[i]=="?":
                    m1+=1
                else:
                    s1+=int(s[i])
            else:
                if s[i]=="?":
                    m2+=1
                else:
                    s2+=int(s[i])
        
      
        
        if (m1+m2)%2==1 or (s1-s2)!=((m2-m1)//2)*9:
            return True
        else:
            return False
         



        