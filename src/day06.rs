use std::collections::HashSet;

pub fn solve_a(input: &str) -> usize {
    let mut sum = 0;
    for group in input.split("\n\n") {
        let answers: HashSet<char> = group.chars().filter(|c| *c != '\n').collect();
        sum += answers.len()
    }
    sum
}

#[cfg(test)]
mod tests {

    #[test]
    fn example_a() {
        let input = "abc\n\
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
        assert_eq!(11, super::solve_a(&input));
    }
}
