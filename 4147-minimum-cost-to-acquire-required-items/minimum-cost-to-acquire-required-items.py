class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total=max(need1,need2)*costBoth
        if costBoth> cost1+cost2:
            return min(cost1*need1 +cost2*need2,total)

        else:
            total1=0
            
            if need2>need1:
                total1+=need1*costBoth
                total1+=(need2-need1)*cost2
            else:
                total1+=need2*costBoth
                total1+=(need1-need2)*cost1
            
            return min(total,total1)