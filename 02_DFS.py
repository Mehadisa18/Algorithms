"""
Lets start with a notes on depth first search

As the name suggests the search goes deep and deep...
if it is a tree the complexity is less as we can travel only in one direction downwards towards the children
In case of graphs, infinite looping might occur during traversal..so a list of visited nodes is maintained to 
avoid this phenomenon

Here I implement DFS algorithm in python.

Cases to be covered :
1. DFS in Directed graphs
2. DFS in undirected graphs
3. DFS with leftout vertices (disconnected vertices) """

""" we would need a graph class for storing current status of the graph.

let us assume the elements are named after alphabets. An edge defines the connection between two nodes """
from collections import defaultdict
class graph:
    def __init__(self):  
       print(self)
    def addEdges(self,list1):
        self.graphDict = defaultdict(list)
        for edge in list1:
            self.graphDict[edge[0]].append(edge[1])
        print(self.graphDict) # successfully created the graph
    def DFS(self):
        visitedlist = []
        for node in list(self.graphDict.keys()): # weird way to iterate over keys of a dictionary
           #print(visitedlist)
           visitedlist= self.visitnode(node,visitedlist)
    def visitnode(self,node,visitedlist):
        if(node not in visitedlist):
               visitedlist.append(node)
               print("Visited: ",node)
               print("choose among: ",self.graphDict[node])
               for i in self.graphDict[node]:
                   visitedlist = self.visitnode(i,visitedlist)
               #print("visited list ",visitedlist)
        return visitedlist


undirectedEdgeList = [('A','B'),('A','C'),('B','A'),('B','E'),('C','E'),('C','A'),('D','E'),('E','F'),('E','D'),('E','C'),('E','B'),('F','G')]
undirectedGraph = graph()
undirectedGraph.addEdges(undirectedEdgeList)
undirectedGraph.DFS()

directedEdgeList = [('A','B'),('B','C'),('D','C'),('C','E'),('F','E'),('D','F')]
directedGraph = graph()
directedGraph.addEdges(directedEdgeList)
directedGraph.DFS()