# Python Program for union-find algorithm to detect cycle in a undirected graph
from collections import defaultdict
debug = False

#This class represents a undirected graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # function to remove edge from Graph
    def removeEdge(self,u,v):
        del self.graph[u][-1]

    # A utility function to find the subset of an element i
    def find_parent(self, parent,i):
        if parent[i] == -1:
            return i
        if parent[i]!= -1:
             return self.find_parent(parent,parent[i])

    # A utility function to do union of two subsets
    def union(self,parent,x,y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1]*(self.V)
        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent,x,y)

    def node_hash(self, keys):
        # Function to transform graphs where Nodes are Chars instead of Ints
        self.str_hash = {}
        node = 0
        for key in keys:
            # if the key is a string and its still not in ditct
            if str(key) == key and self.str_hash.get(key, 'No Key') == 'No Key':
                self.str_hash[key] = node
                node += 1;
            elif int(key) == key: # if key is a Int
                self.str_hash[key] = key


    def reverse_hash(self, value):
        # Function to obtain key name from value in dict
        for key in self.str_hash:
            if self.str_hash[key] == value:
                return key

    def adjacency_list(self):
        # Creates Adjacent List to present results
        self.adj_list = defaultdict(list)
        for min_edge in self.mst:
            self.adj_list[min_edge[0]].append((min_edge[1],min_edge[2]))


    def KruskalMST(self):
    # Kruskal’s Minimum Spanning Tree Algorithm
        self.mst = [] # Minimum Spanning Tree
        for w,s,d in zip(self.weight,self.src,self.dest):
            self.addEdge(s,d) # Add a new edge to graph
            if self.isCyclic(): # If edge added makes a cycle, reject
                self.removeEdge(s,d)
                if debug: print("Graph contains cycle")
            else : # if no cycle, add edge to minimum spanning tree
                self.mst.append([self.reverse_hash(s), self.reverse_hash(d), w])
                if debug: print ("Graph does not contain cycle ")
        return(self.adjacency_list())

    def order_edges(self, graph_adj_list):
        # Initiate Variables
        self.src, self.dest, self.weight = [],[],[]
        for key, content in graph_adj_list.items():
            for entry in content:
                self.src.append(self.str_hash[key])
                self.dest.append(self.str_hash[entry[0]])
                self.weight.append(entry[1])
        # return weight, src, dest sorted by edge weight
        self.weight, self.src, self.dest  = zip(*sorted(zip(self.weight, self.src, self.dest)))


def question3(G):
    g = Graph(len(G)) # Create a graph with given adjacency list
    g.node_hash(G.keys()) # Hash node names, in case they are strigs
    g.order_edges(G) # Order all edges by weight, ascending order
    g.KruskalMST() # Run Kruska Greedy Algorith
    return dict(g.adj_list) # Put together final adjacency List with MST


def main():
    G1 = {0: [(1,4),(7,8)],
        1: [(2,8),(7,11)],
        2: [(3,7),(8,2),(5,4)],
        3: [(4,9),(5,14)],
        4: [(5,10)],
        5: [(6,2)],
        6: [(8,6),(7,1)],
        7: [(8,7)],
        8: []}
    G = {'A': [('B', 2)],
          'B': [('A', 2), ('C', 5)],
          'C': [('B', 5)]}

    print(question3(G))

if __name__ == '__main__':
    main()
