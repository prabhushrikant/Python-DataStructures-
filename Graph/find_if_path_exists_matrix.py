import graph as g

def find_path_exist(graph,s,d):
    path = graph.BFS(s)

    print path

    if d in path:
        return True
    else:
        return False

def is_safe(i, j, matrix):
    if i<0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return False
    return True

def create_graph_from_matrix(matrix):
    k = 1;
    m = len(matrix)
    n = len(matrix[0])
    graph = g.Graph()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                #possible to move only in 4 directions.
                if is_safe(i, j+1, matrix):
                    graph.addEdge(k, k+1);
                if is_safe(i, j-1, matrix):
                    graph.addEdge(k, k-1);
                if j < n and is_safe(i+1, j, matrix):
                    graph.addEdge(k, k+n);  #element below me in matrix will be have vertex no# , n more than me
                if i > 0 and is_safe(i-1, j, matrix):
                    graph.addEdge(k, k-n);  #element below me in matrix will be have vertex no# , n less than me
                #what if allowed to move diagonaly as well
                #then it will be (k,k+n+1), (k,k+n-1), (k,k-n+1), (k,k-n-1)

            #note that this is outside of above if since a node with 0 should also be considered as a graph vertex.
            #without any edges.
            if matrix[i][j] == 1:
                #we found the source.
                s = k

            if matrix[i][j] == 2:
                #we found the destination
                d = k

            #add just the node to graph if there exits no edge
            #coming or going through it.
            if not graph.hasVertex(k):
                graph.addEmptyVertex(k)
            k += 1

    return s,d,graph

#driver program

matrix = [[0,3,0,1],[3,0,3,3],[2,3,3,3],[0,3,3,3]]
s,d, graph = create_graph_from_matrix(matrix)

print find_path_exist(graph, s, d)