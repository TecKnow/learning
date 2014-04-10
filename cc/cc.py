#!/usr/bin/env python3
"""
Problem  : Connected Components
URL      : http://rosalind.info/problems/cc/
Author   : David P. Perkins
"""
def parseEdgeListFormat(elf):
    lines = elf.strip().split("\n")
    nodes, edges = [int(x) for x in lines[0].split()]
    #print("nodes:", nodes, "edges:",edges)
    graph = [[int(x) for x in line.split()] for line in lines[1:]]
    #print(graph)
    return buildAdjacencyList(nodes,edges,graph)

def buildAdjacencyList(nodes, edges, graph):
    adj = {x:set() for x in range(1, nodes+1)}
    for g in graph:
        a, b = g[0],g[1]
        adj[a].add(b)
        adj[b].add(a)
    return adj

def DFSExplore(adjacencyList, vertex, exploredNodes = None):
    if exploredNodes == None:
        exploredNodes = set()
    exploredNodes.add(vertex)
    for x in adjacencyList[vertex]:
        if x not in exploredNodes:
            DFSExplore(adjacencyList, x, exploredNodes)
    return exploredNodes

def DFS(adjacencyList):
    unexplored = set(range(1, max(adjacencyList)+1))
    segments = list()
    while unexplored:
        segment = DFSExplore(adjacencyList, unexplored.pop())
        segments.append(segment)
        unexplored.difference_update(segment)
    return segments
    
if __name__ == "__main__":
    with open("ccIn.txt","r") as infile:
        adj = parseEdgeListFormat(infile.read())
        print(len(DFS(adj)))
        

        
