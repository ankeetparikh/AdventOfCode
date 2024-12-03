use std::fs;

fn solve(input: String) {
  let a: Vec<char> = input.trim().chars().collect();
  let n = a.len();
  let mut p1 = 0;
  let mut p2 = 0;
  for i in 0..n {
    let v = (a[i] as u32) - ('0' as u32);
    if a[i] == a[(i + 1) % n] {
      p1 += v;
    }
    if a[i] == a[(i + n / 2) % n] {
      p2 += v;
    }
  }
  println!("Part 1: {}", p1);
  println!("Part 2: {}", p2);
}

fn main() {
  // let t1 = String::from("1122");
  // solve(t1);

  // let t1 = String::from("1111");
  // solve(t1);

  let input = fs::read_to_string("../inputs/day01input.txt").unwrap();
  solve(input)
}