from functools import lru_cache

def solve1(s):
  s = s.strip().split("\n")
  f = {}
  g = {}
  v = {}
  for line in s:
    a, op = line.split(": ")
    if " " in op:
      f[a] = op
      x, y, z = op.split(" ")
      g[a] = [x, z]
    else:
      v[a] = int(op)
  @lru_cache
  def get(a):
    if a in v: 
      return v[a]
    else:
      vars = {b:get(b) for b in g[a]}
      return int(eval(f[a], vars))
  print(get("root"))

def solve2(s):
  s = s.strip().split("\n")
  f = {}
  g = {}
  v = {}
  for line in s:
    a, op = line.split(": ")
    if " " in op:
      f[a] = op
      x, y, z = op.split(" ")
      g[a] = [x, z]
    else:
      v[a] = int(op)
  def get(a):
    if a == "humn":
      raise Exception
    elif a in v: 
      return v[a]
    else:
      vars = {b:get(b) for b in g[a]}
      return int(eval(f[a], vars))
  print(get(g["root"][1]))

def solve(s):
  solve1(s)
  solve2(s)

solve1(
'''
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
'''
)

solve(
'''
vbfg: 2
dwgb: 3
ctlr: 3
rzwt: fdqz + hpqd
qwlr: 3
hgbz: 2
mbqp: cfmj + gqrj
tmrn: 3
hbvn: rnrm * brjj
pjjr: bvpg + tfqn
fdnr: 10
vgcz: jngf * mgzw
zzvb: 2
cgnn: 5
jqqq: fmvt * vhzd
wlgc: 3
qmjl: 2
pjsd: gzgp * vnsp
vtsq: hctt / lmqf
blgq: 1
nrch: 13
lvjf: tjzh * ffsc
jczs: 5
rfrs: 3
vjwh: mwdw * bhnw
wpvc: jlzw * mfvr
rgbh: 2
htzb: mttr + mqmv
bwbl: pmhf * lfsd
zfdj: 1
pjzf: tppt * ftnh
wzfg: hhjv * dlph
lddf: qjnr / ffvl
jtfj: 17
vqhs: 5
tlrl: 4
httg: hhjb * zhzb
dbrq: hfgs * qlwz
qgjz: hqmg * jchz
jfbw: 2
swmc: rldn + cdgs
jpms: 2
jmmr: 5
lfjw: qngl + tbhl
lstl: 5
gfrz: 2
hldd: 11
mdrm: 19
bnqb: 8
stbv: dwsv + bvhp
glwg: jpzc + djqc
qdcm: lgsd + fjwr
sfgh: 2
bdsr: phdn - gpmn
hldm: mjsp * djsm
wlqt: 6
rftc: twcq * fgnd
qrcn: rntw + gcdg
nntn: 2
vljq: bbnn * gprr
mstq: 2
rbhz: schl + jwtq
mdwj: zhbj + qrfp
cfgp: pnhq - zfdj
nwnh: 7
dvgv: 2
wmrl: wjrw + llvf
ldzp: mlwd + mqcz
cnvf: jqfj / nmdl
qqbg: njsw + dvnc
mzmm: 3
ncwm: 2
wrmh: dprw / jjsd
qrht: zprs * jsqg
znlm: cmgv * lqpm
jlsn: 6
fjfv: ljql + fppt
ffjf: 5
gzsp: 5
ptrh: 13
vfsw: dvvp + gjvc
slgm: 3
lpcg: dsnq + btnn
rhlb: zhrc + jcjv
chfc: 10
dptd: 2
mlhh: cpwr / nbsf
sfqb: 2
zvtn: cbsp * zwsm
bbcc: tmtp + prfm
jwwb: nfdz * zhdj
zhdt: jdfz + fhpp
sdwq: 3
pwcz: vmgn * gwlt
lfcz: 2
pzfh: hjmt / zpfg
hctt: nfwb * wgrs
msgl: 6
lqlw: vnfc + qlwn
lddp: mchv * htwg
zrtc: pwjc + nrpb
nsmp: 2
nrwj: 2
rhhp: cnvf + rjrf
lltr: qbzq + jszc
qrfp: 4
fbtv: nvql + fsrg
nhqr: 3
hghw: pmsr / mmsw
wldw: 3
hfvw: vqjf + wfgc
cmpc: 2
wrst: 2
ntzz: 5
ccvh: 2
fftf: gfpp + cfmn
sfcf: vtsq - dzwb
pltq: 3
lljs: 2
pqfd: 3
wtbg: 5
mhpf: 3
mccg: wbhc * grrr
mfrl: zcvd / chld
rnfh: wqgg * dfrr
fscc: 4
sfrv: 7
frtg: 2
hnmn: 3
hhzv: 2
rstc: rwwl * ftjl
qtdr: vnch + ntbv
jmcf: 5
mgsh: tmbg * lswz
rqsh: 11
blmh: tbhz - vhbg
vwgj: nzvn * gfrz
qclt: nnvb / cmpc
jhrh: 3
lbqs: 4
zbwc: ntsp + rnfh
ndvz: zsfr + ftzh
rwdr: fdpq * pccw
qzlq: gfbc - vtnb
hwfd: ftmf / gjdb
hcfd: 17
hbdp: 3
vzhw: nhqw * tmlc
gpzt: lglv + hldd
dtns: 8
ttbq: 3
cnnw: hdnh + bhlv
vmcn: 4
ddgb: 3
cdrj: 4
jqfl: 2
lnfg: 4
hcgp: 6
pfjs: 3
frdt: bhfn + vqdw
mpgn: 3
hgvp: 2
przl: 5
ptqz: 2
zzvh: qntv * cbsb
gfdw: ctlm * rctr
nhsd: 3
nrld: rjww * wsns
bjng: gldg * zpcv
crwm: jttb + bwbl
cdnl: hjwh / hgrg
mjvl: 2
mhjs: lcqf / drlq
sglg: 3
hchl: wbzs / wjwc
nnwg: 8
hghd: rwdw * cmmf
lnlh: mddj * vrzs
sjpp: dwlz + qnwt
hdcw: vszc * cgzl
hlbd: qrht + lnlh
lzlg: vmpw * bvqq
thlv: clnz * qvcb
hlnl: 2
tjwc: 3
fzmp: htvj / fszn
fvfj: 2
wphb: hlcj * mwcc
qtgr: 2
bjvp: fsjv * zsjb
gfvf: 5
chjr: nntt * gplc
hwls: rsgc * slwr
rmcv: 14
lrhw: 3
pnhq: ljts + gbhr
lwqq: bccm * wjlz
cqlp: cgjf + gfvf
nfgv: hwcq * qvdd
prlb: 12
tdcr: zbdn + tfzl
spbs: fbtv + zcvh
dfnv: 1
tmjj: 7
mjsp: tbtc * hdqf
hbjl: glqm * crss
dbfs: 2
jfqs: 3
spww: zppb * mrmc
msvh: tfmq + hrzl
rbvb: ljnn * pftv
lzpw: clll + slzl
tfcs: 4
bgwg: 3
mgpj: pnwt + pbrt
zhrh: fcvq * rnwn
zlwg: 9
ncgt: 3
hvlv: 2
gcdg: hnwb - zbmj
tpww: 5
qsqw: wldw * zlhb
lfdm: 3
bbtq: 2
ghch: 2
bjqp: ssgw * nchg
qzrv: pcdv + mwzc
mbgb: mhvg + drft
gzbc: 5
ncrd: qqwf * phjw
hpzf: 2
rntw: cnzm / nrpt
tllp: 2
wrff: vjmp - zpfh
llcq: 14
lfdd: 5
blcm: rjzv * phrq
htbc: 13
hqnl: 5
mbjt: 2
mldp: 12
lgnh: rbvd - gvrm
cfmg: 10
fgsd: 2
sgws: zwcl * tqrl
lgcw: 20
cmzt: fmvz * zjlh
fssb: bgcs * rrvs
ntzh: 2
rfpp: 2
jgfg: 2
ppvj: 4
bcvc: gtpb + wjvz
spfg: 4
csvr: hlbd / vrqz
rphf: 2
hdnh: 16
fjwr: fjvf * nwlt
hlqg: ccmz + hzfj
hpdp: qlhd + jwwb
hmgd: 5
zbdh: rmvv * bggc
hpcn: cdnl + zltq
dnhd: vjbn * bhtd
mlnf: 12
hnzz: 20
zlsq: mhpf * htnm
jqcj: 4
mlct: 5
nzmv: bttg * vshr
jwdq: zhzl * hsgn
crww: 3
lzcp: dhtg * pltq
hggn: 2
qdfs: 3
rqlv: sfss + mqpr
lbcq: drrb * gvld
jqtj: 3
fsqs: 5
wjrw: jzps * ptjz
lgpw: jjcq * fgfg
rzzz: 15
fmwb: 19
mmtb: 3
cgfp: 2
chmm: 3
ljgz: csvr + lppw
vqfq: hfhc + ngml
ldmt: 4
zhhm: 9
fzpt: 3
ssdr: 13
fwnf: pjpr * gtvw
bbqf: bjng - msgl
bbjt: 7
fdpp: 14
nntt: 2
dpst: 2
gnmt: 15
wngv: 4
vzjm: jdzc * cwtn
jfpl: njls + gdgj
cqfh: vcmt + qglp
dzwb: 2
mvwr: hbml + dbsd
zsbm: qnsj * mwjn
lfqf: 2
vqdw: zrwd + hppn
rrvs: 10
rsbb: 2
crzd: flnb - pshd
cgzl: 2
zvrn: mvzw + wmrl
ftmf: wzcw - vssf
pjpr: 5
hswl: gczz / nnth
vnww: 5
dbsd: 3
tghv: zgsm * hcfm
ttzb: phzt + ntnq
ppmn: hrwm * rjhr
ndmn: 5
zhvq: mgfs - bnfw
zqfw: 3
hwmd: 7
hlmh: 3
ndlp: 13
vbgt: 14
vqsz: ccpw * wqsm
ldsz: 3
wdqs: 1
zwsm: 4
ldfp: lzcp + nfgv
ffdv: gwqq + wpqr
crmv: 2
fwlf: hfcg / jsbq
dqvm: bvbt / nrvs
qwhg: hnng / tdrs
rnqm: btjz + zvfv
rhqg: nzzq + sbqt
vwmm: mrwm * zdbn
zbfs: 2
thnm: swtb * whdm
qvpm: bcvh * hnjc
pjdr: 2
qvzl: 5
ppjb: 2
cmbj: ccpc + qfpd
hhjb: 2
wpcs: jswt * zcnh
jqhd: pmvv + jdvv
nsln: 3
fshs: 5
vrpw: 2
sqgq: 7
pmhf: rhln + frbr
hcrj: jwhp - jnwm
mswg: hrcv + fqlc
gtnp: hvpg * qsfc
vsbz: ljfn + sjpp
ssqs: 2
lqqg: 4
bhlv: gtmz * sjlw
lnvg: rldv * fhmj
rwwl: gslb * svzn
fmql: vwfn + bzcd
tnqc: chbz * nrbv
cqhd: gdvb / swsc
vgqb: wnfn - wldl
vhbg: 5
pmcp: 13
pflz: tjnh * wcwl
dvnp: lqzn * jmdr
lsgf: vpmd + tggg
sszs: ndhf * jncv
qqnq: gmnc * gmbp
lcmt: cdrj + gdmt
wsmp: fstv * zvrn
rhvw: psbw * lfgf
htdr: spbs - pdrt
mtrz: rmjp * glfz
mzvv: hzbh + qmjl
pmvv: mljh / dwfs
bjnm: fdsj + dwlf
jjrr: 19
dqch: 2
rmnr: 8
qtnb: cbwc * mdzm
dwzg: 16
nggz: 6
zsmn: 4
hnng: rqtc * cbph
qjbg: tjcz * thwh
fqtt: humn - jvzc
gwqq: zffv / jwmg
wqqh: 3
slzl: frhj * nsjn
mljb: 4
wcrr: mhnh + tgzm
fgnd: 5
ndps: wjdd * hgbz
rjqv: 7
cftz: 2
thdb: gqpf * ccrg
zffv: tddq + qpdb
jqmv: dhpt + nfvw
mjmc: 17
hwvn: 19
bngh: 2
pnrp: 4
jtjc: 2
glzn: 13
bbmz: 7
hjwt: dhtw * tpjh
prlg: gdcz * ljsb
jlbt: 3
wmwq: 4
fqwr: 3
qzvd: vtff - lpcb
bjhf: 5
tllg: vpqs + dcfb
gnht: 5
qpwh: qlmp * gcvh
zcvd: svrv * bwsq
wbzs: ntzh * rhvw
hrqs: jhqr * vhhr
hpfc: 2
bqtt: 4
nchg: jznm - zzlw
gpwn: 3
hcwt: 7
wcvv: bfcn + vmcn
rwfm: 2
mgmr: gnvg + fshs
dvnc: nhfw + nrzh
tddg: chpw * wfqb
djlv: 2
nbrv: 17
vpth: 15
ccrg: nggz * prht
cjbz: gswq + ppcg
gbdg: 6
bnfw: 16
dlpb: nmpj * dnpd
qvgz: 11
swsc: 3
sctw: 2
fjrq: 3
hblv: 5
qpvf: hgqf * zrtc
cmms: jsjd - tbth
tstv: dplp / nnjb
pgzc: rnds * qtrs
scwc: cwsc + ppmn
nwcn: 12
nzpn: 13
vssf: ncwm * rzwt
ljsh: nggd * htjn
jdgt: pgzc * gnht
scmj: 3
lgdd: 3
pwgf: 3
btml: mtjr * hwmd
msvj: 1
rmpc: qmfm + rrws
qccw: 9
nvqd: 2
cvpw: bbtq * smzb
rjvr: hzcg - tgtp
ctlm: 2
nrzh: btsl * lgqq
mnmq: jqtr * qzct
jdzs: 2
pbff: 2
zhzc: gcfc + nmfc
bwwz: mztz * zgfb
wldl: jdfv * wjwp
brns: 8
zsfr: 1
lccj: qjbg - mzbz
lnbv: 5
qbzq: nnws * hlvd
hlwz: dvhc * ngdf
stbf: 5
hvgv: 3
dqjb: 3
zpfg: 2
wmzn: 2
ssdb: 3
sdsg: cccn + msqr
jdzc: 11
blsf: pnmj * bngh
dcpd: 3
ptmd: 3
wlch: rgdw - nlqt
tsdf: dvcz * mglc
jmjw: dzdf / lpcg
prvw: 3
mcdz: bqtt + wpfb
mrfv: 12
zqvt: 5
dlph: 12
wdpv: 5
wpfw: 3
wwwc: qvds * ztjs
rjfs: 5
jvdd: 15
tjvl: dhvd - wfqq
fppj: 12
mgzw: dfmg + mlnf
cnrn: nswf * mstq
mhsd: 2
bzdd: srzw * srlt
wgjt: hrvl + gznh
zbmj: jtjc * rvdz
gldg: 7
vgsr: vwmp * mvvj
grqv: qpls * hchl
vcgw: 2
ddcb: 10
nwhj: zzlq * lzdj
fndj: ppdj * hbtv
cwcv: 5
qzzs: zzmg - djgj
qntv: 2
rhln: lqvp * mmgv
zpwf: nqfw * tmjj
plvm: 2
hcmb: 5
wgwv: jfpl * wlhm
cmbf: spzt * lhcn
drdc: 5
swnc: dsnd - tnvf
zvrs: 2
bvhp: mgds * gqbq
rchm: 3
clll: tmmz + thqn
gplr: 11
gwww: jcmg + ccvh
tzlt: zvgj + phdc
zhgr: 2
wpfb: stcj * tfqj
lcqs: mmzw + dpvw
jctj: flhq * wclf
zfdf: 3
wssf: vgft + zgvh
wjrm: 10
vncm: 4
lttb: gpwn * hdpf
zlph: smbf - hcmb
mjpl: 2
fwgr: hvlv + bzdd
chvp: 4
rptg: 7
zpcv: 5
tzfp: bjnf / sfgh
pmzj: fwhp + wcvw
jmdn: 3
nzjg: 11
cjzn: 5
lzbf: 3
ltsn: hqqp + zbfs
hlwv: rbfv * wtnt
dvvp: 5
mzpf: 2
rrmg: 5
hqqq: 5
wjwp: jdzs * hsrq
mlqm: 8
sntl: 5
phdc: wgjt * bqcb
vhgq: 4
vcbv: wqtw + qdfm
qvnj: vcmg * nsrm
mwzc: thdb + scjj
nslr: 4
zqvd: 3
wqsm: 6
tbzv: zzvh * ghch
swtb: pbhn * hhqv
hcvh: 16
tczg: 2
mnfg: 7
qnrt: mtml * tjjs
vnwg: rslr + pflz
fbnl: 3
wdng: 2
tqdf: 11
wgfd: 8
jbwv: hzjv * fphs
rmvv: 5
nqvq: 3
gcld: 10
slbf: 5
rhwv: hrnv * qvtp
rwdw: dgvf * dbhl
hqfv: 15
hnmz: tqpv * hjdd
smjz: 3
ztvv: 10
tscq: zjwz - jjjt
zchz: qbjd * rzzz
bpns: wgrt - brfg
ljbd: gfhl + pmzj
tfqn: cczl * ztvv
ndpn: 3
btbn: wlqt + wdpv
cbsp: 4
rlfn: mslj / jlsg
srgf: 2
gcww: cqhd / nvqd
dshb: tppn * jrmg
cnjr: fnwv / tqrq
fstv: 5
nvgq: sdfm * fbwc
cmrt: chht + wncd
pncc: hpnn * nwqw
gfsb: jqfl * qszr
hlng: lszc + hjrd
nldc: 20
wsdr: 9
dvfp: 5
ffqv: hcdc * prdt
hjwh: gbsl * mjpl
dtpf: wphb + tblh
bdww: 12
hcrm: 5
vzfc: 6
rvjc: rwjl * ntzw
sjqq: 13
lrvl: 2
bszg: zhgr + wnnf
plzr: 19
bcpv: bgzj * dfbh
qjjd: 16
csjp: glgt + hqjf
bgtp: rtnm * hbdh
ctqr: 2
hqsp: 2
rjww: 2
fnpj: 17
lwfm: 2
msff: vlgf - qjgt
mgds: 3
vrzs: brng * rpnq
qwph: rgfh + msfq
prjh: 2
bsqc: hlng / tntr
zcwc: 2
fhpw: rmnr + srcq
dplp: ncvh * mjvl
mdgl: bqht + lztt
tdch: 6
ngvh: 10
cbsb: 11
ndtc: 3
ngsm: qgqp * pnzq
gbfm: 4
humn: 1953
jlsg: 2
cmmf: gbtc * rhqb
zbtz: 3
bqhf: zvcw + vqfq
czsf: ddll * hlmh
vdvd: 4
dzgh: 11
jqhr: ssdr * vfbf
fmvz: gvgb + cclh
dhtw: hfrz * mclw
gtvw: pqdc * dqch
tgzm: 11
tqrl: 3
wmwn: tfrr + mhjs
lvpq: 1
tqrq: 2
mcsc: 4
lszc: bpll / lnfg
hwwm: 18
jqmz: trpm * lstl
phlw: npgp * rjqv
nsvt: 3
tgtp: ctvm * vpjw
jjzc: lmqm + jmcf
qvjs: spzc + jrdq
qzph: 2
pnzl: 2
nfdz: 7
mzgg: 10
srrv: 13
nnjz: 5
nfhv: 2
rdgt: 3
tfmq: gvwq * grtl
cjrd: bgtg * hswl
wtnp: fqbr + hggn
bvlv: 2
qdsg: 7
cnjg: zsrs * gtfc
ffvl: 4
zpmq: 3
mbmg: 5
rfbv: 10
hcqj: 5
sqzv: 4
lsbv: wrff * jvdd
htvj: mtzp + wrmh
ddfm: 5
qmfm: mjzd / spct
spcc: 17
fvcn: 20
fbgz: nqmm + pwcz
sfzn: 6
vjnd: grnb * ffqv
tpjh: 2
frbr: dbht + rgpc
nhtr: 3
dtvr: 8
cpwr: zhrs - tcbz
dsnq: 4
jshl: rvjc * jhdc
ljpg: zzdv - lbsd
tmmr: 9
fdpq: 2
hdqf: 5
jqtr: 2
bpct: 3
ggzj: ctqr * wssf
gcpq: tlzg + wdqs
vqrn: mwgz + bjqp
bppf: hddh + sqgq
vdmp: qrhv * mpgw
mwqn: pbfj / mzvv
fgfg: 3
hhjv: 17
dhbb: jfbw * wlzg
nbsf: 5
rslm: 13
dvss: 19
dwsv: 3
fsrg: 16
prvm: 2
hblr: jbvr * jqts
wdcn: 13
bmfs: pnbv + rnls
mnms: sfqw * sfrv
phnv: vnft + pprw
tfmw: dsll + hwjm
brwh: sntl * mtrw
zgsr: 2
qwhh: 3
tlpz: tmvc * sdlv
wbwv: zhmn + hdvc
jwzn: 7
sfwf: 3
mgmb: ndtc * pbgc
ngsf: 4
vwfn: qvlz + ghcl
hcdp: gfsb + qzph
qvtp: 2
qglg: mczm * wwhh
lssr: jthc * dbrt
gcwt: 3
jzbm: dghp * tscd
ltft: gwtl - cmzt
bzcd: stnh * mzhm
nfpn: gjhd * jztm
mlnn: 2
fqft: 8
gfpp: 8
flmd: sfwf * smjz
zcvh: 3
bmnn: grqv + rmcv
qnsj: scmj * mppn
tbjg: 4
njdw: mgjp + mjpf
vccs: lnbd + lvjf
zdfz: 3
pbhn: 17
fmjd: 10
mjcn: vrvs * qvlq
zwqv: zqvd * jzln
bhfj: 4
mjgm: rfmd - nqmg
rnrm: 2
brzn: 2
hjnl: 5
dzhp: wzhv - qjcn
vjbn: fstb + rjmh
vlst: qnlg + fjfv
dmzf: mmzm * tnnr
qwvn: 3
mclw: 2
dhtf: 2
wrgb: zvpl + lltr
ssvs: zjrg + tbsd
rcwr: gvwh * nchp
cpcd: 3
prfm: 4
vhhz: gmpz * clws
gtzp: 8
fbwc: 7
dctr: 3
tgqm: 7
qmtr: mjzm + qpvf
qbjd: 2
ngtq: rprp - cmwp
zrtf: 2
ssbq: 2
dpvw: 15
rbgz: wtbg + mrfv
svvz: 2
ccvp: 4
fmbs: hglh * qzwb
ljtq: 3
cbwc: 4
srsg: tqqv * zcwq
zqjl: lzpw + zbwc
zdhv: flmd + mmgp
npbs: 10
mhnh: 2
tscd: nsln * hzrz
pbhd: 4
ldrw: btrt / wpmm
zlbn: dtvr + hgsr
pwjc: rgfm * rfpp
rvtm: 2
zpqr: dhtf + wfbv
glqm: zpqr / fqwr
hlcj: 4
wzvg: jmgz / zqtb
cjpm: ndpt * wqfv
pvcw: fsbz * tzlt
mnwm: dvpw * zhhm
clws: ptvc * lhrm
zvgj: svzm * hrmm
fvsc: 13
fmzw: zjnr * csrz
dzrf: jtnc * hqsp
zlwh: 3
pwmd: 2
flft: shzs * bjnm
tqfv: ptvl * jfld
bgtg: zmgl * hqnl
qlhd: ldzp * cnnz
zwwq: 1
jjpm: 14
wzhv: tpgr + pttl
vlgf: tssl * lmvt
gnfg: cggn * pmpn
sffq: 8
fbqz: zqdc + nbjm
vhng: 13
zzwt: 2
qzgd: zlsq * frjt
gzmq: vzhw + qwqr
fvrq: 19
gctq: nrch * ctgl
rdzh: jthv * shsv
mqbv: jdgt - wbrs
vmbr: fvsc * cqgf
fppt: 10
pzzm: nwnh * fsgd
lchq: 4
fbws: 1
qfpd: 8
srzw: 11
cwsc: rjzw + hszg
nfwb: lnvg - zwmh
nwrd: 2
jrjs: 2
gjvn: fvcc * lfcz
tmzr: pbqh * fzvm
cbdp: wzvg * msdv
zlgw: qwhh * jcjq
nvnh: 14
rrbn: 3
pjlf: jmmr * mbqp
qngd: 5
nmhz: pncc + drpt
bljd: 5
fqlc: nzpg + qvpm
whhj: bzjj + qfms
hfvl: 11
pnbv: cnjr + hlnh
bgrg: lssr / fvfj
vcss: 2
gnvg: 1
vgts: 1
bpjh: 3
dhht: vdds + tlbr
whdm: 5
tjcz: 7
gjvc: 2
vflg: 3
dtwp: nvgq + pjzf
gwtl: hbph + ngtq
zwds: djjg / wwwt
bfsf: 11
gvwq: 3
rdgj: 5
pprw: vzlr * stbf
gmzl: 20
scmn: 2
tncz: vqhz + nfcq
sfsl: 5
hmhn: 3
zvfv: hltv - pjdr
phdn: zlts * rjpw
nrhb: ddjw * tjdh
nqmg: 6
nsjn: bdsr + vmbr
bnmd: chfc + phnv
djsm: 7
lztt: dnlg * mmtb
qjgt: rdzh * rcss
dbhl: 20
zzlq: 2
btrj: 7
prdm: mhbb * vrzv
wjwl: zspq + cmrt
pwtr: 2
tsnb: zwqv - ghwp
rwtt: 5
nzvn: qqnq + gzsp
ffwm: 3
lnwn: 2
nnws: 3
bpqn: 3
cbph: pvcw - qpwh
mgfs: wcvv * dnsj
tbrq: spcc * rjmz
jgls: 3
pllq: lbpv + dhgh
rnls: msvh * cchj
qfht: 9
dwsq: mtzt + mjcn
hltv: jqtj + dbrq
mqpr: rsbb * tbrq
tpwt: 2
fqbr: 5
dsnd: dwsq / tpww
hjdv: hdcw / dpst
rtnm: 3
tqqv: jzbm - gmzl
lgfn: hbjl * qjhj
wjqd: 11
vpvv: 5
btcn: rnqm + svwm
hwbc: qfmj * szcb
vrbp: 2
rldv: 4
jznm: fflq * nlvv
rzsf: ndps * vsjp
crss: 2
vsmj: bvrr - mmrf
bwbm: sqtr + vttq
ptjz: bnqb + vzfh
qqfq: 3
jrmg: 5
chld: 2
cchj: 7
jcws: lwqq / jwdq
nzpg: tmrn * clzb
jcjq: 7
hppn: 16
ngpp: ngtf + zdhv
jstz: bbcc + bdww
htnm: mzmm * ssdb
drhd: jrpn * rhgt
jncv: 4
pbqh: vnwg + trgv
fdsj: swnc / zlwh
pqgn: rcdg + tgqm
qfms: bwbm + bqhf
jthv: jwzn * mvwr
ldcd: 13
hcfm: pzdm * vrpw
tmvc: dqjb * fwpn
qpdb: dbrv * cmbj
dwqf: 2
lcvr: ssqs * nmcr
blww: hcgp * nznl
ghcl: rphf * ldzq
dhgh: cftz * jpjc
zzfj: wnvb * svvz
ptmg: 3
dvbb: qwgc * dzhp
wjvz: crvz * mgrb
dhpt: 17
jsqn: 4
phdb: 10
zzlw: 1
llcd: ztjw * rnlc
crld: sdsg * fpdc
jfnt: rqlv + hlqg
dbsp: rzlh + jsqn
wzdj: 5
szcs: bglw * cnsh
wwqm: bbdm * tlwp
dnrs: 5
mdgb: 6
mmzm: ggzj + gwww
cphp: 5
wbrs: jqmv + pzdl
qvnp: 2
wpqr: 15
ccmz: wncw * nzpn
frtq: 5
dpqn: 2
grnb: 3
brjj: lfjp * clfq
hjbn: ndpn * qwvn
msfq: gctq + blgq
wtpm: 2
gbsw: 3
mfvr: llcq + slgm
jcmg: cwhp + fjnj
tfzl: 19
spcz: 9
cqpp: tpzb * sjld
qqhb: 2
nhst: cjpm - gghd
ztjw: 2
wwsn: 4
dfcc: mwnz * pnbt
zjsh: 5
ppfp: 2
rcss: qbqs * fqtd
dcmv: 9
njfv: tfmw + zbdh
bvqq: bwhh * nlhz
jswt: 5
jpzc: 4
zltq: 1
pshd: lqlw - mdgb
sgnm: 2
gbbq: 5
zmgl: 5
ddll: 2
vstm: 14
tjdh: hvbp * hfmn
pgfv: 3
pdrt: ltvh / pnzl
vpvf: 2
jbdd: 2
zwqn: ldnq - hcvv
sgwj: vmhg - dwpl
wjdd: 3
qwdv: 2
zbdn: qqfq * llcd
cclh: nntn * vzgp
cwlg: lmcq * pnbm
bpwc: wgqm + rhlb
jzpf: lbcq * dppz
fstb: 3
mczm: 2
mttr: vhgq * qljl
mmsw: 2
wqtt: ndmc * jngv
mbdz: 8
mdgh: 8
zhrc: phdb * pwnl
wjlw: dwhf + dtns
pbvr: ldrb * dnvq
gdvb: rcns * pfjs
ptvl: 2
wqtw: 4
zjnr: 3
nqnn: fcvf * gbdg
vhvp: bgnn + jcsh
rqtc: 6
wzcw: ldfp * jjbt
ssgw: 2
jhbf: 4
ndmc: 7
pvvz: 2
zhmn: dfcc + tmvl
nswf: fjms - wsmp
mtjr: gdvg - qbsm
zgbb: 3
vpqm: jqqw + bwnj
pqfg: 2
bwcz: 5
prht: 4
qtrs: 5
rslz: 3
njls: tmmr * sctw
tbqc: qtnb + twjg
ntbv: 1
dpvt: 6
shhr: wncg * scgw
nmfc: 2
wmdt: 16
hgqf: mgsh / pbff
hnjc: 2
hsgn: 4
hgwl: vgsr + ttzb
qmvr: 2
gcvh: 3
fhpp: 3
jwsj: 2
mjjf: cjsd / bvmw
vgcg: lgcw + jtfj
tthn: jcws + qdsg
tfqj: 5
mrjs: 3
dcsb: 2
prnv: 3
dsqj: tsdf + wphl
npst: 12
gglj: 2
htlq: 5
sjjl: 20
pnzq: tfnn * scpz
ztwq: gtjp + wzfg
zvbt: 3
hrnz: 5
bggc: sfsl + dpvt
ssvq: 9
jldh: hcqj * cqnp
slmj: qvbl + npst
dqgq: 17
zthw: 2
wnfn: jthn + lrsg
nwpb: mmjw / dgll
lpjr: whhj + tddn
bpnb: ngsm - wrgb
cdvw: lpjr * dmnw
njgs: fpgc + ndff
grrr: tfts * ljgz
tmvl: ljvj * svgf
nfmp: 3
qchv: jbwv + mccg
zjwz: qvhf * ghsz
gvwl: cqpp + wltv
mhvg: qnrt + ndjs
gvld: 2
gtwm: mdfq * qdfb
wsgm: fddr * cqqs
vnws: lhbs + thnm
mvwj: 2
dgzv: dbsp * bfhf
tlzg: zpnf * pwmd
brcq: 5
ptmf: dwgb * wngv
tbvd: mcbz * wmwn
cqgf: ctlv * fppj
vwjh: mmgs * rwdr
qjnr: pzdz * wjpv
cwhp: zqmp * zlwg
fjtm: bmnn / ptqz
dgls: wpvc - mgtj
ltfj: 7
bzfd: 3
gzrg: 2
hpnn: tzfp * nhsd
hwcq: 2
tbth: 7
jsqg: 3
qcql: lqvb * mrjs
djgc: 2
chbz: 3
jwmg: 2
wdfp: 5
qvdd: ggdj + dmvg
mlwd: rvmp * rvss
dmnw: 3
gdcr: 4
pcvc: 9
frjt: 3
shdm: 5
zcnh: 3
wlhm: 3
nnds: crwm + nwpb
btjz: rdvt * pbvr
ptvc: 2
hhrr: 2
tbhz: 16
jdfc: bwpv * ncgt
pwnl: qnsp + tqdf
rlbl: wpcs * jqtg
gzgp: 2
mzhm: 4
hdpf: lfdd * dbrj
qvds: 5
tdqv: 5
pbnc: flft - dgwl
mdfq: qvnp * wdms
lqvb: 3
nlhz: zbtz + mvnl
vvlc: 2
vpmd: 11
glpb: 7
vrzv: 2
ppcg: bjhf * mrmn
gprr: 2
cddq: fqms * stcs
lswz: rbhb + rstc
bfcn: splb + cnhh
mrmc: 3
crvz: vnww + ztzz
wqfv: vhcc + vsbz
frzw: 7
plft: 2
svzm: dsfh * qhgn
lcqf: lfqr + nwmw
mzmr: 10
nhtg: bnmd / zgbb
vszc: qzgd - gjvn
zfdl: 6
hjrd: ldsg + cnrn
mtzp: qzrv + tslf
wsmb: rmpc * lgdd
lhzr: 5
szgj: 2
qvbl: 1
dwrj: twqp * ncrs
fzlc: tscz * wjrm
vrqz: 6
rfmd: hwgg + brmm
mslj: lfhs + nrst
dzdf: vstl * bgrg
jchz: 2
dgwl: mbrc + jshl
jdnv: 2
wfbn: 4
dbrj: 5
tqpv: fzbj * vtdn
bvrr: ffwm * gtzz
svwm: 6
tddq: vvfq * tbjg
jsjd: wjlw * fqrr
clpf: 5
vbsd: hjwt / cgfp
pszc: swmc + vqsz
jqts: 6
tssl: htvm + vjmf
jrpn: 5
qftr: 2
zgvh: dctr * cjbz
vzfh: sdwq + rgnv
jvzc: jqhd * gwgn
hfcs: 2
hhvd: btbr * jjdn
qdfb: 3
dhvd: cphp * crld
rwbw: 13
nggd: 3
cvpf: chvp * hflv
ctgl: 2
tvhs: 4
gmpz: 4
gjnm: frzw * qvgz
qfwr: 2
nwft: 5
jszc: srsg + ffdv
tdlf: 5
qnwt: ddjh - dsqj
wzvl: dvfp + msvj
djfb: wnfr - bbmz
ltcm: 2
ddqm: 10
zppb: 12
hflv: 17
vzmq: scmn * ddns
scpz: 3
nmpj: nhtg * vcss
vtff: qszg / ztvq
dnrb: 3
mrlh: 2
stcj: 5
lmcr: 17
sbhb: 1
zrvl: 3
rctr: 17
cgjf: vgfd / fnzr
hlnh: hwvn + wfbn
hrzl: 10
lfsd: 2
hrcv: 20
rhqb: 2
qrhw: 12
lmqf: 2
gfbc: qngd * rrmg
hlgt: 2
phjw: cdvw * vljq
rrws: 1
gghd: jrgw * fmql
frtl: 10
rcdg: 12
fjvf: crzd + lddf
ggdj: wlgc * ljlw
fmvt: 2
pnmj: 3
rcns: qfwr * rvrj
zqmp: 3
bsmz: 2
rjzw: lgjm * vhng
jdvv: hrtr * pnrp
mbtd: nlpl + wtnp
qjqs: 2
tlfd: 4
hvlb: 3
ntsp: hjbn * mplg
tlbr: 3
flld: 5
twcq: 5
ggtc: pqqz * zcpn
tscz: 3
zhzl: 2
shzs: 10
mrwm: 4
zlts: 14
lwjz: 4
lqvp: 9
lgqq: 2
gjhd: 3
vqhz: mbdz * hrnz
vqjf: jftm * vfsw
dwpl: 5
flnb: rjff + mjmc
cnzm: hrgh * hfhn
spzc: czsf * zvsm
hzbh: 5
ljlw: qtdr * zcwc
vmpw: 5
cwmm: tczg * gjnm
nbjm: zsmn * jbmg
dbmt: vjtq * vbfg
wdtp: bwcz * btbn
tjnh: fnqw + vstm
phrq: 13
ncjl: 7
pcdv: fftf - ddqm
ftrr: 3
hrvl: 2
cqnp: tdlf + hcrj
nmcr: 3
zmzt: sbhb + vjnd
srfg: 5
htvm: 18
dnvd: zmfh * nqwb
wfqq: prlb * nfpn
smmb: gtzp * hqmp
ftnh: ddst + ppvw
wlth: 5
psmd: 4
nchp: 3
splb: ddsl - lzpm
flhq: nqnn * tfhp
snmh: ccvp * plft
zzmg: dwzg + grml
lfqr: zvjs + dwnf
mwcc: 5
ldrb: 3
zbfl: 2
wjpv: 4
hhqv: rgpp / qdnm
wdwj: nldc / nwrd
bncz: 3
gjws: 12
gvtw: zpwf - jhwt
wlsr: wdtp * tglj
dfjd: 3
pjqj: 20
qcdj: jbqm * hblv
wjlz: 16
njdb: tddg - glwg
qwqr: vgsn * vvmv
ztvq: 3
gpgm: 2
tddn: hpsd * qqhj
bfvc: 2
dnng: 2
rjpw: hlgt * jlsn
trdt: qclt + qzzs
mljh: gbph * mwqn
mjst: njcd + lcmg
dvpw: 3
lgjm: 2
ncvh: vhhz + lzlg
vmjm: brtb + mbgb
hfhn: ssvs + ddcb
wltv: wwlv * hfvw
hcnw: 7
lctq: 5
jhfp: gjws + bmsg
jzjb: 2
dbrt: 2
jngv: lgnh + wsgm
gnfl: hvfd - lrlp
qdcs: 4
zpnf: 3
fsjv: 2
bvpg: 3
zhbj: 3
nwlt: chtn + sdfs
pqqz: 5
qwws: rpwc + pdzc
lbpv: zqwh + fssb
cfrc: lljs * ndlp
gzrc: 2
gvgb: 1
hzrz: 3
jltf: blcm + lptn
jhqr: 3
lbsd: qmzb / clpf
zqnj: 18
ftws: 19
zvjs: fpjl + jptg
fvml: vqhs + lvpq
fzbj: 2
gtjp: 1
njcd: fqft + lqgq
tmmz: nnds * qtwf
pnbm: 4
hwjm: bwmp * tbcf
wphl: mzmr + qdjf
hlhh: 2
dgvf: 12
dfzs: hqqq + ssgn
hlbq: tvhs * vccs
vbng: spqh * pwvm
pbfj: wbwv + mzfm
bfhf: cnnw + plmd
zbbv: 12
zczp: 17
wwhh: rlbl + fsbf
gbtc: hlwv + hlwz
tpsm: 2
pdbt: pjlf + srhs
jqtg: 2
fbcb: nfmp * tphz
vvfq: qhnc + jldh
spct: 8
nhqw: jqqq / bsmz
pvps: 2
tggg: 12
rjrf: htbc + frdt
mzbz: 6
dfbh: 3
hsjh: lzfr / lqrj
wqsg: hpzf * zlph
rgdw: ntwd + pvps
bqcz: 5
gdmt: btml - rslm
ndpt: 2
mppn: 19
shsv: 7
gswq: 1
rjzv: 5
zhdj: jhrh * zhzc
grml: pqfd + fdnr
vqjn: 10
wdnj: sgcw + cgcn
dsdj: mbsv + mjjf
ssnl: 11
mddj: 5
rmjp: vpvv * ppfp
rvdz: 7
vjmb: 2
ljts: hpfc * hsjh
lmqm: 1
bhfn: dvct * fbcb
ftzh: vqjn * crww
hwgg: 2
cqqs: 3
hjgj: 2
jztm: 13
ghbc: 6
wncg: 3
rjmz: 2
htbv: 11
ndnp: 5
rfzz: 3
wfgc: dpqn + tlpz
dvcz: 3
qwmt: rrbn * zthb
hwcm: 4
mptj: zfdf * rptg
tbcf: hbvn + zhvq
sbqt: vfnm * pdjp
tphz: 3
pnbt: bszg + gnmt
wnvb: gpfh + cmbf
qbqs: hnfp + wjqd
vshl: rbvb + pjvn
jrpc: nrqq + hblr
zcpn: 5
fnzr: cvnq + tfcs
vmfl: ctlr + qjjd
dhhf: 5
ndhf: cvpw / plrw
zvcw: 6
fjms: vsmj / lhzr
bhtd: fnpj * dptd
vfnm: 14
hvfd: hpdp + mgpj
twcs: tdrv * hvls
tmlc: 3
dsll: hgwl * vncm
vcmt: vjcb * snbr
bjnf: srgf * ftts
scsh: 13
qrpr: dbmt + zbbv
llvf: 13
dfpr: 7
gvgd: 1
lqpl: 4
ngdf: nbrv * wwwc
hbtv: 2
lfrj: 2
mbrc: tbzv - ptmf
bhnw: qqbg + vwmm
gcfc: 7
bmfr: wflc * gzgr
wbrc: lnwn * cjzn
dgll: 2
ddsl: 17
vzgp: 5
cwmp: 4
ddns: rrph + zchz
znfh: fgsd * hcss
mvnl: 4
mwjn: 2
vwds: mpcm + blww
brtb: 7
zwls: 7
hhpm: 3
gtmz: 5
pgcb: qdpl * dnrb
tcrn: qwmt * lchq
qzhb: frtq * drdc
prcm: wjwl / czhc
mtzt: fjvj * gjfs
fdqz: brwh + chjr
plrw: 2
gqhb: mpgn * rvjs
qtjc: 18
hrtr: 4
mwgz: 17
snbr: 2
dnsj: 3
rrcs: qccw * ptmd
rnds: 5
nbdr: smmb / vjnm
gczz: wjwd * jwsj
hqmg: 17
zzdv: nnjz * sfzn
fhph: 3
qwgc: 2
dvhl: bpjh * rrpl
rpwc: lqgf + stbv
gntr: 2
wwwt: 5
jdcc: 1
bmsg: 1
blqg: vshl + dwrj
vssd: nsmp * wgfd
dfrr: zwqn / wwld
vpqs: rgjv * hpcn
wsns: 7
thwh: prcm - spqb
ndzs: qwhg + pqwf
jfjm: 3
hjdd: 2
wwld: 6
tgzr: ljtq + lvwj
hvls: 4
mdzm: 3
fmjw: dphm * wmzn
lbrm: dplt + ndvz
vzlr: 3
tlch: ljbd - fndj
vcmg: cbdp + dvnp
ncjj: lfrj * fbgz
ssgn: fpvg * qdcs
hbdh: sfqb * btcn
stcs: mdwj + shhr
mqzv: wzbf * rslz
sjlw: 3
smzb: zwnh + wmdt
gpch: gwdq + zlgw
lglv: 2
wflc: tdch + zwds
lpnz: 14
svgf: 11
thpp: pglz + hcrm
ncsb: ljlz + jmdn
tstt: 4
cpcs: bbjt * hcwt
pwhq: rqbs + nmzd
tglj: jrjs * pjjr
tlpg: zdfz * nmrr
jjjt: 16
gfhl: tdqv + cvpf
ntzw: 2
hcss: 3
wlzg: 3
zwnh: 7
rrph: sqqt / brzn
vstl: mrlh + dhhf
bbdm: 2
vdds: hwbc / jgjd
tppt: 5
ljnn: nczc + fvml
nfcq: srfg * pvhj
qnsp: 2
drlq: 2
qszg: vgcz + hwfd
fzvm: 2
rqhj: ptmg * wcrr
vnch: mbtd * htlq
lzpm: 4
jptg: rwch * bhfj
hdtm: 4
jcjv: rhhp * cpcd
wncw: nsvt + vwwf
mgtj: 2
wpjd: pszc * dhpr
twjg: 11
gjfs: 14
hnfp: ldcd * wqns
jmdr: scwc * wwsn
lbng: hjnl + rzsf
zprs: bjbz + nwft
plmd: zzwt * gvwl
mmgv: hhzv + lpnz
ppwp: jhbf * qgjz
zjrg: nbdr * tllp
nrpb: fdbz * bmfs
vnft: 14
nbjv: 6
lpcb: hjdv * mlgf
bbnn: 3
fjnj: 2
fmmj: 6
zthb: 5
lqpm: 3
lhcn: 4
rnlc: 5
sjld: 7
ztzz: 1
bcvh: 3
lrlp: rqhj * bpct
jjdn: 13
tdrs: 2
thqn: ffsg + fbqz
tvwz: 3
ltvh: 12
vwwf: 4
mrmn: 2
cnnz: 2
ffsc: 4
mgrb: 2
mcbz: 2
gwdq: djgc * gbfm
rrgm: zwls + snmh
dtmn: 6
tpzb: 3
mpcm: sfcf * jpms
dnpd: 2
dqgt: tlsg * pdtt
tnjc: bvlv + tbqc
qvmf: ncsb + mgmb
jppv: fmjd + fmzw
lptn: lrhw * rbgz
cjsd: cjrd + ngjn
clfq: 3
jtbh: dzjc * mnms
dbht: pdbt + fcjn
vtlz: mtpf + ccjz
csjz: jqhz * qmvr
nqfw: 5
wtnt: qwph * dvbb
rvnn: 3
nfvw: 2
zwmh: 5
hqqp: nzmv / rwlz
wcwl: 4
dhtg: nqvq * blsh
chht: mqzh * jmnq
gdcz: vwgj - cqlp
grtl: 3
dzvt: sjjl + vvlc
pbgc: 3
bwjq: qjqs * bncz
jhwt: 6
dfmg: gcpq + jstz
rrpl: bgtp / tnqc
cppm: 3
qlwz: 5
pccw: 4
qpls: 2
dcfb: rjfs * rllj
llqz: bljd * ssnl
hvqw: nwcn * ldsz
dwfs: 5
qzwb: 12
mtzq: 3
gqpt: vzfc + tbpt
qtwf: 3
ngjn: qzlq + tghv
htwg: 2
zrdq: nvnh * lrvl
djjg: ptfh * hmgd
dzjc: 3
djgj: 6
mglc: 5
fpgc: nfhv * cwlg
brmm: dvhl / qhdp
cnsh: 2
lqzn: ccbp * swnz
gwgn: vdps + phgf
msnl: vwds / hfcs
chpw: 5
sgpg: 10
lhrm: lwjz + fvrq
mftq: 2
tslf: hhvd * ddfm
wncd: bpns + wqtt
nwmw: bpnb * mzpf
jmgz: rdgt * cfwv
gbfc: 7
vjtq: 4
lsft: tncz - gpzt
gpmn: jszb * brcq
nczc: 5
dnvq: 2
fcvf: 2
glhl: 1
qgqp: tstv + mlhh
vmqz: 3
tlwp: 11
ddst: 5
gjqh: 2
nmdl: 3
qrhv: przl * gbbq
lvwj: 16
clnz: lsft * wqsg
zfbf: fqtt / jppn
rwfc: 2
jbmg: nlsz / mlnn
psbw: 7
ljql: 13
cvmv: jffp * szgj
bwnj: mqzv + cvmv
wwlv: 2
qglp: 1
qjhj: 2
jzps: 2
ffsg: tqlc - fjhp
qjcn: tlch + qrcn
fjhp: glzn * cmms
rlpn: hnmz - qtfs
szcb: cqfh + gnfr
zqwg: gnfg * lqqg
lrpn: 2
sqqt: lvlm * trdt
bvmw: 2
zpvw: 5
rwlz: 2
schl: gcwt + nrcl
drpt: lhzq * qmtr
bqsb: dnfc - vlst
jdfz: 5
nlvv: 4
rjmh: lctq * lfqf
dwlz: cwmm + nwhj
dvct: 3
tcbz: rjvr / prjh
tcfq: 4
qvcb: hwls / hpcs
mwhs: 16
gznh: 5
swnz: 3
thcn: srrv * jdnv
tmbg: 2
ljsb: 16
qnnz: ldmt * hhrr
qdfm: mwhs * bfvc
vgfd: qsqw * nhtr
cvcc: mzrm * lmbd
hzjv: mcdz * prnv
zhfp: vrpd * wdnj
mlgf: 14
nmzd: rgbh * bpqn
cmwp: wfjz * gjqh
tfhp: 3
root: zhfp + hghd
vtnb: nrwj + rhwv
ltpp: vcgw * hqdl
wbhc: zgtr + scrb
wzzh: 8
ccpw: mhsd * zmzt
mtgn: 16
drgf: 13
rnwm: 16
hfhc: nwvr * zjsh
tfts: 4
tjjs: mcqw + fsqs
glfz: 2
ldzq: zzgp + nbjv
cdgs: bldp + dtwp
zlhb: 4
wclf: dcmv * gdcr
hszg: fcwq + htzb
cwzd: 2
jbgd: 5
jbvr: 13
vtdn: 7
dppz: 2
ldsg: gqpt + njgs
tfrr: vpth * fmmj
vvmr: 4
ztjs: cvcc - gtnp
jszb: 5
tbpt: srhg + tblr
fpvg: 2
fdbd: 12
ljlz: 19
lnbd: lntr + ptrh
twqp: zqnj + rqsh
mhbb: hlnl * vbsd
nzsq: 1
rdvt: 2
ppvw: 7
ddjw: hlbq - vwjh
wgrt: vdmp + lttb
mvzw: plvm * qfht
fszn: 7
mchv: 5
bwmp: 2
drft: 4
bgqp: 7
trgv: tbvp - qzmc
nwqw: vtlz * qchv
ntwd: llqz / rdgj
jfld: 7
tblr: tlrl * rwbw
dmvg: bqsb / jbdd
nqwb: 3
tnnr: 2
hzcg: wmwz * nnwg
fcjn: 12
lcmg: 8
cczl: qrpr + jgfg
rgfm: vqrn + dzrf
fpdc: 7
pqdc: 5
rdml: 1
nttj: 3
qszr: 7
qmzb: qvzl * bgqp
pwsb: 2
lzdj: 19
bldp: dvss * jhfp
ljvj: rwtt + prvm
vgsn: tcrn - ftws
ngtf: 10
wzbf: 2
pvhj: 2
fvdm: 14
mmjw: gvtw * dlpb
jlzw: 2
qhnc: zczp * gzrc
thvj: 4
mgjp: 1
qgnb: 3
nmrr: 3
bqht: pvvz * fppf
fqtd: lcqs + jllt
nznl: nslr + qlpn
qlpn: 2
rgjv: sqzv + hbdp
mcqw: 6
nnvb: ltfj * hcvh
sdfs: 10
mdmt: 2
zhrs: jrcb * ndzs
rgpc: qvql * dnng
jllt: 7
pzdm: gtwm / mrhp
pzdz: ztwq + qglg
czhc: 7
jffp: 17
mbqh: vtzz / zvzw
hfmn: 2
srlt: 2
cmgv: lrwv + zgsr
wdms: 7
rvrj: 11
lczw: ftrr * gbfc
ncvt: sgpg + rrcs
vttq: 6
hcdc: 2
vzbv: lfqp * qtgr
wgqm: fdpp + dgls
fnqw: 3
lfhs: gpch * hpbj
wfqw: spww - mlqm
hqvl: cddq / qwvp
fppf: jtbh + dqgt
rjff: pdvb * fnrn
bsvl: 10
mtml: 3
hrgh: 7
ptfh: sgws / bgwg
ndjs: drgf + pbhd
gvrm: 4
btsl: 4
zqdc: rbhz * nnph
fpjl: wtlp + dfjd
cnqb: 2
hsjv: hndr + jrtn
nqmm: qgnb + wzvl
fzzd: rchm * lswh
qlmp: qtjc + dfnv
nrzl: drhd * bcvc
cfmn: lsbv / hlhh
mtrw: 5
rzlh: lzbf * jfzc
gplc: vgcg + zvtn
qvlz: mjgm + ghbc
gnfr: 1
spqh: 5
csrz: jfjm + lqpl
rwch: wtpm * dbgl
hmsc: vmfl * cfgp
rwdh: zpmq * mqfb
vjnm: ppvj * ltcm
lmlt: cwmp * cnqb
ccjz: vqmg + pllq
mqfb: wfqw + hhpm
vsjp: 3
lntr: 2
zwcl: 17
rpqc: hfvl * mbqh
fcwq: hwwm * lfdm
bttg: rlpn + ctvz
lqrj: 2
djqc: 5
nrst: bppf * hcnw
wfbv: dshb + ngpp
svrv: 2
zgtr: 5
rzbs: bgwp * pwhq
jzln: 3
jnwm: 1
lqgf: psmd * pqgn
zjlh: 2
lfqp: 3
vbbs: mtzq * rfrs
smbf: lbrm * dbfs
jcsh: 11
sdlv: 5
lwjh: fwnf + jfqs
tdlm: 19
mzfm: tsjf * cwcv
cfmj: wdng * ngsf
gtzz: hhvv + ldrw
phgf: 2
ldtq: 5
wfqb: scsh - mtrj
jpmr: 2
dvhc: hvlb * bdlr
rwjl: ncjl - qtzz
vsrz: 2
ctlv: 3
zdsb: 1
ctvm: 8
lswh: frtg * mdgh
hpbj: vhvp - jbfp
jbqm: 2
bbjh: 4
vdps: 7
zqwh: njdw + vqsp
drrb: phlw + jjrr
mtrj: 2
qdnm: 2
fsbf: dtmn + qzhb
fvcc: 11
jstj: mdrm + zqwg
hrwm: thcn + mnwm
srhs: rdml + fmjw
bzjj: vmqz * wqqh
jwhp: vgts + bwwz
zzgp: 5
lfjp: 3
bpll: djlv * fzmp
qbsm: 2
qqwz: lgpw - jjzc
hqmp: dqgq - qwlr
lfgf: 3
tjzh: 2
wqsn: zdcw * vmjm
nhfw: pwtr * dfzs
zrwd: 3
pjvn: nqpj + twcs
ntnq: 7
qngl: tlpg + rfbv
jmnq: zfbf + nrzl
jjsp: 2
jpjc: tthn - zvrs
msqr: nzjg * zrvl
fshf: 2
jqhh: wlsr + vjvh
ctwp: 2
nrvs: 2
cglc: 3
zsjb: 5
pbrt: fmbs + cpcs
zmfh: mqbv + dhht
glgt: hhqf + njnt
pwvm: hwvg + ncjj
vjcb: 3
vjmf: tcfq * lnbv
wgrs: 2
vdbd: 2
gtfc: tjwc + qcdj
htjn: ltft * tllg
hqdl: swvg - mcsc
rvss: 16
lqgq: 15
bccm: czgc - gvgd
bwsq: rwdh - cfrc
vrpd: 8
jjbs: 4
gslb: fbws + rnwm
vshr: 2
mjzm: gzmq * tlfd
grfl: 3
jqhc: 3
zvzw: 2
prdt: glhl + hqvl
rslr: hsjv * tdlm
rldn: vzjm * jgls
vwmp: brns + lczw
wjwc: 2
rgnv: 3
gggz: 6
bgzj: 5
qfmj: qmql + jpmr
hfrz: 13
jjcq: 15
dbgl: 5
gmnc: 7
rgfh: lrpn * htdr
gtrl: 17
fqms: 4
lvlm: 2
hqjf: tqfv * jjpm
jdfv: gpff * tstt
nsrm: 2
dphm: 3
fdbz: 3
stnh: hnfd * fjrq
nnph: 13
lmcq: 8
zfcc: 20
tdrv: 7
ngml: 2
lzfr: cwzd * fmwb
ghsz: zzvb * mbts
svjq: mjst * hnmn
tnrg: 6
hvpg: qdfs + fvcn
dbqh: 2
mmgp: 2
qsfc: mzgg + sjqq
hhqf: dnhd + jbth
vfbf: thlv - msff
qhrs: nhst / zhfg
brfg: tqpw * fhpw
tpgr: zvbt * dtpf
jjbt: 2
dqbp: vjwh / jjsp
scgw: 5
phzt: gbsw * vrbp
mwdw: 2
ptls: 12
jrcb: 2
bgnn: htbv * fshf
wnnf: bcpv - zqcf
vnsp: qrhw + gzbc
gbhr: nrld * blmh
jfzc: 3
mplg: vpqm + tcfl
tppn: 2
jtbp: nmhz - bsqc
srcq: 3
pttl: rfzz * dnvd
jttb: zqvt * pcvc
fnrn: 6
vhpz: 7
npgp: nhqr * rwfc
cnhh: 2
nlpl: 1
wjmt: vflg * hmsc
brng: 3
mbts: lddp + nzsq
qljl: vzbv + mbjt
rhgt: mdwp * vpvf
fwpn: 2
mdwp: 3
rvmp: 2
zqtb: 3
ncrs: 2
mmrf: dmzf + rpqc
zspq: jzpf * tpwt
dsfh: 3
mpgw: 5
btrt: tbvd - prlg
jbfp: lmlt + mvwj
hgsr: 3
rllj: 2
wqgg: hrqs + rpgq
nrcl: slmj + gvgp
hpsd: 3
qqwf: ncvt * bpwc
tlsg: 5
hfcg: frpb * jstj
wmwz: jdfc + tmsb
bglw: mptj + hhtm
tdvc: tjvl * gglj
tcfl: wlnb * fbnl
njnt: sqrh + cjjr
fjvj: ldtq + rvtm
jqqw: hnzz * gplr
lmvt: zqjl + wjmt
cggn: 3
gvgp: 11
gpff: 3
jngf: mnfg + cfmg
jrgw: 4
qzmc: zhrh + tdcr
dghz: 4
zhzb: fzlc + btrj
mrhp: 7
jthc: dhbb + zwwq
jgjd: 4
cgcn: fbmv + lcvr
nnjb: 2
ttsv: 13
gdvg: 10
mmgs: 3
hbml: 4
jppn: 4
spzt: mswg * qqhb
gbph: 5
cfgt: gfdw - bfsf
hwvg: dcpd * hqfv
bwhh: 5
lmgz: shdm * vdvd
zhfg: 4
jsbq: 2
hdvc: dghz * wbrc
vmgn: 5
ddjh: jqmz + rzbs
vnfc: qftr * wmwq
hddh: zfcc * hjgj
tqlc: crmv * sdlz
lrsg: jctj - fwlf
qqhj: spcz * ssvq
ftts: qvnj / hgvp
hpqd: thpp + hldm
cfwv: dqvm - dgzv
tmtp: 6
rbvd: dzgh * jqhc
bwpv: jcgd + vssd
hzfj: wlch * bjvp
hfgs: 2
rbhb: rvnn * pmcp
gzgr: 3
ljfn: lmcr * pjqj
gmbp: 3
cvnq: 2
ldnq: lcmt * njdb
btbr: gtrl + lwfm
qwvp: 4
zpfh: 3
tbhl: 2
vjmp: ndnp + lbqs
mbmd: 5
hndr: 5
qtzz: 1
pftv: tsnb + mljb
mjpf: gcww * ctwp
srtz: 2
dnlg: nsgc + lwjh
cccn: rdhq * cfgt
vpjw: qvjs / srtz
nrqq: ggtc + tnrg
hrnv: 3
rjhr: 2
fqrr: 4
pdzc: rcwr * vdbd
qvhf: 4
gwlt: 2
tmsb: fvdm * wdwj
jthn: wgwv * wzdj
sfqw: 2
vhzd: pgcb - nrhb
vvmv: mfrl * zbfl
vrvs: 2
tnvf: vzmq * vjmb
rprp: znlm * tvwz
vtzz: fwgr + frtl
sdfm: 3
dghp: 7
qdpl: tdvc / dcsb
hcvv: hcfd * thvj
msdv: ntzz * zpvw
spqb: dsdj * sgnm
svzn: 2
sdlz: csjp * cppm
zsrs: 2
dhpr: 5
mwnz: 5
gpfh: 9
rnwn: ndmn * flld
mqcz: 15
jcgd: 1
pzdl: 4
dprw: wqsn + ljsh
hhtm: mftq * rhqg
trpm: 5
nwvr: 3
blsh: 4
vhcc: qzvd * fdbd
nlsz: dvgv * njfv
vgft: 20
mjzd: qnnz * glhz
ppdj: 5
scrb: mtgn + cnjg
jtnc: 20
rvjs: 3
qnlg: gcld * ddgb
jftm: 2
sfss: ppwp / qwdv
vqsp: gnfl + gntr
mztz: 3
zvpl: qqwz + pjsd
dbrv: 14
nzzq: 3
tfnn: 3
hjmt: 12
nrbv: 2
mqmv: sffq + zqfw
wpmm: 5
wqns: 2
wlnb: 11
fsgd: 3
mbsv: dzvt + wsmb
glhz: csjz + fsvs
pdjp: ngvh - wpfw
lrwv: 9
jrdq: 16
qhgn: 5
gqbq: bsvl - grfl
cwtn: znfh + tnjc
qhdp: 3
pmsr: pzfh + hcdp
gbsl: sglg * gpgm
rbfv: qdcm * sgwj
jbth: msnl * hdtm
rqbs: slbf * mbmg
wjwd: vvmr * wdcn
hbph: 2
zpbn: prdm + tscq
ghwp: 2
swvg: cgnn + mldp
vmhg: 18
hpcs: 2
frpb: 2
jhdc: jdcc + vcbv
pqwf: pbnc / ssbq
qvql: ltpp + prvw
fcvq: 5
gqrj: 4
qmql: lgfn / jjbs
hlvd: 4
sgcw: jtbp / spfg
tqpw: 4
hsrq: npbs + qcql
nljr: dqbp * nttj
mvvj: 2
zdcw: fzzd + jppv
gdgj: 5
zcwq: 5
jrtn: 2
dplt: 16
ccbp: httg + lsgf
tsjf: 6
bgcs: 6
vgls: 19
rsgc: 2
vhhr: pwgf + gggz
btnn: 3
rpgq: 4
dwhf: vhpz * fhph
nqpj: 19
njsw: 5
czgc: hwcm + hvgv
fsvs: jlbt * tpsm
cjjr: 18
ddmt: 3
tntr: 2
bdlr: wpjd + jqhh
zgfb: 2
fnwv: hghw * zrtf
scjj: mlct * ttsv
fflq: 2
nlqt: 4
hpnh: qvmf * bbqf
qzct: 5
tbtc: 3
wfjz: ppjb * ffjf
mzrm: plzr * rwfm
hvbp: 7
fwhp: lfjw * bqcz
wtlp: lmgz + qwws
zgsm: 2
nvql: bbjh + blsf
sqrh: 19
gvwh: 3
mtpf: mdgl - svjq
gjdb: wqmg * pgfv
sqtr: wdfp * mgmr
zfnh: 2
bjbz: chmm * dbqh
hglh: 5
bqcb: jczs + pqfg
bvbt: rlfn * zpbn
jqfj: zfdl * vgls
tbvp: jfnt * dwqf
wnfr: zzfj / zfnh
ctvz: 8
lgsd: vgqb * bzfd
pdtt: pzzm + gzrg
tbsd: fzpt * lbng
lhbs: lccj * jzjb
rdhq: 2
rpnq: 3
jjsd: 2
jwtq: wwqm * pwsb
rgpp: glpb + rrgm
pnwt: 3
frhj: 5
fddr: 14
slwr: szcs + nljr
lmbd: hvqw + rftc
gqpf: ptls + ljpg
srhg: cglc * jmjw
nsgc: ltsn + jbgd
lppw: 4
qvlq: qhrs - hpnh
hgrg: 2
vjvh: bmfr * blqg
dwnf: tmzr / zthw
clzb: 5
pglz: zhdt * gqhb
qdjf: hmhn * mdmt
pdvb: vbgt + bwjq
vqmg: jqcj * fjtm
hnfd: dnrs + vsrz
wqmg: 2
chtn: 1
ccpc: 4
qlwn: mnmq + tgzr
ftjl: 2
fphs: 3
lhzq: ncrd + jqhr
hhvv: zsbm + jltf
mmzw: 15
hhsl: zrdq * zlbn
pmpn: 7
dwlf: sszs * dfpr
mqzh: mtrz * mbmd
ndff: 4
jqhz: 20
dnfc: vnws / ttbq
zdbn: wsdr + zdsb
zqcf: 4
fbmv: 11
fsbz: 2
nnth: fscc * wrst
bgwp: 4
nrpt: 7
hnwb: vbbs * wlth
wcvw: djfb + jrpc
gtpb: wzzh + ddmt
zvsm: 11
hrmm: 3
qtfs: 5
fhmj: 12
tblh: vbng + hhsl
'''
)