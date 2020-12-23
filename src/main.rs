use aoc::day01;
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
        _ => {
            eprintln!("no solution implemented for file {}", file);
        }
    }
    Ok(())
}
