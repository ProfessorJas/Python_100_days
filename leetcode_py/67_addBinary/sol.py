class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)

        sum0 = num1 + num2

        return format(sum0, 'b')


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('1010', '1011'))
