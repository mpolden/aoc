use std::str::Lines;

fn parse_policy(s: &str) -> Option<(i32, i32, char)> {
    let parts: Vec<&str> = s.split(" ").collect();
    if parts.len() < 2 {
        return None;
    }
    let chr = parts[1].chars().next().unwrap();
    let range_parts: Vec<&str> = parts[0].split("-").collect();
    if range_parts.len() < 2 {
        return None;
    }
    let min = range_parts[0]
        .parse::<i32>()
        .expect("failed to parse number");
    let max = range_parts[1]
        .parse::<i32>()
        .expect("failed to parse number");
    return Some((min, max, chr));
}

pub fn solve(lines: Lines) -> i32 {
    let mut matching_passwords = 0;
    for line in lines {
        let parts: Vec<&str> = line.split(": ").collect();
        if parts.len() != 2 {
            panic!("invalid line {}", line);
        }
        let (min, max, chr) = parse_policy(parts[0]).unwrap();
        let password = parts[1];
        let matches = password.matches(chr).count();
        if matches >= min as usize && matches <= max as usize {
            matching_passwords += 1;
        }
    }
    return matching_passwords;
}

#[cfg(test)]
mod tests {
    #[test]
    fn parse_policy() {
        assert_eq!((1, 3, 'a'), super::parse_policy("1-3 a").unwrap());
    }

    #[test]
    fn solve() {
        let passwords = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc";
        assert_eq!(2, super::solve(passwords.lines()));
    }
}
