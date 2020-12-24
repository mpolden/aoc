use std::collections::HashSet;

pub fn solve_a(passports: &str) -> i32 {
    let required_fields: HashSet<&'static str> = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
        .iter()
        .cloned()
        .collect();
    let mut valid = 0;
    for line in passports.split("\n\n") {
        let joined_line = line.replace("\n", " ");
        let fields: HashSet<&str> = joined_line
            .split(" ")
            .map(|s| s.split(":").nth(0))
            .flatten()
            .collect();
        if fields.is_superset(&required_fields) {
            valid += 1;
        }
    }
    valid
}

#[cfg(test)]
mod tests {
    const PASSPORTS: &str = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n\
                             byr:1937 iyr:2017 cid:147 hgt:183cm\n\
                             \n\
                             iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n\
                             hcl:#cfa07d byr:1929\n\
                             \n\
                             hcl:#ae17e1 iyr:2013\n\
                             eyr:2024\n\
                             ecl:brn pid:760753108 byr:1931\n\
                             hgt:179cm\n\
                             \n\
                             hcl:#cfa07d eyr:2025 pid:166559648\n\
                             iyr:2011 ecl:brn hgt:59in";

    #[test]
    fn solve_a() {
        assert_eq!(2, super::solve_a(PASSPORTS));
    }
}
