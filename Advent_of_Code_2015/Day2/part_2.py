needed_ribbon = 0

with open("input.txt", "r") as file:
    for line in file:
        dimensions_string = line.strip().split("x")
        dimensions_int = []
        for string in dimensions_string:
            dimensions_int.append(int(string))
        dimensions_int = sorted(dimensions_int)

        gift_ribbon = 2 * dimensions_int[0] + 2 * dimensions_int[1]
        gift_bow = dimensions_int[0] * dimensions_int[1] * dimensions_int[2]
        gift_total = gift_bow + gift_ribbon

        needed_ribbon += gift_total

    print(needed_ribbon)
