game_powers = []

with open("input.txt", "r") as file:
    for line in file:

        # Assume the minimum is 0
        min_red = 0
        min_green = 0
        min_blue = 0

        line = line.strip()

        # Get game ID
        game_id = line.split(": ")[0].replace("Game ", "")

        drawings = line.split(": ")[1].split("; ")

        for draw in drawings:
            cubes = draw.split(", ")

            for cube in cubes:
                if "red" in cube:
                    amount_red = int(cube.split(" ")[0])
                    if amount_red > min_red:
                        min_red = amount_red

                if "green" in cube:
                    amount_green = int(cube.split(" ")[0])
                    if amount_green > min_green:
                        min_green = amount_green

                if "blue" in cube:
                    amount_blue = int(cube.split(" ")[0])
                    if amount_blue > min_blue:
                        min_blue = amount_blue

        power = (min_red * min_green * min_blue)

        game_powers.append(power)

print(game_powers)
print(sum(game_powers))
