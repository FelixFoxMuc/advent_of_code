from random import choice, randint

ingredients = {}
total_spoons = 100
max_score = 1

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        ingredient = line[0].removesuffix(":").lower()
        characteristics = {}
        for i in range(1, len(line)):
            if i % 2 == 1:
                char_name = line[i]
            else:
                char_value = int(line[i].removesuffix(","))
                characteristics[char_name] = char_value

        ingredients[ingredient] = characteristics


print(ingredients)
for ingredient in ingredients:
    ingredients[ingredient].pop("calories")
print(ingredients)

for k in range(100000000):
    random_amounts = [0 for i in range(len(ingredients))]
    current_spoons = total_spoons

    for i in range(total_spoons):
        j = randint(0, len(ingredients)-1)
        extra = randint(0, current_spoons)
        random_amounts[j] += extra
        current_spoons -= extra

    if sum(random_amounts) < total_spoons:
        j = randint(0, len(ingredients)-1)
        dif = total_spoons - sum(random_amounts)
        random_amounts[j] += dif

    all_scores = {char: [] for char in ingredients[ingredient]}
    # print(random_amounts)

    p = 0
    # print(all_scores)
    for ingredient in ingredients:

        power = 1
        # print(ingredient)
        for char in ingredients[ingredient]:
            power = ingredients[ingredient][char]
            power *= random_amounts[p]
            all_scores[char].append(power)
        p += 1

    # print(all_scores)

    total_score = 1
    for score in all_scores:
        total = 0
        for num in all_scores[score]:
            total += num

        if total >= 0:
            total_score *= total
        else:
            total_score *= 0

    if total_score > max_score:
        max_score = total_score
        print(max_score)
        print(random_amounts)






