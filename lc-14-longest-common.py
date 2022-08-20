from calendar import c


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        prefix_list = ''
        counter = 0
        while True:
            try:
                prefix_list += (strs[0][counter])
            except:
                return (prefix_list)  
 
            for x in strs:
                #print(prefix_list)
                try:
                    if (str(prefix_list) == x[0:counter+1]) is False:
                        
                        return (prefix_list[:-1])
                    
                        
                    
                except:
                    return (prefix_list)  
            
            
            counter += 1
        
test=Solution()


print(test.longestCommonPrefix([""]))
