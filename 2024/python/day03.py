import re

with open('../inputs/day03input.txt') as f:
  inp = f.read()

results = re.findall("mul\((\d+),(\d+)\)", inp)
p1 = 0
for x in results:
  p1 += int(x[0]) * int(x[1])
print("Part 1:", p1)

results = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", inp)

p2 = 0
valid = True
for x in results:
  if "do()" in x: valid = True
  elif "don't()" in x: valid = False
  elif valid: p2 += int(x[0]) * int(x[1]) 
print("Part 2:", p2)