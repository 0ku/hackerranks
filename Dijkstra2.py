n = int(input())

def dijkstra(graph,start):
    queue = []
    dist = {}
    for a in graph.keys():
        queue.append(a)
        dist[a] = 99999999999
    dist[start] = 0
    while len(queue) > 0:
        currentNode = None
        for a in queue:
            if currentNode == None:
                currentNode = a
            elif dist[a] < dist[currentNode]:
                currentNode = a
        queue.remove(currentNode)
        for nextNode in graph[currentNode]:
            alt = dist[currentNode] + nextNode[1]
            if alt < dist[nextNode[0]]:
                dist[nextNode[0]] = alt
    return dist
for case in range(0,n):
    graph = {}
    nodes, edges = map(int,input().split(" "))
    for a in range(1,nodes+1):
        graph[a] = []
    for edge in range(0,edges):
        node1,node2,cost = map(int,input().split(" "))
        graph[node1].append([node2,cost])
        graph[node2].append([node1,cost])
    start = int(input())
    solution = dijkstra(graph,start)
    
    del solution[start]
    finalString = ""
    for node in solution.keys():
        if solution[node] >= 9000000:
            finalString+="-1 "
        else:
            finalString+=f"{solution[node]} "
        finalString[:-1]

    print(finalString)
