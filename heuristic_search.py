# Heuristic Search - AI assignment 2
# Verina Michel Asham - 20221440977

# graph is implemented as dictionary, where keys are nodes, and values are tuples of children and their g(n) function
graph = {
    'A':[('B',5), ('C',4)],
    'B':[('C',2), ('G',5)],
    'C':[('A',4),('B',2), ('D',6)],
    'D':[('B',3), ('C',6), ('G',2)]
}
# h(n) of each node
H_table = {
    'A':28,
    'B':30,
    'C':20,
    'D':40,
    'G':0
}


# functions to calculate g(n), h(n), and f(n)

def path_h_cost(path):
    last_node = path[-1][0]
    return H_table[last_node]

def path_g_cost(path):
    g_cost = 0
    for n in path:
        g_cost = g_cost + n[1]
    return g_cost

def path_f_cost(path):
    f = path_g_cost(path) + path_h_cost(path)
    return f


##########

def Greedy_Search(graph, start, goal):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=path_h_cost)  # sort paths bed on last node's h(n)
        path = queue.pop(0) # pop the first path in the queue 
        node = path[-1][0] # explore the last node in the path

        # if node already visited, skip it and return to the beginning of the loop
        if node in visited:
            continue
        
        queue.clear() # clear other nodes in queue because greeedy search explores only the lowest h(n)
        visited.append(node)  # add node to visited list
        
        # if node is the goal, return the solution and end the search
        if node == goal:
            return path, path_g_cost(path), visited
        else:
            # get adjacent nodes and add a new path for each node in the queue
            adjacent_nodes = graph.get(node, [])  # return empty list by default if node not found in dict
            for(n, g) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((n, g))
                queue.append(new_path)

##########

def Hillclimbing_Search(graph, start, goal):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=path_h_cost)  # sort paths bed on last node's h(n)
        path = queue.pop(0) # pop the first path in the queue 
        node = path[-1][0] # explore the last node in the path

        # if node already visited, skip it and return to the beginning of the loop
        if node in visited:
            continue
        
        visited.append(node)  # add node to visited list
        
        # if node is the goal, return the solution and end the search
        if node == goal:
            return path, path_g_cost(path), visited
        else:
            # get adjacent nodes and add a new path for each node in the queue
            adjacent_nodes = graph.get(node, [])  # return empty list by default if node not found in dict
            for(n, g) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((n, g))
                queue.append(new_path)

##########

def AStar_Search(graph, start, goal):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=path_f_cost)  # sort paths bed on last node's f(n)
        path = queue.pop(0) # pop the first path in the queue 
        node = path[-1][0] # explore the last node in the path
        
        # if node already visited, skip it and return to the beginning of the loop
        if node in visited:
            continue
        
        visited.append(node)  # add node to visited list
        
        # if node is the goal, return the solution and end the search
        if node == goal:
            return path, path_g_cost(path), visited
        else:
            # get adjacent nodes and add a new path for each node in the queue
            adjacent_nodes = graph.get(node, [])  # return empty list by default if node not found in dict
            for(n, g) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((n, g))
                queue.append(new_path)

##########

def Uniform_Search(graph, start, goal):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=path_g_cost)  # sort paths bed on last node's g(n)
        path = queue.pop(0) # pop the first path in the queue 
        node = path[-1][0] # explore the last node in the path
        
        # if node already visited, skip it and return to the beginning of the loop
        if node in visited:
            continue
        
        visited.append(node)  # add node to visited list
        
        # if node is the goal, return the solution and end the search
        if node == goal:
            return path, path_g_cost(path), visited
        else:
            # get adjacent nodes and add a new path for each node in the queue
            adjacent_nodes = graph.get(node, [])  # return empty list by default if node not found in dict
            for(n, g) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((n, g))
                queue.append(new_path)

##########

print("Greedy Best-First Search:")
sol = Greedy_Search(graph=graph, start='A', goal='G')
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()

print("Hill-Climbing Search:")
sol = Hillclimbing_Search(graph=graph, start='A', goal='G')
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()

print("A* Search:")
sol = AStar_Search(graph=graph, start='A', goal='G')
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()



print("Uniform Cost Search:")
sol = Uniform_Search(graph=graph, start='A', goal='G')
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()
