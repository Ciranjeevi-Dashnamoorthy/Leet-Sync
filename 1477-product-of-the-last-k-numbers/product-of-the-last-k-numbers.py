class ProductOfNumbers:

    def __init__(self):
        self.li=[]
        self.prod=1
        

    def add(self, num: int) -> None:
        if num==0:
            self.li=[]
            self.prod=1
        else:
            self.prod*=num
            self.li.append(self.prod)



        

    def getProduct(self, k: int) -> int:
       n=len(self.li)
       if n<k:
        return 0
       if n==k:
            return self.li[-1]
       return self.li[-1]//self.li[-k-1]