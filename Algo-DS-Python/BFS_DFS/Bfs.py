graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  ans = []

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    ans.append(m) 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

  print('ans: ',ans)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling


'''
d = {}
d.update({'2':['1','2','3']})
print(d) #{'2': ['1', '2', '3']}
'''