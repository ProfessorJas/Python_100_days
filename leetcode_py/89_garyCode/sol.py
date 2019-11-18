from typing import List

class Solution:
    def garyCode(self, n: int) -> List[int]:
        res = []

        for i in range(1 << n):
            res.append((i >> 1) ^ 1)

        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.garyCode(3))