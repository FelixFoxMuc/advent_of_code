nice_string_count = 0

rule_one = ["ab", "cd", "pq", "xy"]

vowels = "aeiou"

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        vowel_count = 0

        nice = True
        # rule 1: does not contain "ab, cd, pq, or xy"
        for sub in rule_one:
            if sub in line:
                nice = False

        # continue with rule 2 if still nice: contains at lease one letter double
        if nice:
            nice = False

            letter_1 = 0
            letter_2 = 1
            for _ in range(len(line) - 1):
                if line[letter_1] == line[letter_2]:
                    nice = True

                letter_1 += 1
                letter_2 += 1

        # check rule 3 if still nice: contains at least three vowels "aeiou". Doubles count too
        if nice:
            # for char in vowels:
            #     if char in line:
            #         vowel_count += 1
            for char in line:
                if char in vowels:
                    vowel_count += 1

            if vowel_count < 3:
                nice = False

        if nice:
            nice_string_count += 1

print(nice_string_count)