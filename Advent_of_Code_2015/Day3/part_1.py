locations = [(0, 0)]

current_location = (0, 0)

with open("input.txt", "r") as file:
    directions = file.read()
    for direction in directions:
        if direction == "^":
            current_location = (current_location[0] + 1, current_location[1])
            if current_location not in locations:
                locations.append(current_location)
        elif direction == "v":
            current_location = (current_location[0] - 1, current_location[1])
            if current_location not in locations:
                locations.append(current_location)
        elif direction == ">":
            current_location = (current_location[0], current_location[1] + 1)
            if current_location not in locations:
                locations.append(current_location)
        elif direction == "<":
            current_location = (current_location[0], current_location[1] - 1)
            if current_location not in locations:
                locations.append(current_location)

print(len(locations))
