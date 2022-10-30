class Solution:
    def canFinish(self, numCourses: int, edges: List[List[int]]) -> bool:
        edges_dict = defaultdict(list)
        for n, m in edges:
            edges_dict[n].append(m)

        seen = set()

        def dfs(node):

            if node in seen: return False
            # if we don't have any prerequisite
            if edges_dict[node] == []: return True

            seen.add(node)

            for prereq in edges_dict[node]:
                if not dfs(prereq): return False
            
            seen.remove(node)
            edges_dict[node] = []

            return True


