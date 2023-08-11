# functions to calculate g(n), h(n), and f(n)

def path_h_cost(path, H_table):
    last_node = path[-1][0]
    return H_table[last_node]

def path_g_cost(path):
    g_cost = 0
    for n in path:
        g_cost = g_cost + n[1]
    return g_cost

def path_f_cost(path, H_table):
    f = path_g_cost(path) + path_h_cost(path, H_table)
    return f


##########

def Greedy_Search(graph, start, goal, H_table):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=lambda x: path_h_cost(x, H_table))  # sort paths bed on last node's h(n)
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

def Hillclimbing_Search(graph, start, goal, H_table):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=lambda x: path_h_cost(x, H_table))  # sort paths bed on last node's h(n)
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

def AStar_Search(graph, start, goal, H_table):
    visited = []    # list of visited nodes
    queue = [[(start,0)]]   # List containing a list for each path we expand

    # while queue is not empty..
    while queue:
        print("Queue: ", queue)
        queue.sort(key=lambda x: path_f_cost(x, H_table))  # sort paths bed on last node's f(n)
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

