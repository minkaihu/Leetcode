class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listana= {}
        listanb= {}
        for x in s:
            if x not in listana:
                listana[x] = s.count(x)
            list_inputa = listana
        for x in t:

            if x not in listanb:
                listanb[x] = t.count(x)
            list_inputb = listanb

        return True if list_inputa == list_inputb else False













test = Solution()

test.isAnagram("hehehea")


