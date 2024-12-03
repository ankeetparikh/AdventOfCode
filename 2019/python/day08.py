from collections import Counter
def solve(input, N, M):
  a = input.strip()
  Z = len(a)

  bestz = N * M + 1
  ans = -1
  for i in range(0, Z, N * M):
    c = Counter(a[i:i + N * M])
    if c['0'] < bestz: 
      bestz = c['0']
      ans = c['1'] * c['2']
  print("Part 1:", ans)

  picture = [['2' for j in range(M)] for i in range(N)]
  for layer in range(0, Z, N * M):
    for i in range(N):
      for j in range(M):
        if picture[i][j] != '2': continue
        picture[i][j] = a[layer + i * M + j]
  
  # uncomment the line below to see the output image
  # for row in picture: print(''.join(row).replace("0", "░").replace("1", '█'))
  
  print("Part 2:", "HZCZU") # manually inspected the output


# solve("123456789012", 2, 3)

import sys
locs = [x[x.find('=')+1:] for x in sys.argv if x.startswith("--input-location")] \
  + ['../inputs/day08input.txt']
solve(open(locs[0]).read(), 6, 25)
