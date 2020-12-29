use std::collections::HashMap;
use std::fmt;
use std::str::Lines;

#[derive(Debug)]
struct Bag {
    color: String,
    count: usize,
}

impl fmt::Display for Bag {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{} {}", self.color, self.count)
    }
}

fn parse_bags(lines: Lines) -> HashMap<String, Vec<Bag>> {
    let mut bags: HashMap<String, Vec<Bag>> = HashMap::new();
    for line in lines {
        let parts: Vec<&str> = line.split(" bags contain ").collect();
        if parts.len() < 2 {
            continue;
        }
        let color = parts[0];
        let specs = parts[1];
        let mut sub_bags: Vec<Bag> = Vec::new();
        if specs != "no other bags." {
            for spec in specs.split(", ") {
                let parts: Vec<&str> = spec.splitn(2, ' ').collect();
                if parts.len() < 2 {
                    continue;
                }
                let count = parts[0].parse::<usize>().unwrap();
                let color = parts[1]
                    .replace(" bags", "")
                    .replace(" bag", "")
                    .replace(".", "");
                let bag = Bag {
                    color: color.to_string(),
                    count,
                };
                sub_bags.push(bag);
            }
        }
        bags.insert(color.to_string(), sub_bags);
    }
    bags
}

fn bag_count(bags: &HashMap<String, Vec<Bag>>, color: &str, wanted_color: &str) -> usize {
    let mut count = 0;
    let sub_bags = bags.get(color);
    if sub_bags.is_none() {
        return count;
    } else {
        for bag in sub_bags.unwrap() {
            if bag.color == wanted_color {
                count += 1;
            }
            count += bag_count(bags, &bag.color, wanted_color);
        }
    }
    count
}

pub fn solve_a(lines: Lines) -> usize {
    let bags = parse_bags(lines);
    bags.keys()
        .map(|color| bag_count(&bags, color, "shiny gold"))
        .filter(|count| *count > 0)
        .count()
}

#[cfg(test)]
mod tests {
    #[test]
    fn example_a() {
        let rules = "light red bags contain 1 bright white bag, 2 muted yellow bags.\n\
                     dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n\
                     bright white bags contain 1 shiny gold bag.\n\
                     muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n\
                     shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n\
                     dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n\
                     vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n\
                     faded blue bags contain no other bags.\n\
                     dotted black bags contain no other bags.\n\
                     ";
        assert_eq!(4, super::solve_a(rules.lines()));
    }
}
