use std::{
  fs,
  collections::HashMap,
  iter::zip
};
fn solve(input: String) {
  let mut l1 = Vec::<i32>::new();
  let mut l2 = Vec::<i32>::new();
  for part in input.split("\n") {
    let items: Vec<i32> = part.split_whitespace().into_iter().map(|x| x.parse().unwrap()).collect();
    l1.push(items[0]);
    l2.push(items[1]);
  }

  l1.sort();
  l2.sort();

  let p1: i32 = zip(&l1, &l2).map(|(x, y)| (x - y).abs()).sum();
  println!("Part 1: {}", p1);
  
  let mut c = HashMap::<i32, i32>::new();
  l2.iter().for_each(|x| *c.entry(*x).or_insert(0) += 1);
  let p2: i32 = l1.into_iter().map(|x| x * c.get(&x).unwrap_or(&0)).sum();
  println!("Part 2: {}", p2);
}

fn main() {
  let input = fs::read_to_string("../inputs/day01input.txt").unwrap();
  solve(input)
}