
def find_shortest_path_weight():
    node = find_lowest_cost_node(costs)  # find node with lowest costs from not processed nodes
    shortest_path_weigh = costs[node]
    while node is not None:  # if all nodes are processed cycle is finished
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # loop all neighbors of current node
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # if it is possible to get to the neighbor with lower cost via current node ...
                costs[n] = new_cost  # ... so update cost  for this node
                parents[n] = node  # this node becomes new parent for the neighbor
        processed.append(node)  # mark the node as processed
        node = find_lowest_cost_node(costs)  # find next node for processing and repeat the cycle
        if node is not None:
            shortest_path_weigh = costs[node]
    return shortest_path_weigh

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 1 nodes and neighbors
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# 2 Costs
infinity = float("inf")  # here we get infinity number to determine the weight of end node
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 3 Parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 4 Processed
processed = []

print("Shortest path weight is: " + str(find_shortest_path_weight()))
