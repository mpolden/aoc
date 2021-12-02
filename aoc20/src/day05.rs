use std::error::Error;
use std::fmt;
use std::str::FromStr;
use std::str::Lines;

#[derive(Debug)]
pub struct BoardingIdParseError {
    id: String,
}

impl Error for BoardingIdParseError {
    fn description(&self) -> &str {
        "invalid boarding ID"
    }
}

impl fmt::Display for BoardingIdParseError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.id)
    }
}

fn find_region(min: usize, max: usize, upper: bool) -> usize {
    ((max - min) / 2) + min + (upper as usize)
}

pub struct BoardingId {
    row: usize,
    column: usize,
}

impl FromStr for BoardingId {
    type Err = BoardingIdParseError;

    fn from_str(boarding_id: &str) -> Result<Self, Self::Err> {
        let mut row_min = 0;
        let mut row_max = 127;
        let mut col_min = 0;
        let mut col_max = 7;

        for c in boarding_id.chars() {
            match c {
                'B' => {
                    row_min = find_region(row_min, row_max, true);
                }
                'F' => {
                    row_max = find_region(row_min, row_max, false);
                }
                'R' => {
                    col_min = find_region(col_min, col_max, true);
                }
                'L' => {
                    col_max = find_region(col_min, col_max, false);
                }
                _ => {
                    return Err(BoardingIdParseError {
                        id: boarding_id.to_string(),
                    })
                }
            };
        }
        Ok(BoardingId {
            row: row_max,
            column: col_max,
        })
    }
}

impl BoardingId {
    pub fn seat_id(&self) -> usize {
        (self.row * 8) + self.column
    }
}

pub fn solve_a(lines: Lines) -> usize {
    lines
        .map(|s| s.parse::<BoardingId>().unwrap().seat_id())
        .max()
        .unwrap()
}

pub fn solve_b(lines: Lines) -> Option<usize> {
    let mut seat_ids: Vec<usize> = lines
        .map(|s| s.parse::<BoardingId>().unwrap().seat_id())
        .collect();
    seat_ids.sort_unstable();
    for (i, seat_id) in seat_ids.iter().enumerate() {
        let j = i + 1;
        if j >= seat_ids.len() {
            continue;
        }
        let next_seat_id = seat_ids[j];
        if seat_id + 2 == next_seat_id {
            return Some(seat_id + 1);
        }
    }
    None
}

#[cfg(test)]
mod tests {

    use super::BoardingId;

    #[test]
    fn example_a() {
        let id = "FBFBBFFRLR".parse::<BoardingId>().unwrap();
        assert_eq!(44, id.row);
        assert_eq!(5, id.column);
        assert_eq!(357, id.seat_id());

        let id = "BFFFBBFRRR".parse::<BoardingId>().unwrap();
        assert_eq!(70, id.row);
        assert_eq!(7, id.column);
        assert_eq!(567, id.seat_id());

        let id = "FFFBBBFRRR".parse::<BoardingId>().unwrap();
        assert_eq!(14, id.row);
        assert_eq!(7, id.column);
        assert_eq!(119, id.seat_id());

        let id = "BBFFBBFRLL".parse::<BoardingId>().unwrap();
        assert_eq!(102, id.row);
        assert_eq!(4, id.column);
        assert_eq!(820, id.seat_id());
    }
}
