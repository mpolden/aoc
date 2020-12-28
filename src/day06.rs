use std::collections::{HashMap, HashSet};

pub fn solve_a(input: &str) -> usize {
    let mut sum = 0;
    for group in input.split("\n\n") {
        let answers: HashSet<char> = group.chars().filter(|c| *c != '\n').collect();
        sum += answers.len()
    }
    sum
}

pub fn solve_b(input: &str) -> usize {
    let mut sum = 0;
    for group in input.split("\n\n") {
        let mut persons = 1;
        let mut answers: HashMap<char, usize> = HashMap::new();
        for c in group.trim().chars() {
            if c == '\n' {
                persons += 1;
                continue;
            }
            let count = answers.entry(c).or_insert(0);
            *count += 1;
        }
        sum += answers.values().filter(|count| *count == &persons).count();
    }
    sum
}

#[cfg(test)]
mod tests {

    const INPUT: &str = "abc\n\
                     \n\
                     a\n\
                     b\n\
                     c\n\
                     \n\
                     ab\n\
                     ac\n\
                     \n\
                     a\n\
                     a\n\
                     a\n\
                     a\n\
                     \n\
                     b\n\
                     ";

    #[test]
    fn example_a() {
        assert_eq!(11, super::solve_a(INPUT));
    }

    #[test]
    fn example_b() {
        assert_eq!(6, super::solve_b(INPUT));
    }
}
