import re

def is_valid1(passport):
    if "cid" in passport:
        return len(passport) == 8
    else:
        return len(passport) == 7


def is_valid2(passport):
    try:
        byr = passport["byr"]
        if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
            return False
        iyr = passport["iyr"]
        if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
            return False
        eyr = passport["eyr"]
        if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
            return False
        hgt = passport["hgt"]
        hgt_num = int(hgt[:-2])
        hgt_units = hgt[-2:]
        if hgt_units == "cm":
            if hgt_num < 150 or hgt_num > 193:
                return False
        elif hgt_units == "in":
            if hgt_num < 59 or hgt_num > 76:
                return False
        else:
            return False
        hcl = passport["hcl"]
        if not re.match("#[a-f,0-9]{6}", hcl):
            return False
        ecl = passport["ecl"]
        if not ecl in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return False
        pid = passport["pid"]
        int(pid)
        if len(pid) != 9:
            return False
        return True
    except:
        return False


def main(lines, is_valid):
    passports = []
    passport = {}
    for line in lines:
        if line == "\n":
            if is_valid(passport):
                passports.append(passport)
            passport = {}
        else:
            tail = line
            while (len(tail) > 0):
                match = re.match("(.{3}):(.+?)([ \n])", tail)
                if match:
                    passport[match.group(1)] = match.group(2)
                    tail = tail[match.end(3):]
                else:
                    break
    if is_valid(passport):
        passports.append(passport)
    return(len(passports))


with open("input4") as f:
    lines = f.readlines()
    print(main(lines, is_valid1))
    print(main(lines, is_valid2))
    

