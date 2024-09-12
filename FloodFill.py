class Solution:
    # floodfill algorithm
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # if the image is already a 2, then we don't change it or its neighbors
        # if the initial coordinate is the same as the new color, return the image since it has already been 'filled'
        if image[sr][sc] == color:
            return image
        resultImage = self.fill(image, sr, sc, image[sr][sc], color)
        return resultImage

    # recusive method
    def fill(self, image, sr, sc, oldColor, newColor):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[sr]) or image[sr][sc] != oldColor:
            # if the image is not equal to its oldColor (not equal to one) that means it should not be tampered with as it could be equal to 0 or newColor
            return
        # applies the new color to the coordinate on the image
        image[sr][sc] = newColor

        # calling the function recursively on all 4 sides
        self.fill(image, sr+1, sc, oldColor, newColor)
        self.fill(image, sr-1, sc, oldColor, newColor)
        self.fill(image, sr, sc+1, oldColor, newColor)
        self.fill(image, sr, sc-1, oldColor, newColor)
        return image


# main method (just for test cases)
def main():
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    resultImage = solution.floodFill(image, 1, 1, 2)
    print(resultImage)


# calling the main function
main()
