import random

class Vertex:
    def __init__(self, key):
        self.key = key              # Station code (e.g., NS16)
        self.data = None            # Station name
        self.edges = []            # List of Edge objects
        self.parent = None         # For path reconstruction
        self.color = 'white'       # For BFS (white = unvisited)
        self.distance = float('inf')  # For BFS or Dijkstra

    def display(self):
        print("Station Information")
        print("=" * 40)
        print(f"Code     : {self.key}")
        print(f"Name     : {self.data}")
        print(f"Distance : {self.distance}")
        print("Connections:")
        for e in self.edges:
            print(f"  - to {e.connection.key} ({e.weight} min)")
        print("=" * 40)


class Edge:
    def __init__(self, connection, weight=1):
        self.connection = connection  # Connected Vertex
        self.weight = weight          # Travel time in minutes


class Graph:
    def __init__(self):
        self.vertices = {}  # key: station code, value: Vertex
        self.start = None

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)
        return self.vertices[key]

    def connect(self, key1, key2, weight=1):
        v1 = self.add_vertex(key1)
        v2 = self.add_vertex(key2)
        v1.edges.append(Edge(v2, weight))
        v2.edges.append(Edge(v1, weight))

    def init_search(self):
        for v in self.vertices.values():
            v.parent = None
            v.distance = float('inf')
            v.color = 'white'

    def bfs(self, start):
        if start not in self.vertices:
            print(f"Station '{start}' not found.")
            return

        self.init_search()
        self.start = start
        source = self.vertices[start]
        source.distance = 0
        source.color = 'gray'
        queue = [source]

        while queue:
            current = queue.pop(0)
            current.color = 'black'
            for edge in current.edges:
                neighbor = edge.connection
                if neighbor.color == 'white':
                    neighbor.color = 'gray'
                    neighbor.distance = current.distance + 1
                    neighbor.parent = current
                    queue.append(neighbor)

    def bfs_path(self, dest):
        if dest not in self.vertices:
            print(f"Destination '{dest}' not found.")
            return

        v = self.vertices[dest]
        if v.parent is None and dest != self.start:
            print("No path found.")
            return

        path = []
        while v is not None:
            path.append(v)
            v = v.parent

        path.reverse()
        print("Shortest path (fewest stops):")
        print(" -> ".join([node.data for node in path]))
        print(f"Total Stops: {len(path) - 1}")

    def dijkstra(self, start):
        if start not in self.vertices:
            print(f"Station '{start}' not found.")
            return

        self.init_search()
        self.start = start
        source = self.vertices[start]
        source.distance = 0
        Q = list(self.vertices.values())

        while Q:
            Q.sort(key=lambda x: x.distance)
            u = Q.pop(0)
            for edge in u.edges:
                v = edge.connection
                if u.distance + edge.weight < v.distance:
                    v.distance = u.distance + edge.weight
                    v.parent = u

    def dijkstra_path(self, dest):
        if dest not in self.vertices:
            print(f"Destination '{dest}' not found.")
            return

        v = self.vertices[dest]
        if v.parent is None and dest != self.start:
            print("No path found.")
            return

        path = []
        while v is not None:
            path.append(v)
            v = v.parent

        path.reverse()
        print("Fastest path (based on time):")
        print(" -> ".join([node.data for node in path]))
        print(f"Total Time: {path[-1].distance} minutes")
