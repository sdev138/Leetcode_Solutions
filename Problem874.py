class Solution:
    def iterateDirection(
        self, currentPoint, currentDirection, obstacles, command
    ) -> list[int]:
    # use list splicing to check if the point is within a certain range
        if currentDirection == "north":
            i = 0
            while i < command:
                if [currentPoint[0], currentPoint[-1] + 1] in obstacles:
                    break
                currentPoint = [currentPoint[0], currentPoint[-1] + 1]
                i += 1
        elif currentDirection == "south":
            i = 0
            while i < command:
                if [currentPoint[0], currentPoint[-1] - 1] in obstacles:
                    break
                currentPoint = [currentPoint[0], currentPoint[-1] - 1]
                i += 1
        elif currentDirection == "west":
            i = 0
            while i < command:
                if [currentPoint[0] - 1, currentPoint[-1]] in obstacles:
                    break
                currentPoint = [currentPoint[0] - 1, currentPoint[-1]]
                i += 1
        else:  # east
            i = 0
            while i < command:
                if [currentPoint[0] + 1, currentPoint[-1]] in obstacles:
                    break
                currentPoint = [currentPoint[0] + 1, currentPoint[-1]]
                i += 1

        # returning the current point once the algorithm finishes
        return currentPoint

    # main function that will be executed
    # Using the 'list' instead of the 'List' library
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        currentPoint = [0, 0]
        maxDistance = 0
        currentDirection = "north"
        turnRight = {
            "north": "east",
            "east": "south",
            "south": "west",
            "west": "north",
        }
        turnLeft = {
            "north": "west",
            "south": "east",
            "west": "south",
            "east": "north",
        }

        # iterating through the different commands
        for command in commands:
            if command == -1:
                currentDirection = turnRight[currentDirection]
            elif command == -2:
                currentDirection = turnLeft[currentDirection]
            else:
                currentPoint = self.iterateDirection(currentPoint, currentDirection, obstacles, command)

            # Getting the distance from the point and comparing it to previous maxDistance
            maxDistance = max(maxDistance, (currentPoint[0] ** 2) + (currentPoint[1] ** 2))

        return maxDistance
