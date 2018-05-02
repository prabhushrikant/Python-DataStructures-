import graph as g
from collections import deque

def topological_sort_rec(v, graph, visited, stack):

    visited[v] = True

    for i in graph.graph[v]:
        if not visited[i]:
            topological_sort_rec(i, graph, visited, stack)

    #this is same as postorder, process all adjascent vertices of the current vertex
    #then add it to the stack.
    stack.append(v)

    # return stack

def topological_sort(graph):

    visited = [False for x in range(graph.vertices)]
    stack = []

    for i in range(graph.vertices):
        if not visited[i]:  #this is important.
            topological_sort_rec(i, graph, visited, stack)

    # print stack
    i = len(stack) - 1
    while i >= 0:
        print stack.pop(),
        i -= 1

    print

#method 2 : Kahn's algo
#calculate in-degree for each node,
#add nodes which have zero in-degree in the queue.
#while queue is not empty do this
    #visit all it's neighbors and reduce indegree for each of them,
        # if indegree becomes zero add that node the queue.


def topological_sorting_iterative(graph):

    indegree = [0 for x in range(graph.vertices)]
    q = deque([])

    #find the indegree for each node.
    for i in range(graph.vertices):
        for neighbor in graph.graph[i]:
            indegree[neighbor] += 1

    # print indegree

    #add vertices with indegree of zero to the queue.
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    # print q

    count_visited = 0
    result = []
    while len(q) > 0:
        p = q.popleft()
        count_visited += 1
        result.append(p)

        for neighbor in graph.graph[p]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if count_visited == graph.vertices:
        print result
    else:
        print "There exists a cycle in the graph."

#driver program:
graph = g.Graph(6)
graph.addEdge(5, 2);
graph.addEdge(5, 0);
graph.addEdge(4, 0);
graph.addEdge(4, 1);
graph.addEdge(2, 3);
graph.addEdge(3, 1);

print "Following is a Topological Sort of the given graph - Method 1"
topological_sort(graph)

print "Following is a Topological Sort of the given graph - Method 2"
topological_sorting_iterative(graph)


