floor = 0
i = 0

with open("parenthesis_input", "r") as file:
    content = file.read().strip()
    for parenthesis in content:
        if parenthesis == "(":
            floor += 1
        elif parenthesis == ")":
            floor -= 1
        i += 1
        if floor == -1:
            print(i)
            break
