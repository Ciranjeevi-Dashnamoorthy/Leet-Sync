from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.total=0
        self.arr=SortedList()
        

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.total+=1
        

    def findMedian(self) -> float:
        if self.total%2==1:
            return self.arr[self.total//2]
        else:
            ans=(self.arr[self.total//2]+self.arr[self.total//2-1])/2.0
            return ans
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()