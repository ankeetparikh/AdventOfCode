use std::fs;

fn solve(input: String) {
  let mut p1 = 0;
  let mut p2 = 0;
  for (i, x) in input.chars().enumerate() {
    if x == '(' { 
      p1 += 1;
    } else { 
      p1 -= 1;
    }
    if p1 == -1 && p2 == 0 {
      p2 = i + 1;
    }
  }
  
  println!("Part 1: {}", p1);
  println!("Part 2: {}", p2);
}

fn main() {
  let input = fs::read_to_string("../inputs/day01input.txt").unwrap();
  solve(input)
}