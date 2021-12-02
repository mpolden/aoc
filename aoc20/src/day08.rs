use std::collections::HashSet;
use std::str::Lines;

enum Op {
    Acc(i32),
    Jmp(i32),
    Nop,
}

fn parse_program(lines: &[&str], patch_line: Option<usize>) -> Vec<Op> {
    let mut program: Vec<Op> = Vec::new();
    for (i, line) in lines.iter().enumerate() {
        let parts: Vec<&str> = line.split(' ').collect();
        if parts.len() != 2 {
            continue;
        }
        let patch = patch_line.filter(|line| *line == i).is_some();
        let n = parts[1].parse::<i32>().unwrap();
        let op = match parts[0] {
            "nop" => Some(if patch { Op::Jmp(n) } else { Op::Nop }),
            "acc" => Some(Op::Acc(n)),
            "jmp" => Some(if patch { Op::Nop } else { Op::Jmp(n) }),
            _ => None,
        };
        if let Some(op) = op {
            program.push(op);
        }
    }
    program
}

fn run(program: Vec<Op>) -> (i32, bool) {
    let mut visited: HashSet<usize> = HashSet::new();
    let mut pc = 0;
    let mut acc = 0;
    let mut infinite_loop = false;
    while pc < program.len() {
        infinite_loop = visited.contains(&pc);
        if infinite_loop {
            break;
        }
        let op = &program[pc];
        let (jmp, n) = match op {
            Op::Nop => (1, 0),
            Op::Acc(n) => (1, *n),
            Op::Jmp(n) => (*n, 0),
        };
        visited.insert(pc);
        pc = (pc as i32 + jmp) as usize;
        acc += n;
    }
    (acc, infinite_loop)
}

pub fn solve_a(lines: Lines) -> i32 {
    let lines: Vec<&str> = lines.collect();
    let program = parse_program(&lines, None);
    let (acc, _) = run(program);
    acc
}

pub fn solve_b(lines: Lines) -> Option<i32> {
    let lines: Vec<&str> = lines.collect();
    for i in 0..lines.len() {
        let program = parse_program(&lines, Some(i));
        let (acc, infinite_loop) = run(program);
        if !infinite_loop {
            return Some(acc);
        }
    }
    None
}

#[cfg(test)]
mod tests {
    const INPUT: &str = "nop +0\n\
                     acc +1\n\
                     jmp +4\n\
                     acc +3\n\
                     jmp -3\n\
                     acc -99\n\
                     acc +1\n\
                     jmp -4\n\
                     acc +6\n\
                     ";
    #[test]
    fn example_a() {
        assert_eq!(5, super::solve_a(INPUT.lines()));
    }

    #[test]
    fn example_b() {
        assert_eq!(8, super::solve_b(INPUT.lines()).unwrap());
    }
}
