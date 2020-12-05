def parse_passports(data: str) -> list[dict]:
    data = data.split("\n\n")
    data = [entry.split() for entry in data]
    data = [[pairs.split(":") for pairs in passports] for passports in data]
    data = [dict(passport) for passport in data]
    return data


if __name__ == "__main__":
    required_fields = set("byr iyr eyr hgt hcl ecl pid".split())
    data = open("Day 4 Data.txt").read()
    data = parse_passports(data)
    print(f"Number of passports: {len(data)}")
    valid_passports = [passport for passport in data if not required_fields.difference(passport.keys())]
    print(f"Number of valid passports: {len(valid_passports)}")
    #print(valid_passports)
