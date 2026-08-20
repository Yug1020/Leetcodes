class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # left = image[sr][sc - 1]
        # top = image[sr - 1][sc]
        # bottom = image[sr + 1][sc]
        # right = image[sr][sc + 1]

        imglen = len(image)
        inlen = len(image[0])
        
        def trie(sr, sc, color):
            image[sr][sc] = color

            if 0 <= sr < len(image) and 0 <= sc - 1 < len(image[0]) and image[sr][sc - 1] == og_color:
                trie(sr, sc - 1, color)
            
            if 0 <= sr - 1 < len(image) and 0 <= sc < len(image[0]) and image[sr - 1][sc] == og_color:
                trie(sr - 1, sc, color)
            
            if 0 <= sr + 1 < len(image) and 0 <= sc < len(image[0]) and image[sr + 1][sc] == og_color:
                trie(sr + 1, sc, color)
            
            if 0 <= sr < len(image) and 0 <= sc + 1 < len(image[0]) and image[sr][sc + 1] == og_color:
                trie(sr, sc + 1, color)

            return image
        
        og_color = image[sr][sc]   
        if og_color == color:
            return image

        return trie(sr, sc, color)