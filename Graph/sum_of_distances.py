#leetcode problem
# https://leetcode.com/problems/sum-of-distances-in-tree/description/

from collections import defaultdict

class Solution(object):

    graph = None
    vertices = []
    global_sum = 0

    def DFS(self, vertex, summ, visited):

        visited[vertex] = True
        # print visited

        for i in self.graph[vertex]:
            if not visited[i]:
                self.DFS(i,summ+1, visited)

        self.global_sum += summ

    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        self.graph = defaultdict(list)

        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        # print self.graph

        self.vertices = self.graph.keys()
        # print self.vertices

        res = [0] * N

        for vertex in self.vertices:
            summ = 0
            self.global_sum = 0
            visited = [False] * len(self.vertices)
            self.DFS(vertex, summ, visited)
            res[vertex] = self.global_sum

        return res

N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
sol = Solution()
result = sol.sumOfDistancesInTree(N, edges)
print result

N = 1
edges = [] #graph with no edges and sngle node
sol = Solution()
result = sol.sumOfDistancesInTree(N, edges)
print result

