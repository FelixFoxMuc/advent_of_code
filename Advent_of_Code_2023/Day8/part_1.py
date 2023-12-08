start_position = "AAA"
final_position = "ZZZ"

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


current_position = start_position
steps = 0

while current_position != final_position:
    for char in instructions:
        if steps % 10000 == 0:
            print(steps)

        if char == "R":
            current_position = mapping_dict[current_position][1]

        elif char == "L":
            current_position = mapping_dict[current_position][0]

        steps += 1
        if current_position == final_position:
            break

print(current_position)
print(steps)
