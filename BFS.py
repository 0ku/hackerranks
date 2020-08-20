n = int(input())

def solve(graph,start):
    queue = []
    dist = {}
    prev = {}
    for a in graph.keys():
        dist[a] = 9999999999
        queue.append(a)
    dist[start] = 0
    while len(queue) > 0:
        currentMin = 9999999999
        currentNode = None
        for node in queue:
            if dist[node] < currentMin:
                currentNode = node
        if currentNode == None:
            return dist
        else:
            queue.remove(currentNode)
        for nextNode in graph[currentNode]:
            currentDistance = dist[currentNode] + 6
            if currentDistance < dist[nextNode]:
                dist[nextNode] = currentDistance
    return dist

results = []
for a in range(0,n):
    graph = {}
    nodes,edges = map(int,input().split(" "))
    for n in range(1,nodes+1):
        graph[n] = []
    for b in range(0,edges):
        node1,node2 = map(int,input().split(" "))
        graph[node1].append(node2)
        graph[node2].append(node1)
    start = int(input())
    solution = solve(graph,start)
    del solution[start]
    {k: v for k, v in sorted(solution.items(), key=lambda item: item[1])}
    finalString = ""
    for c in solution.keys():
        if solution[c] == 9999999999:
            finalString += "-1 "
        else:
            finalString+=f"{solution[c]} "
    finalString[:-1]
    results.append(finalString)


for a in results:
    print(a)


            


