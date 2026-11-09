import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses.sort(key=lambda x:x[1])
        n=len(courses)
        total=0
        heap=[]
        for i in range(n):
            total+=courses[i][0]

            heapq.heappush(heap,-courses[i][0])

            while total>courses[i][1]:
                total+=heapq.heappop(heap) 

        return len(heap)



    


        