class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # if the image is already a 2, then we don't change it or its neighbors
        if image[sr][sc] == color:
            return image
        resultImage = self.fill(image, sr, sc, image[sr][sc], color)
        return resultImage

    # recusive method
    def fill(self, image, sr, sc, oldColor, newColor):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[sr]) or image[sr][sc] != oldColor:
            # if the image is not equal to its oldColor (not equal to one) that means it should not be tampered with as it could be equal to 0 or newColor
            return 
        image[sr][sc] = newColor
        self.fill(image, sr+1, sc, oldColor, newColor)
        self.fill(image, sr-1, sc, oldColor, newColor)
        self.fill(image, sr, sc+1, oldColor, newColor)
        self.fill(image, sr, sc-1, oldColor, newColor)
        return image

def main():
    solution = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    resultImage = solution.floodFill(image, 1, 1, 2)
    print(resultImage)

# calling the main function
main()