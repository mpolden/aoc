use std::cmp;
use std::collections::HashSet;
use std::str::Lines;

pub fn solve_a(lines: Lines) -> i32 {
    let mut ratings: Vec<i32> = vec![0];
    lines
        .map(|s| s.parse::<i32>().unwrap())
        .for_each(|r| ratings.push(r));
    ratings.sort_unstable();
    let mut one_jolt_diff = 0;
    let mut three_jolt_diff = 0;
    for (i, rating) in ratings.iter().enumerate() {
        let diff = ratings.get(i + 1).map(|next_rating| next_rating - rating);
        match diff {
            Some(1) => one_jolt_diff += 1,
            Some(3) | None => three_jolt_diff += 1,
            Some(_) => panic!("illegal adapter found after {}", rating),
        }
    }
    one_jolt_diff * three_jolt_diff
}

fn is_valid(diff: i32) -> bool {
    diff >= 1 && diff <= 3
}

pub fn solve_b(lines: Lines) -> i32 {
    let mut ratings: Vec<i32> = vec![0];
    lines
        .map(|s| s.parse::<i32>().unwrap())
        .for_each(|r| ratings.push(r));
    ratings.sort_unstable();
    println!("input {:?}", ratings);
    // [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
    let mut candidates = 1;

    let mut used_adapters: HashSet<i32> = HashSet::new();
    for valid_diff in 1..4 {
        for (i, rating1) in ratings.iter().enumerate() {
            let mut candidates_for_this = 0;
            let next = i + 1;
            print!("{}, ", rating1);
            for (j, rating2) in ratings.iter().skip(next).enumerate() {
                // if used_adapters.contains(rating2) {
                //     continue;
                // }
                let diff = rating2 - rating1;
                if diff == valid_diff || is_valid(diff) {
                    print!("{}, ", rating2);
                }
            }
            if i + 1 == ratings.len() {
                println!();
            }
            // if i + 1 == ratings.len() {
            //     candidates_for_this += 1;
            // }
            // println!("candidates for {:?} = {:?}", rating1, candidates_for_this);
            // candidates *= candidates_for_this;
        }
    }
    candidates
}

#[cfg(test)]
mod tests {

    const INPUT1: &str = r"16
10
15
5
1
11
7
19
6
12
4";

    const INPUT2: &str = r"28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3";

    #[test]
    fn example_a() {
        assert_eq!(35, super::solve_a(INPUT1.lines()));
        assert_eq!(220, super::solve_a(INPUT2.lines()));
    }

    #[test]
    fn example_b() {
        assert_eq!(8, super::solve_b(INPUT1.lines()));
        assert_eq!(19_208, super::solve_b(INPUT2.lines()));
    }
}
