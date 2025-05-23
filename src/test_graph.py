from metro_graph import Graph

def test_graph():
    g = Graph()

    # Add simple graph manually
    g.connect("A", "B", weight=4)
    g.connect("A", "C", weight=2)
    g.connect("B", "D", weight=5)
    g.connect("C", "D", weight=1)
    g.connect("D", "E", weight=3)

    g.vertices["A"].data = "Alpha"
    g.vertices["B"].data = "Bravo"
    g.vertices["C"].data = "Charlie"
    g.vertices["D"].data = "Delta"
    g.vertices["E"].data = "Echo"

    # Test BFS
    g.bfs("A")
    g.bfs_path("E")

    print("\n---")

    # Test Dijkstra
    g.dijkstra("A")
    g.dijkstra_path("E")

if __name__ == "__main__":
    test_graph()
