
class SegTree:

    def __init__(self,arr):
        self.arr=arr
        self.n=len(arr)
        self.tree=[0]*(4*self.n)
        self.lazy=[0]*(4*self.n)

        self.build(0,0,self.n-1,arr)
    
    def check(self,idx):
        if idx==0 or idx==self.n-1:
            return 0
        
        if self.arr[idx-1]<self.arr[idx] and self.arr[idx]>self.arr[idx+1]:
            return 1
        else:
            return 0

    def build(self,node,start,end,arr):

        if start==end:
            self.tree[node]=self.check(start)
            return 

        mid=start+(end-start)//2
        self.build(2*node+1,start,mid,arr)
        self.build(2*node+2,mid+1,end,arr)
        self.tree[node]=self.tree[2*node+1]+self.tree[2*node+2]

    def query(self,l,r):
        return self.query_range(0,0,self.n-1,l,r)

    def query_range(self,node,start,end,l,r):
        self.push(node,start,end)

        if start>r or end<l:
            return 0

        if start>=l and end<=r:
            return self.tree[node]

        mid=(start+end)//2
        left=self.query_range(2*node+1,start,mid,l,r)
        right=self.query_range(2*node+2,mid+1,end,l,r)

        return left + right

    def push(self,node,start,end):
        if self.lazy[node]!=0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            
            self.lazy[node] = 0


    def update(self,l,r,val):
        self.update_range(0,0,self.n-1,l,r,val)

    def update_range(self,node,start,end,l,r,val):
        self.push(node,start,end)

        if start>r or end<l:
            return 

        if start>=l and end<=r:
            self.lazy[node]+=val
            self.push(node,start,end)
            return 

        mid=start+(end-start)//2
        self.update_range(2*node+1,start,mid,l,r,val)
        self.update_range(2*node+2,mid+1,end,l,r,val)
        self.tree[node]=self.tree[2 * node + 1] + self.tree[2 * node + 2]

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        res=[]
        n=len(nums)

        seg=SegTree(nums)

        for t,l,r in queries:
            if t==1:
                if r-l<2:
                    res.append(0)
                else:
                    res.append(seg.query(l+1,r-1))
            else:
                idx =l
                val=r
                aff=[]
                for i in [idx-1,idx,idx+1]:
                    if 0<i<n-1: 
                     aff.append((i,seg.check(i)))
                seg.arr[idx]=val

                for i,old in aff:
                    new=seg.check(i)
                    diff=new-old
                    if diff!=0:
                        seg.update(i,i,diff)
        


        return res
                

        