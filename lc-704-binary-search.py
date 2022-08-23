
class Solution:
    def search(self, nums, target: int) -> int:
        

        
        self.newlistleft = nums
        self.newlistright = nums
        position = 0
        if len(self.newlistleft) == 1:
            return 0 if self.newlistleft[0] == target else -1

        while len(self.newlistleft) >= 1:

            self.newlistleft = nums
            self.newlistright = nums
            splitter = len(self.newlistleft)/2
            self.newlistleft = self.newlistleft[:int(splitter)]
            self.newlistright = self.newlistright[int(splitter):]
            
            position += splitter
            print(len(self.newlistleft))
            if (len(self.newlistleft)) == 0:
                return 0 if self.newlistright[0] == target else -1




            if target == self.newlistleft[-1] and len(self.newlistleft) >0:
                print("target", target, self.newlistleft)
                print("yes targetl")
                print(position)
                return int(position) -1 
            elif target == self.newlistright[0]and len(self.newlistright) >0:
                print("yes targetr")
                print(position)
                return int(position) +1

            elif (target <= int(self.newlistleft[-1])) and len(self.newlistleft) > 0:
                print("check left")
                print(position)

                print(self.newlistleft)
                nums = self.newlistleft
                position -= splitter +1
                print(position, "minus")
                continue
            elif (target >= int(self.newlistright[0])) and len(self.newlistright) > 0: 
                print("check")
                print("position",position, splitter)

                nums = self.newlistright
                print(len(self.newlistright))
                continue
            else:
                print("elsefail")
                nums = self.newlistright
            self.newlistleft = nums
            self.newlistright = nums
            print((target >= int(self.newlistright[0])) and len(self.newlistright) > 0)

        print("fail")
        return -1
        


test= Solution()
test.search( [-1,0,3,5,9,12],
-1)