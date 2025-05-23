def get_station_code(graph, prompt):
    name = input(prompt).strip().lower()

    matches = [v for v in graph.vertices.values() if v.data.lower() == name]

    if not matches:
        print(f"No station named '{name.title()}'. Please try again.")
        return get_station_code(graph, prompt)

    if len(matches) == 1:
        print(f"Found: {matches[0].data} ({matches[0].key})")
        return matches[0].key

    print(f"Multiple stations found named '{name.title()}':")
    for v in matches:
        print(f"  {v.data} → Code: {v.key}")
    code = input("Enter the exact station code: ").strip().upper()

    if code in graph.vertices:
        return code
    else:
        print("Invalid code. Please try again.")
        return get_station_code(graph, prompt)
