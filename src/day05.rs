use std::error::Error;
use std::fmt;
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
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
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

impl BoardingId {
    pub fn seat_id(&self) -> usize {
        (self.row * 8) + self.column
    }

    pub fn from_str(boarding_id: &str) -> Result<BoardingId, BoardingIdParseError> {
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

pub fn solve_a(lines: Lines) -> usize {
    lines
        .map(|s| BoardingId::from_str(s).unwrap().seat_id())
        .max()
        .unwrap()
}

#[cfg(test)]
mod tests {

    use super::BoardingId;

    #[test]
    fn solve_a() {
        {
            let id = BoardingId::from_str("FBFBBFFRLR").unwrap();
            assert_eq!(44, id.row);
            assert_eq!(5, id.column);
            assert_eq!(357, id.seat_id());
        }
        {
            let id = BoardingId::from_str("BFFFBBFRRR").unwrap();
            assert_eq!(70, id.row);
            assert_eq!(7, id.column);
            assert_eq!(567, id.seat_id());
        }
        {
            let id = BoardingId::from_str("FFFBBBFRRR").unwrap();
            assert_eq!(14, id.row);
            assert_eq!(7, id.column);
            assert_eq!(119, id.seat_id());
        }
        {
            let id = BoardingId::from_str("BBFFBBFRLL").unwrap();
            assert_eq!(102, id.row);
            assert_eq!(4, id.column);
            assert_eq!(820, id.seat_id());
        }
    }
}
