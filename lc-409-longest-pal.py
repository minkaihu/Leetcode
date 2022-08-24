class Solution:
    def longestPalindrome(self, s: str) -> int:
        list={}
        #count the amount of syllables, if modulu 2, add to output
        counter = 0
        midchar = False
        if len(s)==0: return 0 
        if len(s)==1: return 1 
        for x in s:
            if x not in list:
                list[x] = s.count(x)
            list_inputa = list


        for x in list_inputa:
            counter += 2 * (list_inputa[x] // 2)
            if midchar == False:
                if (list_inputa[x] % 2 == 1):                
                    midchar = True 

        
        return counter + midchar, print(counter + midchar)


test = Solution()

test.longestPalindrome("abccccdd")


#actually selfwritten with a top 78 time com and top 98% mem, pog.