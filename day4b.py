import string
data = None

validators = {
    'byr': lambda byr: byr.isnumeric() and len(byr) == 4 and 1919 < int(byr) < 2003,
    'iyr': lambda iyr: iyr.isnumeric() and len(iyr) == 4 and 2009 < int(iyr) < 2021,
    'eyr': lambda eyr: eyr.isnumeric() and len(eyr) == 4 and 2019 < int(eyr) < 2031,
    'hgt': lambda hgt: hgt[-2:] in ['cm', 'in'] and hgt[:-2].isnumeric() and 149 < int(hgt[:-2]) < 194 if hgt[-2:] == 'cm' else 58 < int(hgt[:-2]) < 77,
    'hcl': lambda hcl: hcl[0] == '#' and len(hcl) == 7 and all(c in string.hexdigits for c in hcl[1:]),
    'ecl': lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda pid: len(pid) == 9 and pid.isnumeric(),
}

def checkValid(passport):
    for field, validator in validators.items():
        if field == 'cid': continue
        value = passport.get(field)
        if value in ['', None]:
            return False
        if not validator(value):
            return False
    return True

with open('input4') as f:
    nvalid = 0
    passport = {field: None for field in validators.keys()}
    for line in f:
        line = unicode(line.replace('\n', ''), 'utf-8')
        if line == '':
            if checkValid(passport): nvalid += 1
            passport = {field: None for field in validators.keys()}
        chunks = line.split(' ')
        for chunk in chunks:
            keyVal = chunk.split(':')
            if not len(keyVal) == 2: continue
            key, value = keyVal
            passport[key] = value
    if checkValid(passport): nvalid += 1

print(nvalid)
        
