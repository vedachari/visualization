import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.DiGraph()

#static graph: add nodes and edges
G.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
])

pos = nx.spring_layout(G)  #layout for visualization

plt.ion()  #for changing figure
fig, ax = plt.subplots(figsize=(8,6))

def visualize(G, pos, path_nodes=[], visited_nodes=[]):
    ax.clear()
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightgray')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    
    nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='yellow', ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='lightgreen', ax=ax)
    
    plt.draw()
    plt.pause(0.5)

# initial graph
visualize(G, pos)

def BFS(G, start):
    q = deque()
    res = []
    visited = {}
    
    visited[start] = True
    q.append(start)

    while q:
        curr = q.popleft()
        res.append(curr)

        visualize(G, pos, [], visited.keys())

        for neighbor in G.neighbors(curr):
            if not visited.get(neighbor, False):
                visited[neighbor] = True
                q.append(neighbor)

    return res

BFS(G, 'A')

plt.ioff()  #turn off interactive mode
plt.show()  #show final state
