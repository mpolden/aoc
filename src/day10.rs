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

#[cfg(test)]
mod tests {

    #[test]
    fn example_a() {
        let input1 = r"16
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
        let input2 = r"28
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
        assert_eq!(35, super::solve_a(input1.lines()));
        assert_eq!(220, super::solve_a(input2.lines()));
    }
}
