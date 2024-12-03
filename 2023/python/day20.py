from collections import defaultdict
def solve1(s):
  s = s.strip().split("\n")
  m = {}
  t = {}
  r = defaultdict(list)
  rm = defaultdict(dict)
  on = {}
  for line in s:
    src, ts = [x.strip() for x in line.split("->")]
    if src == 'broadcaster':
      m[src] = [x.strip() for x in ts.split(",")]
      t[src] = 'b'
    else:
      t[src[1:]] = src[0] 
      m[src[1:]] = [x.strip() for x in ts.split(",")]
  for k, v in m.items():
    if t[k] == '%': on[k] = 0

  for k, v in m.items():
    for x in v:
      if x in t and t[x] == '&': 
        r[x] += [k]
  # print(r)
  for k, v in r.items():
    for x in v:
      rm[k][x] = 0
  # print(rm)

  lo, hi = 0, 0
  for i in range(1000):
    p = [('broadcaster', 0, 'button')]
    while len(p):
      x, f, se = p[0]
      # print(f"doing {se} {f} -> {x}")
      p = p[1:]
      if f: hi += 1
      else: lo += 1
      if x == 'broadcaster':
        for y in m['broadcaster']:
          p += [(y, f, x)]
      elif x not in t:
        continue
      elif t[x] == '%':
        if f == 0:
          for y in m[x]: p += [(y, 1 - on[x], x)]
          on[x] = 1 - on[x]
      else:
        rm[x][se] = f
        if all(rm[x].values()):
          for y in m[x]: p += [(y, 0, x)]
        else:
          for y in m[x]: p += [(y, 1, x)]

  print("Part 1:", lo * hi)

def solve2(s):
  s = s.strip().split("\n")
  m = {}
  t = {}
  r = defaultdict(list)
  rm = defaultdict(dict)
  on = {}
  for line in s:
    src, ts = [x.strip() for x in line.split("->")]
    if src == 'broadcaster':
      m[src] = [x.strip() for x in ts.split(",")]
      t[src] = 'b'
    else:
      t[src[1:]] = src[0] 
      m[src[1:]] = [x.strip() for x in ts.split(",")]
  for k, v in m.items():
    if t[k] == '%': on[k] = 0

  for k, v in m.items():
    for x in v:
      if x in t and t[x] == '&': 
        r[x] += [k]
  # for k, v in r.items():
  #   print(k, v)
  for k, v in r.items():
    for x in v:
      rm[k][x] = 0
  # print(rm)

  # for k, v in m.items():
  #   if k in t and t[k] == '&':
  #     print(k)

  # for k, v in m.items():
  #   for x in v:
  #     print(f"{k} {x}")


  lo, hi = 0, 0
  bt = 0
  while True:
    bt += 1
    print(bt)
    p = [('broadcaster', 0, 'button')]
    done = False;
    while len(p):
      x, f, se = p[0]
      if x == 'rx' and f == 0:
        print("Part 2:", bt)
        done = True
        break
      p = p[1:]
      if f: hi += 1
      else: lo += 1
      if x == 'broadcaster':
        for y in m['broadcaster']:
          p += [(y, f, x)]
      elif x not in t:
        continue
      elif t[x] == '%':
        if f == 0:
          for y in m[x]: 
            if not (y in t and t[y] == '%' and 1 - on[x] == 1):
              p += [(y, 1 - on[x], x)]
          on[x] = 1 - on[x]
      else:
        rm[x][se] = f
        if all(rm[x].values()):
          for y in m[x]: p += [(y, 0, x)]
        else:
          for y in m[x]: p += [(y, 1, x)]
    if done: break

  
def solve(s):
  solve1(s)
  # solve2(s)

# solve("""
# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a
# """)

# solve("""
# broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output
# """)

solve2("""
%vh -> qc, rr
&pb -> gf, gv, vp, qb, vr, hq, zj
%zj -> kn, pb
%mm -> dj
%gp -> cp
&dc -> ns
%qc -> gp
%dx -> fq, dj
%tg -> nl, ks
%pr -> nl
%gx -> xf
%hd -> lt, nl
%dq -> dj, jc
%ht -> jv
%bs -> pb, rd
&nl -> ks, cq, tc, xf, gx, hd, lt
&dj -> dc, fq, jz, ht, zs, jc
&rr -> gp, rv, jt, qc, sq
%vr -> qb
%jz -> dj, ht
%hq -> nx
%cf -> jg, rr
%hj -> cf, rr
%mt -> rr
%sq -> rr, vh
%jg -> rr, pd
%gf -> gv
%xv -> dj, dx
%rh -> nl, gx
broadcaster -> hd, zj, sq, jz
%jv -> dj, zs
%rd -> vs, pb
%pd -> rr, mt
&rv -> ns
&vp -> ns
%vs -> pb
%nx -> pb, bs
%zp -> mm, dj
&ns -> rx
%lt -> rh
%pf -> pr, nl
%tc -> qz
%xz -> dj, zp
%qb -> hq
%rl -> pf, nl
%fq -> xz
%kn -> pb, xn
%xf -> tg
%qz -> nl, rl
%ks -> tc
%jt -> kb
%jc -> xv
%kb -> hj, rr
%zs -> dq
%gv -> vr
&cq -> ns
%cp -> rr, jt
%xn -> pb, gf
""")