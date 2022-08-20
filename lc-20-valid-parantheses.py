class Solution:



    



    def isValid(self, s: str) -> bool:
        dictio = { 0:None, '(':')', '[':']', '{':'}'}

        stack = [0]
        for x in s:
            if x in dictio:
                print('stack2', stack)

                stack.append(x)
                print('stack1', stack)
            else:
                if dictio[stack.pop()] != x: return False
        print("outofloop")
        return stack == [0]

test = Solution()

test.isValid("()[]{")