use std::collections::VecDeque;
use std::str::Lines;

fn is_valid(preamble: &VecDeque<i64>, n: i64) -> bool {
    for i in preamble {
        for j in preamble {
            if i + j == n {
                return true;
            }
        }
    }
    false
}

pub fn solve_a(lines: Lines, preamble_size: usize) -> Option<i64> {
    let mut preamble: VecDeque<i64> = VecDeque::with_capacity(preamble_size);
    for line in lines {
        let n = line.parse::<i64>().unwrap();
        if preamble.len() < preamble_size {
            preamble.push_back(n);
            continue;
        }
        if !is_valid(&preamble, n) {
            return Some(n);
        }
        if preamble.len() == preamble_size {
            preamble.pop_front();
            preamble.push_back(n);
        }
    }
    None
}

pub fn solve_b(lines: Lines, invalid_number: i64) -> Option<i64> {
    let mut sequence: VecDeque<i64> = VecDeque::new();
    for line in lines {
        let n = line.parse::<i64>().unwrap();
        let mut sum = sequence.iter().sum::<i64>();
        while sum > invalid_number {
            sequence.pop_front();
            sum = sequence.iter().sum::<i64>();
        }
        if sum == invalid_number {
            let min = sequence.iter().min().unwrap();
            let max = sequence.iter().max().unwrap();
            return Some(min + max);
        }
        sequence.push_back(n);
    }
    None
}

#[cfg(test)]
mod tests {

    const INPUT: &str = r"35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576";

    #[test]
    fn example_a() {
        assert_eq!(127, super::solve_a(INPUT.lines(), 5).unwrap());
    }

    #[test]
    fn example_b() {
        assert_eq!(62, super::solve_b(INPUT.lines(), 127).unwrap())
    }
}
