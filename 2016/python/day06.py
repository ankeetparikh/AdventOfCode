from collections import Counter
def solve1(s):
	s = s.strip().split("\n")
	res = ''
	for j in range(len(s[0])):
		ch = Counter(s[i][j] for i in range(len(s))).most_common()[0][0]
		res += ch
	print("Part 1:", res)

def solve2(s):
	s = s.strip().split("\n")
	res = ''
	for j in range(len(s[0])):
		ch = Counter(s[i][j] for i in range(len(s))).most_common()[-1][0]
		res += ch
	print("Part 2:", res)


def solve(s):
	solve1(s)
	solve2(s)

# solve(
# '''
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
# '''
# )

with open('../inputs/day06input.txt') as f:
  s = f.read()
solve(s)