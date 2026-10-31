class RandomizedCollection:

    def __init__(self):

        self.pos=defaultdict(set)
        self.nums=[]
         

    def insert(self, val: int) -> bool:
        
        fl= not self.pos[val]

        self.pos[val].add(len(self.nums))
        self.nums.append(val)

        return fl


        

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False
        
        idx=self.pos[val].pop()

        last_val=self.nums[-1]
        last_idx=len(self.nums)-1

        self.nums[idx]=last_val

        self.pos[last_val].add(idx)
        self.pos[last_val].remove(last_idx)

        self.nums.pop()

        
        return True

        

    def getRandom(self) -> int:

        return random.choice(self.nums)

        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()