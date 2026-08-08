class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        
        n=len(s)
        total=0
        stack=[]
        for ch in s:
            if ch==letter:
                total+=1
        
        curr=0
        for i in range(n):
            ch=s[i]

            while stack and stack[-1]>ch:

                if len(stack)+n-i-1<k:
                    break
                if stack[-1]==letter:

                    if total+curr-1<repetition:
                        break
                    curr-=1
                stack.pop()
                    
            if len(stack)<k:
                if ch==letter:
                    stack.append(ch)
                    curr+=1
                else:
                    need=max(0,repetition-curr)
                    if k-len(stack)>need:
                        stack.append(ch)
            if ch==letter:
                    total-=1

        return "".join(stack)

        