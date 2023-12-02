import hashlib

given = "yzbqklnj"

i = 0

run = True

while run:

    str2hash = given + str(i)

    result = hashlib.md5(str2hash.encode())

    result = result.hexdigest()

    if result[:6] == "000000":
        print(i)
        exit("nice")
    else:
        i += 1
