def getSeatId(code):
    rows = range(128)
    columns = range(8)
    for i, character in enumerate(code):
        upper = character in ['R', 'B']
        if i > 6:
            columns = columns[(len(columns) / 2) * upper: (len(columns) / 2) + ((len(columns) / 2) * upper)]
        else:
            rows = rows[(len(rows) / 2) * upper: (len(rows) / 2) + ((len(rows) / 2) * upper)]
    return rows[0] * 8 + columns[0]

with open('input5') as f:
    highest = 0
    for line in f:
        seatId = getSeatId(line.replace('\n', ''))
        if seatId > highest: highest = seatId
    print(highest)
