from collections import defaultdict
class MyCalendarThree:

    def __init__(self):
        self.d=defaultdict(int)

    def book(self, s: int, e: int) -> int:
        self.d[s]+=1
        self.d[e]-=1

        res=list(self.d.keys())
        res.sort()
        curr=0
        maxi=0
        for key in res:
            curr+=self.d[key]

            if curr>maxi:
                maxi=curr
        return maxi

        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)