"""
Let us write a program for breadth first search within a graph

"""

class Graph:
    def __init__(self,list):
        self.graph={}
        print(list)
        for i in list:
            print(i[0]," : ",i[1])
            if(i[0] not in list):
             self.graph[i[0]]=[i[1]]
            else:
             self.graph[i[0]].append(i[1])
        print(self.graph) 


edgelist =[(0,1),(0,2),(0,3),(3,4),(1,5),(2,6),(5,6),(6,7),(7,8)]
print(edgelist)
graph = Graph(edgelist)
