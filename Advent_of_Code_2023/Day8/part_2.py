from math import lcm
from datetime import datetime, timedelta

start_time = datetime.now()

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

start_position = "XXA"
final_position = "XXZ"


current_positions = [position for position in mapping_dict if position[2] == start_position[2]]
finals = []

print(current_positions)

for current_position in current_positions:
    steps = 0
    while current_position[2] != final_position[2]:
        for char in instructions:
            if steps % 10000 == 0:
                print(steps)

            if char == "R":
                current_position = mapping_dict[current_position][1]

            elif char == "L":
                current_position = mapping_dict[current_position][0]

            steps += 1
            if current_position[2] == final_position[2]:
                break

    finals.append(steps)

print(finals)

finals = [int(x) for x in finals]

steps = lcm(*finals)

print(steps)

end_time = start_time.now()

print(start_time)
print(end_time)
