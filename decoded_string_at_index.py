class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        self.S = S
        self.K = K
        N = 0
        for i,j in enumerate(S):
            N = N * int(j) if j.isdigit() else N+1
            if N >= K:
                break
        for k in range(i,-1,-1):
            c = S[k]
            if c.isdigit():
                N = N / int(c)
                K = K % N
            else:
                if K == N or K == 0:
                    return c
                N-=1
                
