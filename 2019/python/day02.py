def solve(input):
  def result(noun, verb):
    a = [int(x) for x in input.strip().split(",")]
    
    a[1] = noun
    a[2] = verb

    i = 0
    while True:
      if a[i] == 99: break
      if a[i] == 1:
        a[a[i + 3]] = a[a[i + 1]] + a[a[i + 2]]
        i += 4
      elif a[i] == 2:
        a[a[i + 3]] = a[a[i + 1]] * a[a[i + 2]]
        i += 4
      else:
        raise Exception("bad opcode")
    return a[0]
  print("Part 1:", result(12, 2))
  for noun in range(0, 100):
    for verb in range(0, 100):
      if result(noun, verb) == 19690720:
        print("Part 2:", 100 * noun + verb)


import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day02input.txt']
solve(open(locs[0]).read())