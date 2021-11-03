passwords = []
with open("input2") as f:
    for line in f:
        chunks = line.split(" ")
        minmax = chunks[0].split("-")
        passwords.append(
            {
                "pos1": int(minmax[0]) - 1,
                "pos2": int(minmax[1]) - 1,
                "character": chunks[1][0:-1],
                "password": chunks[2],
            }
        )

ncorrect = 0

for password in passwords:
    npos = 0
    if len(password["password"]) >= password["pos1"]:
        if password["password"][password["pos1"]] == password["character"]:
            npos += 1
    if len(password["password"]) >= password["pos2"]:
        if password["password"][password["pos2"]] == password["character"]:
            npos += 1
    if npos == 1:
        ncorrect += 1

print(ncorrect)
