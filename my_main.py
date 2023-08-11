import uninformed_search as us, heuristic_search as hs

# graph for uninformed search

# graph : Search Sheet 1, ex 1
# graph is implemented as a dictionary: keys = nodes, values = list of adjacent nodes
graph1 = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['G', 'H'],
    'D':['F'],
    'E':[],
    'F':['K', 'L'],
    'G':[],
    'H':['I', 'J'],
    'I':[],
    'J':[],
    'K':[],
    'L':[]
}

# graph for informed search

# graph is implemented as dictionary, where keys are nodes, and values are tuples of children and their g(n) function
graph2 = {
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

#############

## try uninformed search

us.bfs(graph1, 'A', 'G')
us.dfs(graph1, 'A', 'G')


## try informed search


print("Greedy Best-First Search:")
sol = hs.Greedy_Search(graph=graph2, start='A', goal='G', H_table=H_table)
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()

print("Hill-Climbing Search:")
sol = hs.Hillclimbing_Search(graph=graph2, start='A', goal='G', H_table=H_table)
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()

print("A* Search:")
sol = hs.AStar_Search(graph=graph2, start='A', goal='G', H_table=H_table)
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()



print("Uniform Cost Search:")
sol = hs.Uniform_Search(graph=graph2, start='A', goal='G')
print("Path found: ", [n[0] for n in sol[0]])
print("Cost: ", sol[1])
print("Visited nodes: ", sol[2])
print()

