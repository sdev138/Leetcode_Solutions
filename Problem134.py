class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # returns the starting point of the array
        startingPoint = 0
        visitedSPs = []

        # while the starting point is not in the visited list
        while startingPoint not in visitedSPs:
            for i in range(startingPoint, len(gas)):
                # calculating the new starting point
                startingPoint += gas[i]
                # if the starting point is at the end of the list, put it to the beginning
                if startingPoint >= len(gas) - 1:
                    startingPoint = 0

        return startingPoint
