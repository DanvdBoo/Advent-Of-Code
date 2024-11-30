use std::fs;

fn main() {
  let input = fs::read_to_string("./input.txt")
    .expect("Should have been able to read the file");

  dbg!(part1(input.clone()));
  dbg!(part2(input.clone()));
}


fn part1(input: String) -> usize {
  let mut visited = vec![(0, 0)];
  let (mut x, mut y) = (0, 0);

  for c in input.chars() {
    match c {
      '<' => x -= 1,
      '>' => x += 1,
      'v' => y -= 1,
      '^' => y += 1,
      _ => todo!(),
    };
    if !visited.contains(&(x, y)) {
      visited.push((x, y));
    }
  }

  visited.len()
}

fn part2(input: String) -> usize {
  let mut visited = vec![(0, 0)];
  let (mut x, mut y) = (0, 0);
  let (mut xr, mut yr) = (0, 0);
  let mut robot = false;

  for c in input.chars() {
    if !robot {
      match c {
        '<' => x -= 1,
        '>' => x += 1,
        'v' => y -= 1,
        '^' => y += 1,
        _ => todo!(),
      };
      if !visited.contains(&(x, y)) {
        visited.push((x, y));
      }
    } else {
      match c {
        '<' => xr -= 1,
        '>' => xr += 1,
        'v' => yr -= 1,
        '^' => yr += 1,
        _ => todo!(),
      };
      if !visited.contains(&(xr, yr)) {
        visited.push((xr, yr));
      }
    }
    robot = !robot;
  }

  visited.len()
}