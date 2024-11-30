use std::fs;

fn main() {
  let input = fs::read_to_string("./input.txt")
    .expect("Should have been able to read the file");

  let mut level = 0;
  let mut pos = 0;

  for c in input.chars() {
    pos += 1;
    if c == '(' {
      level += 1;
    } else {
      level -= 1;
    }

    if level == -1 {
      break;
    }
  }

  println!("{}", pos);
}