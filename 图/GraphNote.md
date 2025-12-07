### Graph

Discrete Mathmatices
A graph G is an ordered pair of a set V of vertices(nodes) and a set E of edges
**G = (V, E)**

Classification of Graphs
1. Directed: World Wide Web vs Undirected: Social Network
2. Weighted:Intercity road network vs Unweighted

Properties of Graphs
self-loop multiedge

Number of edges:
if |V| = n, then:
    O <= |E| <= n(n-1) if directed
    O <= |E| <= 1/2*n(n-1) if undirected

Strongly Connected Graphs (强连通)

```python
class egde:
    def __init__(self, u, v, w):
        self.u = u  # 边的起点
        self.v = v  # 边的终点
        self.w = w  # 边的权重
```

### Graph Representation

**边列表**
1. Vertex List O(|E|) or O(|V|^2^) costly
2. Edge List  O(|V|) OK

**邻接矩阵**
Adjacency Matrix
A~ij~ = 1 , if exist edge from i to j
A~ij~ = 0 , otherwise

**邻接表**
connections of node: 只保留1，去掉冗余的0

For a social network with a billion (10^9^) users:
    if maximum num of friends = 10000
    if machine can scan 10^6^cells/second
- | Structure-1 (Matrix) | Structure-2
------- | ------ | ------ 
finding adjacent nodes | 10^9^/10^6^=1000sec | 10^4^/10^6^=10^-2^sec
finding if two nodes are connected | 10^-6^sec | 10^-2^sec

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = NOne
A = [Node()] * 8
```
Space Complexity = O(|E|+|V|)