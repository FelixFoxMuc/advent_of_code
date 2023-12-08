# Tried to route until all of them got to the same spot. Runs forever :)

instructions = ""

mapping_dict = {}

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.count("R") > 10:
            instructions += line
        elif line == "":
            continue
        else:
            key = line.split(" = ")[0]
            values = line.split(" = ")[1]

            value_1 = values.split(", ")[0].removeprefix("(")
            value_2 = values.split(", ")[1].removesuffix(")")

            mapping_dict[key] = (value_1, value_2)

# Needs to be every position that end with A
start_position = "XXA"

# Needs to be every position that ends with Z
final_position = "XXZ"

current_position = [position for position in mapping_dict if position[2] == start_position[2]]
steps = 0
new_current_position = []

print(current_position)

not_found = True

while not_found:
    for char in instructions:
        if steps % 1000000 == 0:
            print(steps)
        finals = []

        if char == "R":
            for position in current_position:
                new_current_position.append(mapping_dict[position][1])
                steps += 1

        elif char == "L":
            for position in current_position:
                new_current_position.append(mapping_dict[position][0])
                steps += 1

        current_position = new_current_position
        new_current_position = []

        for position in current_position:
            if position[2] != final_position[2]:
                finals.append(False)
            else:
                finals.append(True)

        if all(finals):
            exit((steps, current_position))



