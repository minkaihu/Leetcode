class Solution:
    def isPalindrome(self, s: str) -> bool:
        whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
 
        if s:
            string1 = s
            string2 = s[::-1]
            string1 = ''.join(filter(whitelist.__contains__, string1))
            string2 = ''.join(filter(whitelist.__contains__, string2))
            string1 = string1.lower()
            string2 = string2.lower()

            print(string1,string2)
            if string1 == string2:
                return True
            else: False
        else:
            return True



test = Solution()

test.isPalindrome("0P")