use std::str::Lines;

pub fn solve_a(lines: Lines) -> usize {
    let mut trees_total = 0;
    let mut x = 3; // Starting in 0,0 and moving 3 right, 1 down
    for line in lines.skip(1) {
        let trees = line
            .chars()
            .nth(x)
            .map_or(0, |c| if c == '#' { 1 } else { 0 });
        trees_total += trees;
        x += 3;
        if x >= line.len() {
            // Outside the map, reset the x coordinate
            x -= line.len();
        }
    }
    return trees_total;
}

#[cfg(test)]
mod tests {
    #[test]
    fn solve_a() {
        let map = "..##.........##.........##.........##.........##.........##.......  --->\n\
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
        assert_eq!(7, super::solve_a(map.lines()));
    }
}
