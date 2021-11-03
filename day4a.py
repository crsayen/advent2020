data = None

fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
]

def checkValid(passport):
    for field in fields:
        if field == 'cid': continue
        value = passport.get(field)
        if value in ['', None]:
            return False
    return True

with open('input4') as f:
    nvalid = 0
    passport = {field: None for field in fields}
    for line in f:
        line = line.replace('\n', '')
        if line == '':
            if checkValid(passport): nvalid += 1
            passport = {field: None for field in fields}
        chunks = line.split(' ')
        for chunk in chunks:
            keyVal = chunk.split(':')
            if not len(keyVal) == 2: continue
            key, value = keyVal
            passport[key] = value
    if checkValid(passport): nvalid += 1

print(nvalid)


