destinations = [(0,0), (1,2), (3,1), (4,4)]
start = destinations[0]
destinations = destinations[1:]
min_sorted_destinations = []
starting_point = start

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

while destinations:
    closest_destination = None
    closest_distance = float('inf')
    for each_point in destinations:
        d = distance(starting_point, each_point)
        if d < closest_distance:
            closest_distance = d
            closest_destination = each_point

    if closest_destination is None:
        break

    min_sorted_destinations.append(closest_destination)
    destinations.remove(closest_destination)
    starting_point = closest_destination


min_sorted_destinations = min_sorted_destinations[::-1] + [start]
print(min_sorted_destinations)