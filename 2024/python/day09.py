with open('../inputs/day09input.txt') as f:
  contents = f.read()
a = [int(x) for x in contents.strip()]
N = len(a)
L = sum(a)
b = [0] * L
p = 0
for i, x in enumerate(a):
  for j in range(x):
    b[p] = i // 2 if i % 2 == 0 else -1
    p += 1

i, j = 0, L - 1
while i < j:
  if b[i] > -1:
    i += 1
  elif b[j] == -1:
    j -= 1
  else:
    b[i] = b[j]
    b[j] = -1
    i += 1
    j -= 1
p1 = sum(i * x for i, x in enumerate(b) if x > -1)
print("Part 1:", p1)

from collections import defaultdict
from sortedcontainers import SortedSet

d = defaultdict(SortedSet)
pos = {}
p = 0
for i, x in enumerate(a):
  if i % 2 == 0: 
    pos[i // 2] = p
  else:
    d[x].add(p)
  p += x
p2 = 0
for i in range(N // 2, -1, -1):
  block_start = pos[i]
  block_len = a[2 * i]
  assert(block_len > 0)
  gap_ind = L
  for j in range(block_len, 10):
    if len(d[j]) > 0 and d[j][0] < block_start and (gap_ind >= L or d[j][0] < d[gap_ind][0]):
      gap_ind = j
  if gap_ind < L:
    st = d[gap_ind][0]
    d[gap_ind].pop(0)

    pos[i] = st
    gap_rem = gap_ind - block_len
    if gap_rem > 0: 
      d[gap_rem].add(st + block_len)
  for j in range(block_len):
    p2 += i * (pos[i] + j)
print("Part 2:", p2)