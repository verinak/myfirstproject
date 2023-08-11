def bfs(graph, start, goal):
    visited = []  # list to save visited nodes
    queue = [[start]]
    # queue implemented as list containing a list for each path we explore
    # start with a list with only the start node

    while True:
        path = queue.pop(0)  # pop the first path in the queue 
        node = path[-1]  # explore the last node in the path
        
        # if node already visited, skip it and return to the beginning of the while loop
        if node in visited:
            continue

        visited.append(node) # add node to visited list

        # if node is the goal, print the solution and end the search
        if node == goal:
            print(f'Breadth-First Search\nPath: {path}\nVisited nodes: {visited}\n')
            break
        
        # get adjacent nodes and add a new path for each node in the queue
        adjacent_nodes = graph.get(node)
        for n in adjacent_nodes:
            p = path[:]
            p.append(n)
            queue.append(p)
        
        # queue is empty = there are no more paths to explore = no solution found
        if not queue:
            print('Breadth-First Search found no solution.')
            break
    


def dfs(graph, start, goal):
    visited = []  # list to save visited nodes
    stack = [[start]]
    # stack implemented as list containing a list for each path we explore
    # start with a list with only the start node

    while True:
        path = stack.pop()  # pop the last path in the queue 
        node = path[-1]  # explore the last node in the path

        # if node already visited, skip it and return to the beginning of the while loop
        if node in visited:
            continue

        visited.append(node) # add node to visited list

        # if node is the goal, print the solution and end the search
        if node == goal:
            print(f'Depth-First Search\nPath: {path}\nVisited nodes: {visited}\n')
            break
        
        # get adjacent nodes and add a new path for each node in the stack
        adjacent_nodes = graph.get(node)
        adjacent_nodes.reverse()  # reverse list to explore alphabetically
        for n in adjacent_nodes:
            p = path[:]
            p.append(n)
            stack.append(p)
        
        # stack is empty = there are no more paths to explore = no solution found
        if not stack:
            print('Depth-First Search found no solution.')
            break

