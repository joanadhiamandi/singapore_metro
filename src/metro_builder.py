import csv
import random
from metro_graph import Graph


def build_graph_from_csv(csv_path):
    graph = Graph()
    stations = []

    #Read the CSV and collect station info
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row['code']
            name = row['name'].title()
            line = row['line']
            num = int(row['num'])
            vertex = graph.add_vertex(code)
            vertex.data = name
            stations.append({'code': code, 'name': name, 'line': line, 'num': num})

    # Connect stations on the same line
    stations.sort(key=lambda s: (s['line'], s['num']))
    for i in range(len(stations) - 1):
        curr = stations[i]
        next = stations[i + 1]
        if curr['line'] == next['line'] and next['num'] - curr['num'] == 1:
            travel_time = random.randint(2, 8)
            graph.connect(curr['code'], next['code'], travel_time)

    # Connect interchange stations (same name, different lines)
    name_to_codes = {}
    for s in stations:
        name = s['name']
        if name not in name_to_codes:
            name_to_codes[name] = []
        name_to_codes[name].append(s['code'])

    for codes in name_to_codes.values():
        if len(codes) > 1:
            for i in range(len(codes)):
                for j in range(i + 1, len(codes)):
                    graph.connect(codes[i], codes[j], 5)  # fixed 5 min transition

    return graph

# Make sure this function is accessible
__all__ = ["build_graph_from_csv"]
