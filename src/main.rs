use aoc::{day01, day02, day03, day04, day05};
use std::env;
use std::fs::read_to_string;

fn main() -> Result<(), std::io::Error> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("usage: {} <input-file>", &args[0]);
        std::process::exit(1);
    }
    let file = &args[1];
    match file.as_str() {
        // Day 1: Report Repair
        "input/day01.txt" => {
            let input = read_to_string(file)?;
            let numbers = day01::parse_numbers(input.lines());
            let a = day01::solve_a(&numbers);
            let b = day01::solve_b(&numbers);
            println!("day 1 answer a: {}", a);
            println!("      answer b: {}", b);
        }
        // Day 2: Password Philosophy
        "input/day02.txt" => {
            let input = read_to_string(file)?;
            let a = day02::solve_a(input.lines());
            let b = day02::solve_b(input.lines());
            println!("day 2 answer a: {}", a);
            println!("      answer b: {}", b);
        }
        // Day 3: Toboggan Trajectory
        "input/day03.txt" => {
            let input = read_to_string(file)?;
            let a = day03::solve_a(input.lines());
            let b = day03::solve_b(input.lines());
            println!("day 3 answer a: {}", a);
            println!("      answer b: {}", b);
        }
        // Day 4: Passport Processing
        "input/day04.txt" => {
            let input = read_to_string(file)?;
            let a = day04::solve_a(&input);
            let b = day04::solve_b(&input);
            println!("day 4 answer a: {}", a);
            println!("      answer b: {}", b);
        }
        // Day 5: Binary Boarding
        "input/day05.txt" => {
            let input = read_to_string(file)?;
            let a = day05::solve_a(input.lines());
            let b = day05::solve_b(input.lines()).unwrap();
            println!("day 5 answer a: {}", a);
            println!("      answer b: {}", b);
        }
        _ => {
            eprintln!("no solution implemented for file {}", file);
        }
    }
    Ok(())
}
