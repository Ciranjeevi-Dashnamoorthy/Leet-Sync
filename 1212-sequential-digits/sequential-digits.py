class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        l,r=len(str(low)),len(str(high))
        res=[]
        s="123456789"
        for i in range(l,r+1):
            
            for j in range(0,9-i+1):
                num=int(s[j:j+i])
                if low<=num<=high:
                    res.append(num)
        return res
        




            
            