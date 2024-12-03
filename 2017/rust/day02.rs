use std::fs;

fn solve(input: String) {
  let lines = input.trim().split("\n");
  let mut p1 = 0;
  let mut p2 = 0;
  for line in lines {    
    let a: Vec<u32> = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
    
    p1 += a.iter().max().unwrap() - a.iter().min().unwrap();

    let n = a.len();

    for i in 0..n {
      for j in 0..n {
        if i == j { continue };
        if a[i] % a[j] == 0 {
          p2 += a[i] / a[j];
        }
      }
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

  let input = fs::read_to_string("../inputs/day02input.txt").unwrap();
  solve(input)
}