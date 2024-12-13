from hashlib import md5

input = ["abcdef", "pqrstuv"]

for item in input:
    i = 0

    while True:
        string = item + str(i)
        output = md5(string.encode()).hexdigest()

        if output[:6] == "000000":
            print(i)
            break

        i += 1
