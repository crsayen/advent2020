passwords = []
with open("input2") as f:
    for line in f:
        chunks = line.split(" ")
        minmax = chunks[0].split("-")
        passwords.append(
            {
                "min": int(minmax[0]),
                "max": int(minmax[1]),
                "character": chunks[1][0:-1],
                "password": chunks[2],
            }
        )

ncorrect = 0

for password in passwords:
    n = password["password"].count(password["character"])
    print(password, n)
    if n >= password["min"] and n <= password["max"]:
        ncorrect += 1

print(ncorrect)