use std::collections::HashSet;
use std::str::Lines;

enum Op {
    Nop,
    Acc(i32),
    Jmp(i32),
}

fn parse_program(lines: Lines) -> Vec<Op> {
    let mut program: Vec<Op> = Vec::new();
    for line in lines {
        let parts: Vec<&str> = line.split(' ').collect();
        if parts.len() != 2 {
            continue;
        }
        let n = parts[1].parse::<i32>().unwrap();
        let op = match parts[0] {
            "nop" => Some(Op::Nop),
            "acc" => Some(Op::Acc(n)),
            "jmp" => Some(Op::Jmp(n)),
            _ => None,
        };
        if let Some(op) = op {
            program.push(op);
        }
    }
    program
}

pub fn solve_a(lines: Lines) -> i32 {
    let program = parse_program(lines);
    let mut visited: HashSet<usize> = HashSet::new();
    let mut i = 0;
    let mut acc = 0;
    while !visited.contains(&i) {
        let op = &program[i];
        let (jmp, n) = match op {
            Op::Nop => (1, 0),
            Op::Acc(n) => (1, *n),
            Op::Jmp(n) => (*n, 0),
        };
        visited.insert(i);
        i = (i as i32 + jmp) as usize;
        acc += n;
    }
    acc
}

#[cfg(test)]
mod tests {
    #[test]
    fn example_a() {
        let input = "nop +0\n\
                     acc +1\n\
                     jmp +4\n\
                     acc +3\n\
                     jmp -3\n\
                     acc -99\n\
                     acc +1\n\
                     jmp -4\n\
                     acc +6\n\
                     ";
        assert_eq!(5, super::solve_a(input.lines()));
    }
}
