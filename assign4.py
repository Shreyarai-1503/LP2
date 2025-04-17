def isSafeToColor(graph, vertex, color, colors_assigned):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors_assigned[i] == color:
            return False
    return True

def printSolution(colors_assigned):
    print("Solution colors are:")
    for color in colors_assigned:
        print(color, end=" ")
    print()

def graphColoringUtil(graph, m, vertex, colors_assigned):
    # If all vertices are assigned a color then return true
    if vertex == len(graph):
        printSolution(colors_assigned)
        return True

    for color in range(1, m + 1):
        if isSafeToColor(graph, vertex, color, colors_assigned):
            colors_assigned[vertex] = color

            # Recursive call
            if graphColoringUtil(graph, m, vertex + 1, colors_assigned):
                return True

            # BACKTRACK
            colors_assigned[vertex] = 0

    return False

def graphColoring(graph, m):
    V = len(graph)
    colors_assigned = [0] * V

    if not graphColoringUtil(graph, m, 0, colors_assigned):
        print("No solution exists.")

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3  # Number of colors

graphColoring(graph, m)

# Output:
'''
Solution colors are:
1 2 3 2
'''