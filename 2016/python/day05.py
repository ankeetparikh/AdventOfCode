import hashlib

def solve1(s):
	s = s.strip().split("\n")
	k = s[0]
	i, f, ans = 0, 0, ''
	while f < 8:
		inp = k + str(i)
		x = hashlib.md5(inp.encode()).hexdigest()
		if "00000" == x[:5]:
			# print("found at", i)
			ans += x[5]
			f += 1
		i += 1
	print(ans)

def solve2(s):
	s = s.strip().split("\n")
	k = s[0]
	i, f = 0, 0,
	ans = ['' for i in range(8)]
	while f < 8:
		inp = k + str(i)
		x = hashlib.md5(inp.encode()).hexdigest()
		if "00000" == x[:5] and x[5] in "0123456789":
			pos = int(x[5])
			val = x[6]
			if pos < 8 and ans[pos] == '':
				ans[pos] = val
				f += 1
		i += 1
	print(''.join(ans))


def solve(s):
	solve1(s)
	solve2(s)

solve(
'''
abc
'''
)
solve(
'''
reyedfim
'''
)
