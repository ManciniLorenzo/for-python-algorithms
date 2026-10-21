# FOR Python Algorithms

Python implementations of the algorithms from Foundations of Operations Research (Politecnico di Milano): graph and network optimization, then LP/ILP.

A learning repo: each file starts as a guided placeholder (problem, assumptions, implementation plan, tests to write, self-check questions) and gets implemented by hand.

## Structure

```text
graphs/
  graph_representation.py   adjacency matrix, successor lists
  reachability_bfs.py       reachability with a FIFO queue (BFS)
  dfs.py                    depth-first search (extra)
  connected_components.py   components of an undirected graph (extra)
  prim.py, kruskal.py       minimum cost spanning tree
  dijkstra.py               shortest paths, non-negative costs
  bellman_ford.py           shortest paths, negative costs (extra)
  floyd_warshall.py         all-pairs shortest paths, negative circuits
  dag_shortest_path.py      topological order + DP, shortest/longest paths
  cpm.py                    project planning, critical path
  ford_fulkerson.py         maximum flow, minimum cut
  dijkstra_attempt_*.py     earlier Dijkstra attempts
linear/                     LP modelling and solver (Chapter 3)
integer/                    ILP modelling (Chapter 4)
```

## Tests

Tests use the built-in `unittest`, one file per algorithm in `tests/test_<algorithm>.py`, added once the algorithm is implemented. Run them from the repo root:

```bash
python3 -m unittest discover -s tests
```
