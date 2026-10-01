class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        # 0 = unvisited
        # 1 = currently visiting
        # 2 = completely processed
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False       # cycle

            if state[course] == 2:
                return True        # already processed

            state[course] = 1

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True