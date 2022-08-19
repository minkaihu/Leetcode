

class Solution:
    def romanToInt(self, s: str) -> int:
        string_list = [x for x in s]
        int_list = [None] * len (string_list)

        for xind, x in enumerate(string_list):
            if x == 'M':
                int_list [xind] = 1000
            elif x == 'D':
                int_list [xind] = 500
            elif x == 'C':
                int_list [xind] = 100
            elif x == 'L':
                int_list [xind] = 50
            elif x == 'X':
                int_list [xind] = 10
            elif x == 'V':
                int_list [xind] = 5
            elif x == 'I':
                int_list [xind] = 1
        
        #DP 
        sum = 0
        print (int_list)
        for xind, x in enumerate (int_list):
            if xind == len(int_list) - 1 :
                if int_list [xind - 1 ] < int_list[xind ]:
                    break
                else:
                    sum += x
            elif int_list [xind] < int_list[xind + 1]:

                sum +=  abs (x - int_list[xind + 1 ] )


  
            elif int_list [xind - 1 ] < int_list[xind ] and xind != 0:

                continue
            elif int_list [xind] >= int_list[xind + 1 ]:
                sum += x



        return (sum)    


test = Solution()

print (test.romanToInt("III"))



