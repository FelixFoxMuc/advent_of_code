locations = [(0, 0)]

current_location_santa = (0, 0)
current_location_robo = (0, 0)

directions_santa = []
directions_robo = []


with open("input.txt", "r") as file:
    directions = file.read()

    # split directions for each delivery person
    i = 0
    for char in directions:
        if i % 2 == 0:
            directions_santa.append(char)
        if not i % 2 == 0:
            directions_robo.append(char)
        i += 1


    # Let Santa move
    for direction in directions_santa:
        if direction == "^":
            current_location_santa = (current_location_santa[0] + 1, current_location_santa[1])
            if current_location_santa not in locations:
                locations.append(current_location_santa)
        elif direction == "v":
            current_location_santa = (current_location_santa[0] - 1, current_location_santa[1])
            if current_location_santa not in locations:
                locations.append(current_location_santa)
        elif direction == ">":
            current_location_santa = (current_location_santa[0], current_location_santa[1] + 1)
            if current_location_santa not in locations:
                locations.append(current_location_santa)
        elif direction == "<":
            current_location_santa = (current_location_santa[0], current_location_santa[1] - 1)
            if current_location_santa not in locations:
                locations.append(current_location_santa)

    # Let Robo move
    for direction in directions_robo:
        if direction == "^":
            current_location_robo = (current_location_robo[0] + 1, current_location_robo[1])
            if current_location_robo not in locations:
                locations.append(current_location_robo)
        elif direction == "v":
            current_location_robo = (current_location_robo[0] - 1, current_location_robo[1])
            if current_location_robo not in locations:
                locations.append(current_location_robo)
        elif direction == ">":
            current_location_robo = (current_location_robo[0], current_location_robo[1] + 1)
            if current_location_robo not in locations:
                locations.append(current_location_robo)
        elif direction == "<":
            current_location_robo = (current_location_robo[0], current_location_robo[1] - 1)
            if current_location_robo not in locations:
                locations.append(current_location_robo)

print(len(locations))
