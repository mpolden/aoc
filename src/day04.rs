use std::collections::{HashMap, HashSet};

pub fn solve_a(passports: &str) -> i32 {
    solve(passports, false)
}

pub fn solve_b(passports: &str) -> i32 {
    solve(passports, true)
}

fn solve(passports: &str, validate_value: bool) -> i32 {
    let required_fields: HashSet<&'static str> = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
        .iter()
        .cloned()
        .collect();
    let mut valid = 0;
    for line in passports.split("\n\n") {
        let joined_line = line.replace("\n", " ");
        let field_values: HashMap<&str, &str> = joined_line
            .split(" ")
            .map(|s| {
                let parts: Vec<&str> = s.split(":").collect();
                if parts.len() < 2 {
                    return None;
                }
                Some((parts[0], parts[1]))
            })
            .flatten()
            .collect();
        let fields_present = required_fields
            .iter()
            .all(|field| field_values.contains_key(field));
        if !fields_present {
            continue;
        }
        let mut is_valid = true;
        if validate_value {
            is_valid = field_values.iter().all(|kv| {
                let (field, value) = kv;
                validate(field, value)
            });
        }
        if is_valid {
            valid += 1;
        }
    }
    valid
}

fn validate(field: &str, value: &str) -> bool {
    match field {
        "byr" => {
            let year = value.parse::<i32>().unwrap();
            year >= 1920 && year <= 2002
        }
        "iyr" => {
            let year = value.parse::<i32>().unwrap();
            year >= 2010 && year <= 2020
        }
        "eyr" => {
            let year = value.parse::<i32>().unwrap();
            year >= 2020 && year <= 2030
        }
        "hgt" => {
            if value.ends_with("cm") {
                let height = value.replace("cm", "").parse::<i32>().unwrap();
                return height >= 150 && height <= 193;
            } else if value.ends_with("in") {
                let height = value.replace("in", "").parse::<i32>().unwrap();
                return height >= 59 && height <= 76;
            }
            false
        }
        "hcl" => {
            if !value.starts_with("#") || value.len() != 7 {
                return false;
            }
            value
                .chars()
                .skip(1)
                .all(|c| (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f'))
        }
        "ecl" => match value {
            "amb" | "blu" | "brn" | "gry" | "grn" | "hzl" | "oth" => true,
            _ => false,
        },
        "pid" => {
            if value.len() != 9 {
                return false;
            }
            value.chars().all(|c| c >= '0' && c <= '9')
        }
        "cid" => true,
        _ => false,
    }
}

#[cfg(test)]
mod tests {

    #[test]
    fn example_a() {
        let passports = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n\
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
        assert_eq!(2, super::solve_a(&passports));
    }

    #[test]
    fn example_b() {
        let passports = "eyr:1972 cid:100\n\
                         hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926\n\
                         \n\
                         iyr:2019\n\
                         hcl:#602927 eyr:1967 hgt:170cm\n\
                         ecl:grn pid:012533040 byr:1946\n\
                         \n\
                         hcl:dab227 iyr:2012\n\
                         ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277\n\
                         \n\
                         hgt:59cm ecl:zzz\n\
                         eyr:2038 hcl:74454a iyr:2023\n\
                         pid:3556412378 byr:2007\n\
                         \n\
                         pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\n\
                         hcl:#623a2f\n\
                         \n\
                         eyr:2029 ecl:blu cid:129 byr:1989\n\
                         iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm\n\
                         \n\
                         hcl:#888785\n\
                         hgt:164cm byr:2001 iyr:2015 cid:88\n\
                         pid:545766238 ecl:hzl\n\
                         eyr:2022\n\
                         \n\
                         iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719";
        assert_eq!(4, super::solve_b(&passports));
    }

    #[test]
    fn validate() {
        assert_eq!(true, super::validate("byr", "2002"));
        assert_eq!(false, super::validate("byr", "2003"));

        assert_eq!(true, super::validate("hgt", "60in"));
        assert_eq!(true, super::validate("hgt", "190cm"));
        assert_eq!(false, super::validate("hgt", "190in"));
        assert_eq!(false, super::validate("hgt", "190"));

        assert_eq!(true, super::validate("hcl", "#123abc"));
        assert_eq!(false, super::validate("hcl", "#123abz"));
        assert_eq!(false, super::validate("hcl", "123abc"));

        assert_eq!(true, super::validate("ecl", "brn"));
        assert_eq!(false, super::validate("ecl", "wat"));

        assert_eq!(true, super::validate("pid", "000000001"));
        assert_eq!(false, super::validate("ecl", "0123456789"));
    }
}
