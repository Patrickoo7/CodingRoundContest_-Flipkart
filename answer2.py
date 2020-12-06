# Python3 program to find Maximum sum 
# of values of nodes among all connected 
# components of an undirected graph 
import sys 

graph = [[] for i in range(1001)] 
visited = [False] * (1001 + 1) 
sum = 0

# Function to implement DFS 
def depthFirst(v, values): 
	
	global sum
	
	# Marking the visited vertex as true 
	visited[v] = True

	# Updating the value of connection 
	sum += values[v - 1] 

	# Traverse for all adjacent nodes 
	for i in graph[v]: 
		if (visited[i] == False): 

			# Recursive call to the 
			# DFS algorithm 
			depthFirst(i, values) 

def maximumSumOfValues(vertices,values): 
	
	global sum
	
	# Initializing boolean array to 
	# mark visited vertices 

	# maxChain stores the maximum chain size 
	maxValueSum = -sys.maxsize - 1

	# Following loop invokes DFS algorithm 
	for i in range(1, vertices + 1): 
		if (visited[i] == False): 

			# Variable to hold temporary values 
			# sum = 0 

			# DFS algorithm 
			depthFirst(i, values) 

			# Conditional to update max value 
			if (sum > maxValueSum): 
				maxValueSum = sum
				
			sum = 0
			
	# Printing the heaviest chain value 
	print("Max Sum value = ", end = "") 
	print(maxValueSum) 

# Driver code 
if __name__ == '__main__': 
	
	# Initializing graph in the 
	# form of adjacency list 

	# Defining the number of 
	# edges and vertices 
	E = 4
	V = 7

	# Assigning the values for each 
	# vertex of the undirected graph 
	values = [] 
	values.append(10) 
	values.append(25) 
	values.append(5) 
	values.append(15) 
	values.append(5) 
	values.append(20) 
	values.append(0) 

	# Constructing the undirected graph 
	graph[1].append(2) 
	graph[2].append(1) 
	graph[3].append(4) 
	graph[4].append(3) 
	graph[3].append(5) 
	graph[5].append(3) 
	graph[6].append(7) 
	graph[7].append(6) 

	maximumSumOfValues(V, values)