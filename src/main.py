import os
from metro_builder import build_graph_from_csv
from station_input import get_station_code
from metro_graph import Graph

def main():
    print("=" * 60)
    print("WELCOME TO THE SINGAPORE MRT PLANNER")
    print("=" * 60)

    print("\nBuilding the metro graph...")

     #Get the correct path to the CSV
    base = os.path.dirname(__file__)
    csv_path = os.path.abspath(os.path.join(base, '..', 'data', 'processed_stations.csv'))

    graph = build_graph_from_csv(csv_path)
    print("Metro graph loaded successfully.")

    print("\n" + "-" * 60)
    print("Please enter your journey details")
    print("-" * 60)

    start_code = get_station_code(graph, "\nStart station: ")
    dest_code = get_station_code(graph, "End station: ")

    print("\n" + "=" * 60)
    print("SHORTEST ROUTE (BY NUMBER OF STOPS)")
    print("=" * 60)

    graph.bfs(start_code)
    graph.bfs_path(dest_code)

    print("\n" + "=" * 60)
    print("FASTEST ROUTE (BY TRAVEL TIME)")
    print("=" * 60)

    graph.dijkstra(start_code)
    graph.dijkstra_path(dest_code)

    print("\n" + "=" * 60)
    print("Thank you for using the MRT Planner.")
    print("=" * 60)

if __name__ == '__main__':
    main()
