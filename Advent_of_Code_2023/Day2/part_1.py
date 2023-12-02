max_red = 12
max_green = 13
max_blue = 14

possible_ids = []

with open("input.txt", "r") as file:
    for line in file:

        # Assume the draw is possible
        possible = True
        line = line.strip()

        # Get game ID
        game_id = line.split(": ")[0].replace("Game ", "")

        drawings = line.split(": ")[1].split("; ")

        for draw in drawings:
            cubes = draw.split(", ")

            for cube in cubes:
                if "red" in cube:
                    amount_red = cube.split(" ")[0]
                    if int(amount_red) > max_red:
                        possible = False

                if "green" in cube:
                    amount_green = cube.split(" ")[0]
                    if int(amount_green) > max_green:
                        possible = False

                if "blue" in cube:
                    amount_blue = cube.split(" ")[0]
                    if int(amount_blue) > max_blue:
                        possible = False

        if possible:
            possible_ids.append(int(game_id))


print(possible_ids)
print(sum(possible_ids))
