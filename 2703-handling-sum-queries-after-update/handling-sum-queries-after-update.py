
class SegTree:

    def __init__(self,arr):
        self.n=len(arr)
        self.tree=[0]*(4*self.n)
        self.lazy=[False]*(4*self.n)

        self.build(0,0,self.n-1,arr)

    def build(self,node,start,end,arr):

        if start==end:
            self.tree[node]=arr[start]
            return 

        mid=start+(end-start)//2
        self.build(2*node+1,start,mid,arr)
        self.build(2*node+2,mid+1,end,arr)
        self.tree[node]=self.tree[2*node+1]+self.tree[2*node+2]

    def query(self,l,r):
        return self.query_range(0,0,self.n-1,l,r)

    def query_range(self,node,start,end,l,r):
        self.push(start,node,end)

        if start>r or end<l:
            return 0

        if start>=l and end<=r:
            return self.tree[node]

        mid=(start+end)//2
        left=self.query_range(2*node+1,start,mid,l,r)
        right=self.query_range(2*node+2,mid+1,end,l,r)

        return left + right

    def push(self,node,start,end):
        if self.lazy[node]:
            self.tree[node] = (end - start + 1) - self.tree[node]
            
            if start != end:
                self.lazy[2 * node + 1]= not self.lazy[2 * node + 1]
                self.lazy[2 * node + 2]= not self.lazy[2 * node + 2]
            
            self.lazy[node] = False


    def update(self,l,r,val):
        self.update_range(0,0,self.n-1,l,r,val)

    def update_range(self,node,start,end,l,r,val):
        self.push(node,start,end)

        if start>r or end<l:
            return 

        if start>=l and end<=r:
            self.lazy[node]= not self.lazy[node]
            self.push(node,start,end)
            return 

        mid=start+(end-start)//2
        self.update_range(2*node+1,start,mid,l,r,val)
        self.update_range(2*node+2,mid+1,end,l,r,val)
        self.tree[node]=self.tree[2 * node + 1] + self.tree[2 * node + 2]


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:

        n=len(nums1)
        seg=SegTree(nums1)
        total=sum(nums2)
        res=[]

        for t,l,r in queries:
            if t==1:
                seg.update(l,r,0)
            if t==2:
                total+=seg.query(0,n-1)*l
            if t==3:
                res.append(total)
            
        return res



        