# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 0, n
        mid = n
        
        while l <= r:

            if( isBadVersion(mid) and isBadVersion(mid -1 ) )is True:
                r = mid
            elif isBadVersion(mid) is False:
                l = mid
            else:
                return mid
            mid = (l+r) // 2

    
#easy binary