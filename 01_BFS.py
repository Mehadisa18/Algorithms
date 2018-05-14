"""
Let us write a program for breadth first search within a graph

All the adjacent nodes of a graph or a tree are visited first before going to another level.

we would require a queue which specifies the nest node to be visited.

In python, the order of the list is maintained. so we can use it as a queue.

In this example I have covered all the possibilities...even the Disconnected graph.

This may not be optimized algorithm...but it surely serves the purpose

"""
from collections import defaultdict
class Graph:
    def __init__(self):
        print(self)
    def addEdges(self,edgelist):
        self.graphDict = defaultdict(list)
        for i in edgelist:
           self.graphDict[i[0]].append(i[1])
        print(self.graphDict)
    def BFS(self):
        visitedlist=[]
        visitingqueue =[]
        for node in list(self.graphDict.keys()):
            print("node value: ",node,"nodetype: ",type(node))
            visitedlist = self.visitnode(node,visitedlist,visitingqueue)
        print("Visited List: ",visitedlist)  
    def visitnode(self, node, visitedlist,visitingqueue):
            if node not in visitedlist:
               visitedlist.append(node)
               for x in self.graphDict[node]:
                   if x not in visitedlist and x not in visitingqueue:
                       visitingqueue.append(x)
               print("visiting queue : ",visitingqueue)
               for element in visitingqueue:
                   print("selected element: ",element)
                   visitingqueue.remove(element)
                   if element not in visitedlist: 
                       visitedlist=self.visitnode(element, visitedlist,visitingqueue)   
            return(visitedlist)



edgelist =[('A','C'),('A','B'),('B','C'),('C','B'),('C','D'),('D','E'),('D','F'),('E','G'),('E','F'),('F','E'),('F','D'),('G','E')]
print(edgelist)
graph = Graph()
graph.addEdges(edgelist)
graph.BFS()
edgelist1 =[('A','B'),('B','A'),('B','C'),('C','E'),('C','B'),('C','N'),('E','G'),('G','F'),('E','F'),('D','D')]
graph1 = Graph()
graph1.addEdges(edgelist1)
graph1.BFS()
