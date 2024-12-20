import fluentpy as _
import re
from collections import *
from itertools import *
from math import *
from functools import *
import string

def solve(s):
	x = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
	)
	MX = 100000
	N = len(x)
	i = 0
	cd = []
	subdirs = defaultdict(list)
	files = defaultdict(list)
	while i < N:
		# print(line)
		if '$ ls' in x[i]:
			f = []
			while i + 1 < N and '$' not in x[i + 1]:
				f.append(x[i + 1])
				i += 1
			for elem in f:
				y = elem.split()
				if y[0] == 'dir':
					subdirs['/'.join(cd)].append('/'.join(cd + [y[1]]))
				else:
					files['/'.join(cd)].append((int(y[0]), y[1]))

		else:
			q = x[i].split()[2]
			if q == '/':
				cd = []
			elif q == '..':
				cd.pop()
			else:
				cd.append(q)

		i += 1


	def sizes(sz, path):
		for elemsz, elemname in files[path]:
			sz[path] += elemsz
		for subdir in subdirs[path]:
			sz[path] += sizes(sz, subdir)
		return sz[path]

	sz = defaultdict(int)
	sizes(sz, '')
	ans = 0
	for x, y in sz.items():
		if y <= MX:
			ans += y
	print(ans)

	TOT = 70000000
	REQ = 30000000
	FREE = TOT - REQ

	used = sz['']
	ans = 10**50
	for x, y in sz.items():
		if used - y <= TOT - REQ:
			if y < ans:
				ans = y
	print(ans)

print("SAMPLE:")
solve(
'''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
)

print("\nACTUAL:")
solve(
'''
$ cd /
$ ls
dir bsnqsfm
dir dtqvbspj
dir hhhtrws
dir ldmsq
307337 pnm.slh
dir pqcndb
dir pwtqzwv
212421 zcrfndg.cms
$ cd bsnqsfm
$ ls
179236 lccnhn
$ cd ..
$ cd dtqvbspj
$ ls
221336 gdjfp.mfp
273114 jjgpvcqv.jlq
$ cd ..
$ cd hhhtrws
$ ls
dir gcbg
dir jjgpvcqv
dir mgvdbtl
1606 mgvdbtl.ztt
dir qhv
27538 wprqtd.wph
$ cd gcbg
$ ls
dir bgcwh
dir bsnqsfm
dir jjgpvcqv
186683 lccnhn
dir rqbnd
32944 zjfs.mdf
$ cd bgcwh
$ ls
211273 nvns
$ cd ..
$ cd bsnqsfm
$ ls
dir bsnqsfm
210022 dtqvbspj
dir gpcpgfh
189603 pnm.slh
199755 rcsffv.gbt
$ cd bsnqsfm
$ ls
292856 bsnqsfm.vww
$ cd ..
$ cd gpcpgfh
$ ls
177703 jrr.jnj
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
233963 bsnqsfm.fnn
127603 gpcpgfh.gtw
dir jjgpvcqv
48213 jrs.bdw
172974 pnm.slh
$ cd jjgpvcqv
$ ls
dir bqnctqvn
dir bsnqsfm
dir gpcpgfh
254570 qpmnqwvl
258040 rrvjrv.zbp
$ cd bqnctqvn
$ ls
106211 bsnqsfm.pql
299973 dtqvbspj
dir nzrst
$ cd nzrst
$ ls
dir whtfvrl
$ cd whtfvrl
$ ls
12412 vzdrqs.rwt
$ cd ..
$ cd ..
$ cd ..
$ cd bsnqsfm
$ ls
293832 bggllqhj.dvb
$ cd ..
$ cd gpcpgfh
$ ls
196159 jrr.jnj
$ cd ..
$ cd ..
$ cd ..
$ cd rqbnd
$ ls
97630 ddjrjp
56378 rsb
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
89238 bsnqsfm.mgf
dir dvsst
dir gpcpgfh
dir jjgpvcqv
dir mhrzj
164176 pnm.slh
dir tmh
dir vmwz
$ cd dvsst
$ ls
286924 dtqvbspj
252366 hcnqdmg.zst
266562 wgfdmgmh.ptw
$ cd ..
$ cd gpcpgfh
$ ls
91199 jrs.bdw
78761 rspd.vmj
dir tbrbw
dir vvm
dir wplf
$ cd tbrbw
$ ls
195696 bjd.csj
56063 lccnhn
193863 pnm.slh
121918 qpd.dtq
209757 rcsffv.gbt
dir rmqlpvq
$ cd rmqlpvq
$ ls
dir gjgfvt
255533 lhdqqbg.fgm
68413 qltvgnrp.gfd
dir wqfcnlzq
$ cd gjgfvt
$ ls
242867 zqbdmpb
$ cd ..
$ cd wqfcnlzq
$ ls
dir vhhscrvb
$ cd vhhscrvb
$ ls
62647 rcsffv.gbt
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd vvm
$ ls
281698 dscllv.qwl
14348 rmgpnprq
$ cd ..
$ cd wplf
$ ls
44465 jjgpvcqv
248434 vpsfbjh.zsj
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
dir dhfcbc
dir jjgpvcqv
dir ltclg
dir ptbsgmlr
$ cd dhfcbc
$ ls
224134 lccnhn
197124 tns
$ cd ..
$ cd jjgpvcqv
$ ls
126322 jrr.jnj
280287 jrs.bdw
$ cd ..
$ cd ltclg
$ ls
dir fdfn
47501 jrr.jnj
dir mgvdbtl
24374 mgvdbtl.gll
227751 pnm.slh
286088 wvsfr
$ cd fdfn
$ ls
32987 hmt
$ cd ..
$ cd mgvdbtl
$ ls
201629 pnm.slh
246591 whtcjvh
$ cd ..
$ cd ..
$ cd ptbsgmlr
$ ls
239257 rcsffv.gbt
$ cd ..
$ cd ..
$ cd mhrzj
$ ls
279222 mgvdbtl.rzf
214102 rvjnddbr
$ cd ..
$ cd tmh
$ ls
152958 rcsffv.gbt
$ cd ..
$ cd vmwz
$ ls
131525 bsnqsfm.djc
122342 jrs.bdw
$ cd ..
$ cd ..
$ cd mgvdbtl
$ ls
24916 tcsltrml
$ cd ..
$ cd qhv
$ ls
dir hncvrlbw
153239 jwdg.wbg
$ cd hncvrlbw
$ ls
178499 clmwn.ztj
297967 jrr.jnj
30359 sntbnf.whh
$ cd ..
$ cd ..
$ cd ..
$ cd ldmsq
$ ls
dir jngnzc
dir psgrjgr
dir rgwp
dir rtsmnzm
dir wsd
$ cd jngnzc
$ ls
dir dzlcq
dir gpcpgfh
dir rlwwwngc
dir swrlvd
$ cd dzlcq
$ ls
70984 lccnhn
$ cd ..
$ cd gpcpgfh
$ ls
288159 hztmtp.fpj
$ cd ..
$ cd rlwwwngc
$ ls
173335 bsnqsfm.rtr
292723 jrr.jnj
175123 lccnhn
$ cd ..
$ cd swrlvd
$ ls
69589 fwrt
$ cd ..
$ cd ..
$ cd psgrjgr
$ ls
283186 dtqvbspj.hjw
dir fcvqsp
104691 jrs.bdw
286657 lccnhn
258194 rcsffv.gbt
$ cd fcvqsp
$ ls
209758 fzqmqlvs.hsc
$ cd ..
$ cd ..
$ cd rgwp
$ ls
11060 nwg.qcg
$ cd ..
$ cd rtsmnzm
$ ls
dir rdv
dir sdwmbsz
dir tjwht
$ cd rdv
$ ls
189234 nngdwngf.jpm
102320 qbq
$ cd ..
$ cd sdwmbsz
$ ls
dir dfzw
dir jbnsvcv
dir jjgpvcqv
140827 jjgpvcqv.cvz
$ cd dfzw
$ ls
168631 dhbfr
$ cd ..
$ cd jbnsvcv
$ ls
dir bsnqsfm
20840 lsgnjrn
83537 lvtbqlh
dir qfmj
$ cd bsnqsfm
$ ls
74345 jrr.jnj
$ cd ..
$ cd qfmj
$ ls
dir bfvwng
dir jjgpvcqv
$ cd bfvwng
$ ls
dir qzdpp
$ cd qzdpp
$ ls
dir jjgpvcqv
$ cd jjgpvcqv
$ ls
207083 rchw.lgb
$ cd ..
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
273755 dqmb
$ cd ..
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
190922 dtqvbspj.rww
59784 lccnhn
293765 mwvpgtzm
dir vtbln
dir wph
$ cd vtbln
$ ls
19558 jrs.bdw
72791 lccnhn
262803 pnm.slh
40575 sbdz
$ cd ..
$ cd wph
$ ls
174151 jrr.jnj
$ cd ..
$ cd ..
$ cd ..
$ cd tjwht
$ ls
dir mgvdbtl
136586 rcsffv.gbt
$ cd mgvdbtl
$ ls
dir gtmbf
$ cd gtmbf
$ ls
61244 jvs.gvw
269474 rcsffv.gbt
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd wsd
$ ls
275247 dtqvbspj.mjl
dir gpcpgfh
dir jdnfsqzd
88516 jrr.jnj
77096 lccnhn
dir lspqh
dir pfcmb
120975 tqzmlsz
215518 zvzhjd.ggw
$ cd gpcpgfh
$ ls
217225 lccnhn
dir qtnqzql
$ cd qtnqzql
$ ls
242800 rzfvcjvh
$ cd ..
$ cd ..
$ cd jdnfsqzd
$ ls
293894 ppdh
310316 rcsffv.gbt
$ cd ..
$ cd lspqh
$ ls
dir pspghgw
$ cd pspghgw
$ ls
105894 gpcpgfh.zht
20657 nccmrdjv.tml
241440 nrb.zrj
$ cd ..
$ cd ..
$ cd pfcmb
$ ls
64751 cfnptz
dir dmlsqf
dir dtqvbspj
288252 nfcdscgz
309178 pnm.slh
$ cd dmlsqf
$ ls
82960 czhbvv.fvc
238189 dtqvbspj.mqp
232175 lccnhn
$ cd ..
$ cd dtqvbspj
$ ls
dir fpq
99045 jrs.bdw
$ cd fpq
$ ls
98034 bnbvjg.nfq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pqcndb
$ ls
dir dtqvbspj
dir fvrtmdg
dir gpcpgfh
dir jjgpvcqv
dir mgvdbtl
dir pftswtnl
302354 rcsffv.gbt
dir zwph
$ cd dtqvbspj
$ ls
134541 mgvdbtl.gbr
$ cd ..
$ cd fvrtmdg
$ ls
dir gpcpgfh
231704 gpcpgfh.cgh
304822 jrr.jnj
$ cd gpcpgfh
$ ls
64193 ztqztct.ctr
$ cd ..
$ cd ..
$ cd gpcpgfh
$ ls
dir cmg
129101 hqcjs.fsf
dir jjgpvcqv
dir lmb
dir lzgc
dir nqvzvfb
dir rbh
149226 tzgn.sqv
257657 zbjzcn
$ cd cmg
$ ls
54041 bbrbwdw.mtf
233793 dtqvbspj.hjj
227618 jjgpvcqv.sls
36553 rcsffv.gbt
dir vsjs
$ cd vsjs
$ ls
199262 bsnqsfm
dir dqpqvsfn
dir ghw
73538 jrs.bdw
20726 mtfzjhc
$ cd dqpqvsfn
$ ls
91215 ppfmvz
$ cd ..
$ cd ghw
$ ls
dir bwhn
307330 jrr.jnj
25726 pnm.slh
$ cd bwhn
$ ls
dir gpcpgfh
$ cd gpcpgfh
$ ls
61301 mhchvsnp.lpv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
281936 zjfrwg
$ cd ..
$ cd lmb
$ ls
dir mmqr
$ cd mmqr
$ ls
60362 mbjdfmf.wfh
$ cd ..
$ cd ..
$ cd lzgc
$ ls
211543 rcsffv.gbt
$ cd ..
$ cd nqvzvfb
$ ls
288538 lccnhn
224852 rcsffv.gbt
$ cd ..
$ cd rbh
$ ls
dir cwgc
dir gpcpgfh
dir hdmmgms
dir jwqdv
75165 mgvdbtl.rdd
dir mzt
$ cd cwgc
$ ls
254910 ghsbvcw.wgh
$ cd ..
$ cd gpcpgfh
$ ls
8668 lccnhn
145750 mcpd
265522 rcsffv.gbt
$ cd ..
$ cd hdmmgms
$ ls
dir dtqvbspj
dir gpcpgfh
203642 jrs.bdw
19047 rcsffv.gbt
215131 tbdf
dir tgqbtw
$ cd dtqvbspj
$ ls
46484 hjztnq
14784 tmmf.ggs
$ cd ..
$ cd gpcpgfh
$ ls
123990 jrs.bdw
52381 mgvdbtl
130292 rrqp.pmz
$ cd ..
$ cd tgqbtw
$ ls
dir bsnqsfm
dir nnn
$ cd bsnqsfm
$ ls
279305 mgvdbtl.mhc
$ cd ..
$ cd nnn
$ ls
181320 jjgpvcqv.zcn
$ cd ..
$ cd ..
$ cd ..
$ cd jwqdv
$ ls
306471 jjgpvcqv.jbv
$ cd ..
$ cd mzt
$ ls
159120 wcfjbfsb.vlq
$ cd ..
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
dir drmmqldt
dir jjgpvcqv
235210 jjnbtgh
116214 lccnhn
dir mzj
dir qcclcdd
dir rtnnjct
dir trgbfqb
$ cd drmmqldt
$ ls
dir bsnqsfm
dir gpcpgfh
dir jjgpvcqv
$ cd bsnqsfm
$ ls
200217 gpcpgfh.bmf
$ cd ..
$ cd gpcpgfh
$ ls
183548 jjgpvcqv.cgs
119367 rcsffv.gbt
$ cd ..
$ cd jjgpvcqv
$ ls
dir bzhsjfq
dir lptnp
$ cd bzhsjfq
$ ls
37713 pnm.slh
$ cd ..
$ cd lptnp
$ ls
150154 jjgpvcqv.jpt
$ cd ..
$ cd ..
$ cd ..
$ cd jjgpvcqv
$ ls
dir csvpf
$ cd csvpf
$ ls
96915 bdsqr.ptg
15712 gpcpgfh.hbw
13419 pnm.slh
23191 vhzngpw.bdp
$ cd ..
$ cd ..
$ cd mzj
$ ls
216100 fblqpwgd.rmb
$ cd ..
$ cd qcclcdd
$ ls
67202 bdz.flj
51451 dtqvbspj
dir mgvdbtl
36642 rhc.qtg
252808 slqzl.hgz
$ cd mgvdbtl
$ ls
dir dtqvbspj
$ cd dtqvbspj
$ ls
142184 pnm.slh
$ cd ..
$ cd ..
$ cd ..
$ cd rtnnjct
$ ls
dir bsnqsfm
dir dtqvbspj
dir ftlr
dir grpln
dir wtjfbzjq
$ cd bsnqsfm
$ ls
dir gbp
$ cd gbp
$ ls
dir gpcpgfh
$ cd gpcpgfh
$ ls
157447 msdhpv
$ cd ..
$ cd ..
$ cd ..
$ cd dtqvbspj
$ ls
dir fbpz
dir mgvdbtl
$ cd fbpz
$ ls
118001 zzffss.qdv
$ cd ..
$ cd mgvdbtl
$ ls
dir gtbpnhhm
dir rvjdhdvf
$ cd gtbpnhhm
$ ls
115199 mgvdbtl.zhd
307710 pbqqz.dvg
$ cd ..
$ cd rvjdhdvf
$ ls
192704 lccnhn
49374 qsv.nzw
dir vnlq
$ cd vnlq
$ ls
dir zwtwvdb
$ cd zwtwvdb
$ ls
99356 cqfppfg.cwl
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ftlr
$ ls
dir fdm
$ cd fdm
$ ls
dir pdzbthz
$ cd pdzbthz
$ ls
dir gmpzrfv
286299 gmvg
32579 jrr.jnj
$ cd gmpzrfv
$ ls
44930 tfwc.sjb
76143 wtwpz
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd grpln
$ ls
dir thsbgczd
dir vdmt
$ cd thsbgczd
$ ls
231385 lccnhn
$ cd ..
$ cd vdmt
$ ls
dir qzwzwlpr
$ cd qzwzwlpr
$ ls
119862 qbpglhp.pmz
$ cd ..
$ cd ..
$ cd ..
$ cd wtjfbzjq
$ ls
308656 cvjrn.mmz
107735 mgvdbtl.pjv
$ cd ..
$ cd ..
$ cd trgbfqb
$ ls
59890 jrr.jnj
dir mhhbp
$ cd mhhbp
$ ls
dir bsnqsfm
dir hvjtmr
$ cd bsnqsfm
$ ls
80555 trsl.zjm
$ cd ..
$ cd hvjtmr
$ ls
78682 cgjqlrw
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd mgvdbtl
$ ls
85693 bsnqsfm.jft
dir gpcpgfh
136814 gvfz
243282 jjgpvcqv.phc
23472 mrq
dir tdnhp
188849 ztrvjzw.gjj
$ cd gpcpgfh
$ ls
dir bfjb
172798 blt
dir dtqvbspj
dir lwtj
$ cd bfjb
$ ls
9385 fhgqhrnq
$ cd ..
$ cd dtqvbspj
$ ls
dir zrtpvzh
$ cd zrtpvzh
$ ls
115949 gjcpswqv.tqg
$ cd ..
$ cd ..
$ cd lwtj
$ ls
269246 dtqvbspj.tmv
106980 jrr.jnj
20735 ldjswqtb.plp
$ cd ..
$ cd ..
$ cd tdnhp
$ ls
25816 lccnhn
$ cd ..
$ cd ..
$ cd pftswtnl
$ ls
60146 blg.vhz
dir cjzl
dir mgvdbtl
165072 mgvdbtl.cvq
dir rdhdqvm
dir swgdh
dir tgwws
101085 wtvlsbbf
139565 zfhlb.fmg
$ cd cjzl
$ ls
51636 hmwmvgg
$ cd ..
$ cd mgvdbtl
$ ls
dir dtlr
118691 pjjfwhwj
74684 rcsffv.gbt
253814 rgmn.csn
$ cd dtlr
$ ls
43065 dtqvbspj
$ cd ..
$ cd ..
$ cd rdhdqvm
$ ls
103093 bsnqsfm.rjd
5514 lccnhn
$ cd ..
$ cd swgdh
$ ls
dir dwznjd
230643 jjgpvcqv
296232 ltnlhbln.bqp
dir mgvdbtl
dir nbpdfrv
199830 rcsffv.gbt
$ cd dwznjd
$ ls
138849 jrs.bdw
240327 mgvdbtl
$ cd ..
$ cd mgvdbtl
$ ls
293382 dgrzgpr
218657 jjgpvcqv.lwt
dir pbw
125455 rcsffv.gbt
$ cd pbw
$ ls
242621 tnt.zbl
$ cd ..
$ cd ..
$ cd nbpdfrv
$ ls
297826 nfqbq.zfg
183227 qvr
148665 rcsffv.gbt
$ cd ..
$ cd ..
$ cd tgwws
$ ls
dir bhr
dir gpcpgfh
$ cd bhr
$ ls
dir wfjfvb
$ cd wfjfvb
$ ls
dir jgfbpwjh
13720 lwnz
38140 wrgb.ntr
$ cd jgfbpwjh
$ ls
207048 cbtdqb
176591 mgvdbtl
311612 nwflw.mmp
92978 pwrrz
273467 rnzzs.wrr
dir vsmgcv
$ cd vsmgcv
$ ls
dir dpdmspz
$ cd dpdmspz
$ ls
dir bsnqsfm
$ cd bsnqsfm
$ ls
197093 wzqlhhpv.lgb
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd gpcpgfh
$ ls
98093 lccnhn
208835 llplrrr.jrp
$ cd ..
$ cd ..
$ cd ..
$ cd zwph
$ ls
dir cmznd
$ cd cmznd
$ ls
dir zhhm
$ cd zhhm
$ ls
204738 rjh.qjf
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pwtqzwv
$ ls
21382 gbcccm.jdc
dir hthq
dir jcsmcf
dir jjgpvcqv
262556 mgvdbtl.vrm
dir twrjfd
dir zzclqz
$ cd hthq
$ ls
dir dtqvbspj
dir mgvdbtl
dir wgcss
$ cd dtqvbspj
$ ls
35525 gpcpgfh.wpc
4808 jjgpvcqv
dir lrvftwzb
dir nzvbpcwd
$ cd lrvftwzb
$ ls
92705 rcsffv.gbt
33209 wvthcng.qlf
$ cd ..
$ cd nzvbpcwd
$ ls
dir tzvclhw
$ cd tzvclhw
$ ls
251094 gpcpgfh.bpj
$ cd ..
$ cd ..
$ cd ..
$ cd mgvdbtl
$ ls
229319 hvzhcpr.dbc
301679 lrvlp.bnl
157154 pjq
129501 sgqsjl
$ cd ..
$ cd wgcss
$ ls
37019 fpmmqmv
286113 gpcpgfh.mrm
dir jjgpvcqv
132664 lccnhn
194995 pnm.slh
$ cd jjgpvcqv
$ ls
116833 pnm.slh
$ cd ..
$ cd ..
$ cd ..
$ cd jcsmcf
$ ls
146144 jjgpvcqv.jvj
$ cd ..
$ cd jjgpvcqv
$ ls
dir gdrqbn
dir nwbqdd
$ cd gdrqbn
$ ls
149865 bsnqsfm.zjh
1714 jjgpvcqv.lwq
$ cd ..
$ cd nwbqdd
$ ls
14359 bsnqsfm
77969 dpqt.lph
285861 dtqvbspj.svq
dir gpcpgfh
156597 hhsfwctl.hng
15497 mgvdbtl
$ cd gpcpgfh
$ ls
275833 gpcpgfh.hdd
$ cd ..
$ cd ..
$ cd ..
$ cd twrjfd
$ ls
302115 gpcpgfh.zcb
dir gqlqnpvm
20848 rcsffv.gbt
$ cd gqlqnpvm
$ ls
123135 gpcpgfh
57433 gpcpgfh.zfp
$ cd ..
$ cd ..
$ cd zzclqz
$ ls
217719 vcq.flg
'''
)