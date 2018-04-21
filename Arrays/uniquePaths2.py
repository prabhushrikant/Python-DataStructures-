class Solution(object):

    paths = []

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        self.uniquePathsRec(obstacleGrid, m,n,0,0,[(0,0)])

        # print self.paths
        return len(self.paths)

    def uniquePathsRec(self, G, m, n,i,j,path):
        if i == m-1 and j == n-1:
            path.append((i,j))
            self.paths.append(path)
        else:
            if i+1 < m and j < n and G[i+1][j] != 1:
                path1 = list(path)
                path1.append((i+1,j))
                self.uniquePathsRec(G, m,n,i+1,j,path1)

            if i < m and j+1 < n and G[i][j+1] != 1:
                if path is None:
                    print i, j
                path2 = list(path)
                path2.append((i,j+1))
                self.uniquePathsRec(G, m,n,i,j+1,path2)


if __name__ == '__main__':
    sol = Solution()

    obstacleGrid = [[0,0,0],[0,1,0],[1,0,0]]

    sol.uniquePathsWithObstacles(obstacleGrid)

    print "no of paths : " + str(len(sol.paths))
    print sol.paths
