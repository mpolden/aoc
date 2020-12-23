use std::str::Lines;
use std::vec::Vec;

pub fn solve_a(numbers: &Vec<i32>) -> i32 {
    return solve(numbers, false);
}

pub fn solve_b(numbers: &Vec<i32>) -> i32 {
    return solve(numbers, true);
}

pub fn parse_numbers(lines: Lines) -> Vec<i32> {
    let mut numbers = Vec::new();
    for line in lines {
        let n = line.parse::<i32>().expect("failed to parse number");
        numbers.push(n);
    }
    return numbers;
}

fn solve(numbers: &Vec<i32>, b: bool) -> i32 {
    for i in numbers {
        for j in numbers {
            if b {
                for k in numbers {
                    if i + j + k == 2020 {
                        return i * j * k;
                    }
                }
            } else {
                if i + j == 2020 {
                    return i * j;
                }
            }
        }
    }
    return 0;
}
