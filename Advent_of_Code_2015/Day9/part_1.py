from random import choice

lines = []
distances = {}
destination_list = []
min_distance = 99999999999
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

for line in lines:
    destination_1 = line.split(" to ")[0]
    destination_2 = line.split(" to ")[1].split(" = ")[0]
    distance = int(line.split(" to ")[1].split(" = ")[1])
    if destination_1 not in destination_list:
        destination_list.append(destination_1)
    if destination_2 not in destination_list:
        destination_list.append(destination_2)

    destinations = [destination_1, destination_2]
    sorted_destinations = sorted(destinations)

    distances[(sorted_destinations[0], sorted_destinations[1])] = distance

for i in range(1000000):
    route_distance = 0
    route_destinations = [d for d in destination_list]
    start_destination = choice(route_destinations)
    route_destinations.remove(start_destination)
    while len(route_destinations) > 0:
        end_destination = choice(route_destinations)
        route_destinations.remove(end_destination)
        sorted_route = sorted([start_destination, end_destination])
        start_destination = end_destination

        dest_distance = distances[(sorted_route[0], sorted_route[1])]
        route_distance += dest_distance

    if route_distance < min_distance:
        min_distance = route_distance

print(min_distance)
