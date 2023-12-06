solution = {}
with open("input_reader.txt", "r") as reader:
    for line in reader:
        line = line.strip().split(": ")
        solution[line[0]] = line[1]

print(f"Reader: {solution}")

with open("input.txt", "r") as file:
    for line in file:
        sue = {}
        line = line.strip().split(" ")

        num = line[1].removesuffix(":")

        sue["num"] = num

        for i in range(2, len(line)):
            if i % 2 == 0:
                item = line[i].removesuffix(":")
                item_amount = line[i+1].removesuffix(",")
                sue[item] = item_amount

        found_her = []

        for item in sue:
            if item == "num":
                continue
            try:
                if solution[item] != sue[item]:
                    found_her.append(False)
                elif solution[item] == sue[item]:
                    found_her.append(True)
            except KeyError:
                pass

        if False not in found_her:
            print(f"Found the Sue. It is number {sue['num']}\n"
                  f"Sue items: {sue}")
