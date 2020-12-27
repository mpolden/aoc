use std::str::Lines;

pub fn solve_a(lines: Lines) -> usize {
    let lines: Vec<&str> = lines.collect();
    return solve(&lines, 3, 1);
}

pub fn solve_b(lines: Lines) -> usize {
    let lines: Vec<&str> = lines.collect();
    let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let mut answer = 1;
    for (right, down) in &slopes {
        answer *= solve(&lines, *right, *down);
    }
    answer
}

fn solve(lines: &Vec<&str>, right: usize, down: usize) -> usize {
    let mut trees = 0;
    let mut x = right;
    let lines = lines
        .iter()
        .skip(down)
        .enumerate()
        .filter(|t| t.0 % down == 0)
        .map(|t| t.1);
    for line in lines {
        let is_tree = line.chars().nth(x).map_or(false, |c| c == '#');
        if is_tree {
            trees += 1;
        }
        x += right;
        if x >= line.len() {
            // Outside the map, reset the x coordinate
            x -= line.len();
        }
    }
    return trees;
}

#[cfg(test)]
mod tests {
    const MAP: &str = "..##.........##.........##.........##.........##.........##.......  --->\n\
                       #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..\n\
                       .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.\n\
                       ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#\n\
                       .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.\n\
                       ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->\n\
                       .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#\n\
                       .#........#.#........#.#........#.#........#.#........#.#........#\n\
                       #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...\n\
                       #...##....##...##....##...##....##...##....##...##....##...##....#\n\
                       .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->";

    #[test]
    fn example_a() {
        assert_eq!(7, super::solve_a(MAP.lines()));
    }

    #[test]
    fn example_b() {
        assert_eq!(336, super::solve_b(MAP.lines()));
    }
}
