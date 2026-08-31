# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next
        
        dist=[]
        
        for i in range(1,len(res)-1):
            if res[i-1]<res[i] and res[i]>res[i+1]:
                dist.append(i)
            if res[i-1]>res[i] and res[i]<res[i+1]:
                dist.append(i)
        
        if len(dist)<2:
            return [-1,-1]
        else:
            
            maxi=dist[-1]-dist[0]
            mini=float("inf")
            for i in range(len(dist)-1):
                mini=min(mini,dist[i+1]-dist[i])
            return [mini,maxi]

        