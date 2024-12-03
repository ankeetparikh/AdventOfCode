import re
from collections import defaultdict
def solve(a):
	n, p = list(map(int, re.findall("\d+", a)))
	def go(p):
		ne, pr = {}, {}
		ne[0] = pr[0] = 0
		cur = 0
		sc = defaultdict(int)
		for i in range(1, p):
			if i % 23 == 0:
				for j in range(7): cur = pr[cur]
				sc[i % n] += i + cur
				p, q = pr[cur], ne[cur]
				ne[p] = q
				pr[q] = p
				cur = q
			else:
				p = ne[cur]
				q = ne[ne[cur]]
				ne[p] = i
				ne[i] = q
				pr[q] = i
				pr[i] = p
				cur = i
		return sc
	print("Part 1:", max(go(p).values()))
	print("Part 2:", max(go(100*p).values()))


solve(
'''
9 players; last marble is worth 25 points
'''
)

solve(
'''
10 players; last marble is worth 1618 points
'''
)


solve(
'''
13 players; last marble is worth 7999 points
'''
)

solve(
'''
459 players; last marble is worth 71320 points
'''
)