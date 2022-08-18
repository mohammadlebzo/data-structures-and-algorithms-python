# Graphs
<!-- Short summary or background information -->
Graphs are non-linear data structure that consist of a set of nodes that are connected by edges.

## Challenge
<!-- Description of the challenge -->
**Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:**

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I took a linear approach throughout all methods, as for the Big O:

- add node:
  - **Time**: O(1)
  - **Space**: O(1)

- add edge:
  - **Time**: O(1)
  - **Space**: O(1)

- get nodes:
  - **Time**: O(1)
  - **Space**: O(1)

- get neighbors:
  - **Time**: O(1)
  - **Space**: O(1)

- size:
  - **Time**: O(1)
  - **Space**: O(1)

## API
<!-- Description of each method publicly available in your Graph -->

- **add_node()**: adds a node to the graph.
- **add_edge()**: adds an edge to connect two nodes within a graph.
- **get nodes()**: returns all nodes within the graph.
- **get neighbors()**: returns all the connected nodes for the passed node.
- **size()**: returns the number of the nodes within the graph
