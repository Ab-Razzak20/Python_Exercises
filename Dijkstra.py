class Dijkstra:
    def __init__(self, graph, start_node, end_node):
        '''SAVE each of the 3 arguments as class attributes for further use'''
        self.graph = graph
        self.start = start_node
        self.end = end_node
        self.nodes = list(graph.keys())  # Simplified initialization of nodes
        # for node in self.graph:
        #     self.nodes.append(node)

    def _initialize(self):
        self.node_val = [float('inf')] * len(self.nodes)
        # self.node_val = []  
        # for node in self.nodes:
        #     self.node_val.append(float('inf'))  
        
        start_ind = self.nodes.index(self.start)
        self.node_val[start_ind] = 0 
        self.base_val = 0 # captures the current node's base value
        
        self.visited = [False] * len(self.nodes)
        # self.visited = []  
        # for i in range(len(self.nodes)):
        #     self.visited.append(False)
        self.visited[start_ind] = True 
        self.route = {} # this class attribute will be used to give out the final path.

    def _get_neighbours(self, node):
        # if not node in self.graph:
        #     raise ValueError('{} is not found in the graph'.format(node))
        return self.graph[node]
    
    def _visited_node(self, node):
        # if not node in self.graph:
        #     raise ValueError('{} is not found in the graph'.format(node))
        self.visited[self.nodes.index(node)] = True # sets the visited attribute of the node as True

    def _check_visited(self, node):
        # if not node in self.graph:
        #     raise ValueError('{} is not found in the graph'.format(node))
        return self.visited[self.nodes.index(node)]
    
    def _is_neighbour(self, node_1, node_2):
        ''' returns True in case node_2 is a neighbour of node_1, 
            else returns False.'''
        return node_2 in self.graph[node_1]
    
    def _update_node_val(self, current_node):
        '''sets the node_val attribute of the neighbour node 
        to the minimum of the previous value it had
        '''
        neighbours_dict = self._get_neighbours(current_node)	
        
        for adjacent_vertex, weight in neighbours_dict.items():
            # current_node_ind = self.nodes.index(current_node)
            adjacent_vertex_ind = self.nodes.index(adjacent_vertex)
            new_distance = self.base_val + weight # current value of the base_val attribute plus the edge weight of going from current_node to this neighbour node
                
            if not self._check_visited(adjacent_vertex) and\
                  new_distance < self.node_val[adjacent_vertex_ind]:
                self.node_val[adjacent_vertex_ind] = new_distance # updating
                self.route[adjacent_vertex] = current_node

    def _get_min_val(self):
        min_node_val = float("inf")
        # min_node = None
        
        for node in self.nodes:
            node_index = self.nodes.index(node)
            if not self.visited[node_index] and self.node_val[node_index] < min_node_val:
                min_node_val = self.node_val[node_index]
                # min_node = node

        # for val, visit_status in zip(self.node_val, self.visited):
        #     if not visit_status and val < min_node_val:
        #         min_node_val = val
        return min_node_val

    def _next_node(self, current_node):
        self._update_node_val(current_node)
        # min_val = self._get_min_val()
        # next_node = self.nodes[self.node_val.index(min_val)]

        min_node_val = float("inf")
        next_node = None
        for node in self.nodes:
            if not self._check_visited(node) and self.node_val[self.nodes.index(node)] < min_node_val:
                min_node_val = self.node_val[self.nodes.index(node)]
                next_node = node
        
        if next_node is not None:
            self.base_val = self.node_val[self.nodes.index(next_node)]
            self._visited_node(next_node)
        
        return next_node
    

    def find_path(self):
        self._initialize()
        current_node = self.start

        while current_node != self.end:
            current_node = self._next_node(current_node)
            #if current_node is None:  # No path found
                #return None


        # Reconstructing the path
        path = []
        current_node = self.end
        while current_node != self.start:
            path.append(current_node)
            current_node = self.route.get(current_node)
            #if current_node is None:  # Broken path
               # return None

        path.append(self.start)
        path.reverse()
        
        return path
      
if __name__ == '__main__':
    graph = {   
                'A' : {'D' : 1 , 'C' : 2 ,}, 
                'B' : {} ,
                'C' : {'D' : 1, 'F' : 2},
                'D' : {'B' : 5, 'F' : 6, 'E' : 1, "G" : 5},
                'E' : {'B' : 1},
                'F' : {'G' : 10},
                'G' : {'E' : 3},

            }
    
    dijkstra_instance = Dijkstra(graph, "A", "B")
    # print(dijkstra_instance.nodes)
    # dijkstra_instance._initialize()
    # print(dijkstra_instance.node_val)
    # dijkstra_instance._update_node_val('A')
  
    # print(dijkstra_instance.node_val)
    # # print(dijkstra_instance._get_min_val())

    # print(dijkstra_instance.route)
    print(dijkstra_instance.find_path())


    

