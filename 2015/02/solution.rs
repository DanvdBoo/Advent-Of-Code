use std::fs;

fn main() {
  let input = fs::read_to_string("./input.txt")
    .expect("Should have been able to read the file");
  let mut total_area : i32 = 0;
  let mut total_length : i32 = 0;

  for line in input.lines() {
    let values = line.split('x').collect::<Vec<&str>>();
    assert!(values.len() == 3);
    let (l, w, h) = (values[0].parse::<i32>().unwrap(), values[1].parse::<i32>().unwrap(), values[2].parse::<i32>().unwrap());
    total_area += part1(l, w, h);
    total_length += part2(l, w, h);
  }

  dbg!(total_area);
  dbg!(total_length);
}

fn part1(l : i32, w : i32, h : i32) -> i32 {
  let sizes = vec![l * w, w * h, h * l];
  sizes.iter().min().unwrap() + 2*sizes.iter().sum::<i32>()
}

fn part2(l : i32, w : i32, h : i32) -> i32 {
  let ribbon = l * w * h;
  2 * (l + w + h - vec![l, w, h].iter().max().unwrap()) + ribbon
}