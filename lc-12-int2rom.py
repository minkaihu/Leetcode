class Solution:
    INT_TO_ROMAN = {
        1 : 'I',
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    reversed_INT2ROMAN = (dict(reversed(list(INT_TO_ROMAN.items()))))

    def intToRoman(self, num: int) -> str:
        
        converted = ''
        for xind, (xnum, xrom) in enumerate(self.reversed_INT2ROMAN.items()):
            modulu_result = num // xnum 
            converted += xrom * modulu_result
            num -= xnum * modulu_result
        return converted







test = Solution()

print (test.intToRoman(1994))



