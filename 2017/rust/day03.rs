use std::fs;
use std::collections::HashMap;

fn location(_n: u32) -> (i32, i32) {
  let mut n = _n;
  let (mut x, mut y) = (0, 0);
  let (mut dx, mut dy) = (1, 0);
  let (mut s, mut cs) = (1, 1); // s = cur side length, cs = cur side index
  while n > 1 {
    n -= 1;
    x += dx;
    y += dy;
    cs -= 1;
    if cs == 0 {
      (dx, dy) = (-dy, dx);
      if (dx, dy) == (0, 1) {
        s += 2;
        cs = s - 2;
      } else if (dx, dy) == (1, 0) {
        cs = s;
      } else {
        cs = s - 1;
      }
    }
  }
  (x, y)
}

fn p2(lim: u32) -> i32 {
  let (mut x, mut y) = (0, 0);
  let (mut dx, mut dy) = (1, 0);
  let (mut s, mut cs) = (1, 1); // s = cur side length, cs = cur side index
  let mut z = HashMap::new();
  z.insert((0, 0), 1);
  loop {
    x += dx;
    y += dy;
    cs -= 1;
    if cs == 0 {
      (dx, dy) = (-dy, dx);
      if (dx, dy) == (0, 1) {
        s += 2;
        cs = s - 2;
      } else if (dx, dy) == (1, 0) {
        cs = s;
      } else {
        cs = s - 1;
      }
    }
    let mut tot = 0;
    for (ex, ey) in vec![(1, 0), (1, -1), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)] {
      tot += match z.get(&(x + ex, y + ey)) {
        Some(z) => 0 + z,
        None => 0,
      }
    }
    // println!("=> ({}, {}): {}", x, y, tot);
    z.insert((x, y), tot);
    if tot > lim {
      return tot as i32
    }
  }
}

fn solve(input: String) {
  let n: u32 = input.trim().parse().unwrap();
  let (x, y) = location(n);
  // println!("n, x, y = {} {} {}", n, x, y);
  println!("Part 1: {}", x.abs() + y.abs());
  println!("Part 2: {}", p2(n));
}

fn main() {
  solve(String::from("1"));
  solve(String::from("12"));
  solve(String::from("23"));
  solve(String::from("1024"));

  let input = fs::read_to_string("../inputs/day03input.txt").unwrap();
  solve(input)
}