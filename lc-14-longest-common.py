from calendar import c


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            print((letter_group))
            print(set(letter_group))
            if len(set(letter_group)) > 1:      
                print (len(set(letter_group)))
                return strs[0][:i]
        else:
            print("else")
            return min(strs)
        
test=Solution()


print(test.longestCommonPrefix(["flower","flow","flight"]))
