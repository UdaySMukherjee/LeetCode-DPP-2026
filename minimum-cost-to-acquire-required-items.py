class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        return (
            self.minimumCost(cost2, cost1, costBoth, need2, need1) if cost2 < cost1 else
            costBoth * max(need1,need2)          if costBoth <= cost1 else
            costBoth *(mn:= min(need1,need2)) + 
            cost1*(need1 -mn) +
            min(cost2, costBoth) *(need2 -mn)    if costBoth < cost1+cost2 else
            cost1*need1 + cost2*need2
        )
        
