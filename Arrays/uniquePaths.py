class Solution(object):
    paths = []

    def uniquePathsRec(self, m, n,i,j,path):
        if i == m-1 and j == n-1:
            path.append((i,j))
            self.paths.append(path)
        else:
            if i+1 < m and j < n:
                path1 = list(path)
                path1.append((i+1,j))
                self.uniquePathsRec(m,n,i+1,j,path1)

            if i < m and j+1 < n:
                if path is None:
                    print i, j
                path2 = list(path)
                path2.append((i,j+1))
                self.uniquePathsRec(m,n,i,j+1,path2)

if __name__ == '__main__':
    sol = Solution()
    sol.uniquePathsRec(2,3,0,0,[(0,0)])
    print sol.paths
