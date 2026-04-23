class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)

        WHITE, GREY, BLACK = 0, 1, 2
        color = [WHITE] * numCourses

        def dfs(node):
            if color[node] == GREY:
                return False  # cycle found
            if color[node] == BLACK:
                return True   # already safe

            color[node] = GREY  # enter node

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            color[node] = BLACK 
            return True

        for i in range(numCourses):
            if color[i] == WHITE:
                if not dfs(i):
                    return False

        return True
