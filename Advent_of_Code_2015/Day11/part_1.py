old_password_string = "vzbxkghb"
old_passwort = [char for char in old_password_string]

alphabet_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = [char for char in alphabet_string]


def check_rules(password: list):
    # rule 1
    # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on,
    # up to xyz. They cannot skip letters; abd doesn't count.
    rule_1 = False
    alphabet_index = [alphabet.index(item) for item in password]

    for i in range(len(alphabet_index) - 2):
        if alphabet_index[i] == (alphabet_index[(i + 1)] - 1) and (alphabet_index[(i + 1)]) == (
                alphabet_index[(i + 2)] - 1):
            rule_1 = True

    if not rule_1:
        return False

    # rule 2
    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are
    # therefore confusing.
    rule_2 = True
    for letter in password:
        if letter == "i" or letter == "o" or letter == "l":
            return False

    if not rule_2:
        print("Failed rule 2")
        return False

    # rule 3
    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    rule_3 = False
    for i in range(len(password) - 2):
        if password[i] == password[(i + 1)]:
            for j in range(i + 2, len(password) - 1):
                if password[j] == password[j + 1] and password[j] != password[i]:
                    rule_3 = True

    if rule_3:
        correct_password = ""
        for letter in password:
            correct_password += letter
        print(f"All rules correct. password is: {correct_password}")
        return True
    else:
        return False


old_passwort_num = [alphabet.index(letter) for letter in old_passwort]
print(old_passwort_num)
new_password = [alphabet[num] for num in old_passwort_num]
print(new_password)

j = 1

for i in range(10000000000000000):
    if i % 1000000 == 0:
        print(i)
    up = False
    j = 1
    check_rules(new_password)
    while up is False:
        if old_passwort_num[-j] != 25:
            old_passwort_num[-j] += 1
            up = True
            # print(old_passwort_num)
            new_password = [alphabet[num] for num in old_passwort_num]
            # print(new_password)
        else:
            old_passwort_num[-j] = 0
            j += 1
