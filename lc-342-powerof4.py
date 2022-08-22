class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        if n == 1:
            return True
        elif n <= 0:
            return False
        else:
            print(10000 & 1111)
            while 4 ** (x - 1)  < n:
                y = lambda x : 4 ** x
                if y(x) != n:
                    x += 1

                else: 
                    return True




test = Solution()

test.isPowerOfFour(26)