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
    seats = [getSeatId(line.replace('\n', '')) for line in f]
    seats.sort()
    prev = seats[0] - 1
    for seat in seats:
        if seat != prev + 1:
            print(prev + 1)
            break
        prev = seat

