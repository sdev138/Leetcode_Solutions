class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        output = 0
        playerIndex = 0
        trainerIndex = 0

        # the lenght of players and trainers are the same
        while playerIndex < len(players) and trainerIndex < len(players):
            if players[playerIndex] <= trainers[trainerIndex]:
                playerIndex += 1
                trainerIndex += 1
                output += 1
            else:
                trainerIndex += 1
        
        return output