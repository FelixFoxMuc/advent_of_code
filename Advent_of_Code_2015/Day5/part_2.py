nice_string_count = 0

nice_count = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        nice = False

    # It contains a pair of any two letters that appears at least twice in the string without overlapping,
    # like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
        pairs = []
        i = 0
        for i in range(len(line)-1):
            pair = line[i] + line[i+1]
            pairs.append(pair)

        i = 0
        for i in range(len(pairs)):
            z = i + 2
            if pairs[i] in pairs[z:]:
                nice = True

        # It contains at least one letter
        # which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
        if nice:
            nice = False
            i = 0
            for i in range(len(line) - 2):
                if line[i] == line[i+2]:
                    nice = True

        if nice:
            nice_count += 1

print(nice_count)
