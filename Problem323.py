from collections import defaultdict

# turned List to list in the parameters section for testing purposes
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        # dfs alg
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        components = 0

        # check each node, if not visited, its a new component
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components

def main():
    solution = Solution()
    print(solution.countComponents(5, [[0,1], [1,2], [3,4]])) 

main()