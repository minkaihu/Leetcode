class Solution:
    def floodFill(self, image, sr: int, sc: int, new_color: int) :
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]
        
        def isNotValidPixel(row,col):
            return (
                row < 0 or row >= rows or
                col < 0 or col >= cols )
        
        def isNotValidColor(row,col):
            return (
                image[row][col] == new_color or
                image[row][col] != color )
        
        def dfs(row,col):
            if isNotValidPixel(row,col): return
            if isNotValidColor(row,col): return
            
            image[row][col] = new_color
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        
        dfs(sr,sc)
        return image
test= Solution()
test.floodFill( [[1,1,1],[1,1,0],[1,0,1]], sr = 0, sc = 0, new_color = 2)