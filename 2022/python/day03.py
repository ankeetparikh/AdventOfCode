import fluentpy as _
from collections import *
from itertools import *
from math import *
from functools import *
import string

def solve1(s):
	x = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
		)
	s = 0
	for r in x:
		n = len(r)
		a = r[:n//2]
		b = r[n//2:]
		aa = set(a)
		bb = set(b)
		u = list(aa & bb)[0]
		if u.isupper():
			s += 26 + ord(u) - ord('A') + 1
		else:
			s += ord(u) - ord('a') + 1
	print(s)

def solve2(s):
	x = list(
		_(s)
		.split("\n")
		.filter(lambda y : len(y) > 0)
		._
		)
	s = 0
	for i in range(0, len(x), 3):
		a, b, c = x[i], x[i + 1], x[i + 2]
		u = list(set(a) & set(b) & set(c))[0]
		if u.isupper():
			s += 26 + ord(u) - ord('A') + 1
		else:
			s += ord(u) - ord('a') + 1
	print(s)

def solve(s):
	solve1(s)
	solve2(s)

print("Sample:")
solve(
'''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
)

print("\nActual:")
solve(
'''
BdbzzddChsWrRFbzBrszbhWMLNJHLLLLHZtSLglFNZHLJH
nnfMwqpQTMffHlNNLllHnZSS
cGpcMwfppfqcjcTCBBzWDsDbDrjzWz
LhfjhcdjcGdhFfdGfdjdvwCCZMvvLvWwMLCLSwZC
rDnsbmptPmlbQMCrQWQQBZQW
gltgVPngDPbptPsbPzVgmDldfTdfczThjJJjfMcJdFHjjH
dGlgDflTLLLrRLTLVdQLcQMnbvHbbFzNNvMbnHHn
sZjWJJCSjWqfCqSjSmJSbFvCzBMBBzHncHNvMBHN
twqqwpZwfrlwRwDGDR
zCGGFTQMQrsNRNGZdR
cLLQgPDpgcgmvPRHrwBdvrNZ
glWpmJWQDcJpQnpjSmbhFtMnqFfCVTCFCFFM
zNZWFNZBFrGTdBcZZBdJTrGrmgvppgDHwHmgVHCHCvCPDjzC
qtqqPnLSfLwvjvvgvvqH
MtbLLLQbRfPRfnbnnLMtnsbdBNsrGWNWcNcTBWZrrcrWcJ
sZwstbbDVlHtbhcrhhZLrRpNQN
jqGjjFjWnzWGgqWjJJNphnLMRhLhcrhcrSLN
qCJzFJdvmHvbtpbb
ZSRsvvQvZpsRQGJghClPCwGPChCP
FVdMLDdtDRdDcBtmcVFntwgJJTlnNPwJnlTlwlTPgN
VqttMWFmDbjbzrSWRQ
TsDSBcwshdwSCrgRWZBvgGRG
LPVJLqqJbbzpFqwpbvgGRmZPrmZgCvCCfr
tzJlJzQllFLqtwHhjNSdtthjDhTN
fsDLDDnwvnSdqLSsFSDfsLpbgVttPMpPNjMWVMNfpjgW
jhHmBmlrTBBHRPVtMZbppNPPZB
JmTTrTmjRTJqSQQSFqQw
HPzZFgPFMCHJCcZMcDQGwpLqPLqppwhGvv
BrWRqbqRsTSTqNddrVrthLQVwnpwphnvnDnGvGDn
tSbBfsRbTfqjJqjCqm
pCqrqzmqZzrmCCvCJwJPBRwJBWBmwWBJ
VqbqbjFLFfSHnfctBwDdDFTwtRRTDF
LVcnbjHLSqHnhbSGGppCMMZMphpNrQ
PhTcTPsSPCMvvhhMRPttbNWfNsWFNfWWtpNw
rdQrDbJBVVjrBVdLjHHHWNWwfHtzzNtFpZZptppg
JJVGGdddjDjDJmdjGqqRSbPMTvcRlqnnMlvT
SqGfTrBlSrrrfGGQvCnqZhZmPPhvJh
LdVNwgsjdjHmjWwDsDpwsHWtnCnQQQQNnvCnbJZQbNbtZZ
DjssDHLLVppDssdLspswFLVjzfFMTfSBcTRcrFSBzBTzmGzr
JSJJqlldpJlcdVWMlgMJrcCjrhzHCwTjHrQzwTzZ
bBvsGBGNFDNRFNFBRDPsDDHCChhhrZRQQzhjhCjTzWCr
FvbLFGDDtWDFBnPGFDWGqJMgJpSdVStllttlppVS
clpBdBQBsqGpQbVdqTTWRTSFgLLggffg
NzvwmHvZtZZgbDSCLDmfmm
jPJjthHzNwPvvjwjNzPzztZBlrccpbVGBQhlGBVlrpnpBs
NmFFGlGmzCrNWHvFmFWCFvQPTdDDlbbdgJPtgbbdPDcc
RwfBqLwZqffqnPbdDgVQDdtRbT
hnptqLMMLwqjMMjzSzHmhvNNrvvhhz
hqVrDdPdVDqjsDrjjqsfrrWlctvHJNLfvNcLHNNZRNZHvfZL
CSnWQSGBBSnmBnTmSbQbNZZMJNJMccGNHLZNNvNv
gFnmBmBnTCpwmBbgWVqjPsrsjplVrjlqPr
vgVgJJCphzFjzbwljwww
PWmfDgrPrPWlSWqSWlSZ
rrTHQTGTPHDDHgPrcrcPmDPhdtGvnvNnttJCdJhtGVnpdM
DDDhNgWNLWgDqDgtgtwSngjVSQdf
cvFrcGmBrrrCdSfSJQ
mBHzFFvFzmsBspsFsZqhqbWlWdPDlLHbqZ
TLNpGpRzwGQLLQRTwdvWdWbdbgdBlblb
FJDVzZzHfZHVzcHgnvHnvngvvc
MzDVSmZPPrqhGmCqQqLR
mqHWcBHVcgsbhhnTrrTg
fWftGtfJpwJMSdFDLFSGDGFnnNrbrhTNsZnrhTswZZnnsb
dSftppdSFStLDpQfLjWHQvWBmmqVjCqcVv
frfNzgvzzzJwJqpRcP
VdVSnGnHqhDDTdqhdLWmjMTmjMPjPmTsmsmjmR
BdGLSWtBSWDtVqdSDVGqtSSHFZFZtQbZlZfNgFffrgNrvgrl
jBVSjsJcLcqqjtgcmRFRNFFzFm
CnHnWQQGGWnnCnfvCTmZRZgNtfZtNDZPtNDtzl
mWWGGdmQQWwrHHMBBBhrBVqshBLBSL
cLtFcllvrslGLcLHVzDZQzzpznWzQtQZ
TmShfSSPJRRBBfSgmdfBJhDNVpGzVZpzQgZgbWzpnDGp
BhJPfSqdhqJRdBdPqTJBChvrFlHvvCGCccHsMscvrHvv
zfddZTpZLzLDfLtDCttdTfZPnlcPcnhjPDnlcjMchDPjnP
MQsFvFHJsQvmNvvswljgbPbwlwjnmcch
VFVqvqFQHqVJRVCBLpqTGMzCqtMZ
PZdVgNdQQcdcZQtGhnHtBlvlvWTnbBHWWH
CDJmzqFmMmLfqmzFwqfzfwMRvpRbTWBBWDnlnbnWnTNTnB
zFfffjCqwLJCfrCFjCLCzCMsjSZjQNPhQGVSQQZhsGjGgd
nbHntnqPQwTHwQVC
BzfSZSpcBZpzpPhSBjRTCBWTTRWTTTWR
pvZpzPzNfhddJGmmNnJb
GwTgWlvbgTwMrbwTrlWvwtHBNtNvBhBtdZcShHDtNS
PnndmnCmnJFnsmRdmFnnZDhRRScRQQHDtDNtcDQS
CLffLsmqqpJljVdlpMpWlr
dPCzBLTSLqmqdSCsmrTDVQjZfjfVVZnZhhhLGQ
wwFpgvPJNwgPPwvZGnQhbZQQFfQZbf
WvRwwJpHHgpNMNqdTdCdqrmHBPtm
DbWwjSGFSFfwGfCwDSSPPjLhgrrLWRJRgggJphLzpJLq
lQTnMHdcQBvlHMMZBcHHTrbzpdzgqrpLdqzzVRVRVV
vlvlNlBQvBZTQBnHnQTTBBPwPNCCsfSFmbSFfmGPwFmj
hGGQtbVjhRqlmqqrmDlpmw
gPMZsMgdssCPPsvrgZcTZTPSnnLLnBWDwLmwWwBnmWSnWNWB
TsvgMPdcgCfMdcsZJRQhVfVRVQFFQGtr
NfpFTTpFNbpZMRFrJMMMCv
dWJPngDWBtPVBdPVGHZzCGHZrrvZRSMSzv
WDDDVDPlWnLBVgnsgJmQJNqThNmbjlqbbh
vnznqvfrzzVzrvvnfVqztBtGbMCdGmCcdccJccCLCcpSSgcL
RQsDsljDlhssWshHhlhsHTlLbgJLpmgbbcMSpSSbcSJgjd
WswhhHWlRTsQDwWHTRhsvNVvwqzfVmNBtZNmnzzq
cjcPfLlQtPsZQlfHZJqVSFdVwmSRRqSSddwDvF
MgNbBgzgnwdPRFmSPn
CMGbNNMhCMzzPzBpTNPGBclLcLfsptHQfQlZssLcLf
slsdfpSlllpTVJJGgGDgHMdV
wrBQrbQrhQcpbQrhLwRBrjVVgGGPgZMtZMVhgMPMGHPg
QQwRnrwRbbRcmQmrjRnjpvNsNTNSlTmsTqCSvsNSWz
GWNwppdHdpmzgPFPCRmlCBPB
bSrJhJSsMhrJMDPRCPBlwVCtVSLV
QbsbwqQZvrJhhQrhZZrhchTfnTWGNvWpNnjHGvGjNdGT
NMZGmnMBWmwmNnGwHrHvHzfrvrVVVj
pSbDRLgbpJDPpRZRQjjFqVhhDFjDVqfrzv
sQQscLTZcsTpRsBnmlBcdCMBMtlc
hwWslbGWbRvLZvcscZ
gQnmmrNTmSnTfgwDwVwpJvJPJzLqLJTLLvRcZz
mrmnSrDNNQSmmwdggrrDbHMGhtdtGhGlhtClMGhM
qQdlGcvDQDQvDdmtPmmmlStbjSrm
CpNhzWTCTRznBMvwtTjMrHtSvj
nWzsfZCsBhNpZLgGdQDddvqd
ggjTjJWDVVVRTwQcZWvchshWhs
LmFfLfSmBtCttNLfCFBPFNBvvvhrcQdvsrsdSwdqcwrwSw
CHttltmlPLMHRTgJQDgRDTMb
RPJgCdhgPPSzvWDcCfGHDcvf
HbrrwBspTwWDDnqbZjjD
rQrFsrsstQMQHJdHQm
GVwQVGBZBNQwsjdNcMMlgJNPgj
SWFfSzTCSWFCSpgnJLSjpMdc
FhTbvrzrMrDCVHsVsHGBtHwv
FsqjjVzFVWFqRRWBssdpNSBHwJpHHJJdddSN
lQgmhvbTcgTgfhTQhSCFCGJHSlwNtJdGHG
vgZPbbfMhbTmchhjRFRnsDRPWVqzWz
cvwfjjcJjqhctvSpCgCFVhrFCrpC
mRsQmsMlNNzznWQlRnsMRQlSCpLNbpwSSSrwFLDFLLLgFp
zznlnGlmRmMlPZnGQzMszMRfccTjcBJjtJtJjqTZtfwBTt
PtCwCCVqbjNNqqvGssPmHGsHMfPH
dcddcWFDJJJcLczhWQdcDScZvHZgpGfsvMfSmsggSvvnvM
TTQmTDhdQQzdRwjBVrRwCwBbBr
BnBsFHCrcnBrMBPSmMSCmrcFqnZLddLhdhdGLvqLqgqnLJJp
WfjTlNVDTtjzNWTlVMWNlTwTJphdgpvJLGLdgghZvGLpwddq
zVjbVblVDlNTlbzTzDjllDTzHmHCsmcMHcSBrCBbrHBcBPSC
ddlcGQlCjQNGQmPLslZTlmTtfT
MDzMwSwqpzpDRpWRJwgZhttrZmTPfZmrmtrMZZ
JSqRBpJzwgDDpqDqvpBRdCjbCjQCFCbHvdGPjdHQ
bwzPwGLZMsbJMPPLGLMQzbhhQRvWWtVqVhgCVtWWQDqt
HddrHFnFNpVnVLhnvLRV
NLdrFjHTBrrdjFSpFmNBmSfZMwZMJJfSffbwzwPbczbJ
QTWSzTTLwTfwflSNJRdvGlRGcNgJBl
FnmmqrqbBBgRbHGc
MFZqrCVCqmZCprspFZmnnMsDfzWzDwSfjSwPQPTLhffwBLwj
npfgFRTZRRnDZLdgRfRrrjcWzGpWGGGQrjjWpP
vblVbvSShhVzHWjzzlrPWG
bVwqvCBtShqBhCCtqhNqCJRTTBDFJJLnJgDRWFBnWg
nHDNQvgvnNZHDnsGcjfNTrTfVrfL
SRWFSBRLtSFqjTrVVcsVjTSG
BdBbRttWBdbdWdbppmZlLmgwHvgQvgLZ
PQRZlpDDptQSclBMGVBdhVFGBMpf
nnrsTCWjLJsnsSMShhGJfwffwV
vjzqsjqgSHbbtvHZ
DgFmbdSDZbPgLbDDmFwZwgLSfccGcGvnvvngsGGnsGMNWsWs
HqztHHhHVhHjhRRhJtCVBCfNprMWpcMMJfsvvMsGscpG
tjVtBVTBtHHqCRqtzQwTPSNdSwPTTbPFDdml
sbmBmHZbRRRmwBmsSjHzRjmSCNFLNLLQNQhFgtQLzNztlrff
MpqPPDPVnGqrJpcqqJpMVlgtlLFLChCgChCCQgCtCD
VdcVVJvdrVWHbwHWBSSBRb
tPDVBzzNSNdDSQpMQMTQJMMQMN
LqSWSmbsmfQTTGZMWGCW
cLjLcbrjqmvfqLbfmqLwDBBzSHPzlwzcdBlnnP
SbnHrGHSrrhHJBrrScDfcPDMfpPGcGcpDL
QTpmpmmQWlZsTvVQDMgggFLgFcPf
zsCNlltCslzlTNsNlShwdJCpSqdHrBhpwr
JZmFrmLGjFZdDGrrVTvzmPVvRRVzwzzl
WBnfMDBqMsgDBqpBvzwVlCwRTRRPpvlw
WfghfttggfSnnqbDftfqSBBDQdHhZFFJrrHFjGJdGjFrjQLj
rNLRjrlVlrFRJzlsjrVlRFGCmnMtftgCNDDgDmCfqNgPNM
SpdBpdHbpHWhZqnCdtCGggqCPn
QHHvvWwWhwVVQRscVzGl
QffLtMQGMQfDMMwMTJwqWHvH
nSSFznjFcfjTgVJTJjvT
RrBpcfSNpRBcFshrCtQrDGLPQb
GctcMldStGwPPbcLsQTV
jhnzDgnHnnfPVwHQTTLTds
gBgzDDhzvqdGGvrtdvtm
PPwRWVTvRvPVLwRpMlzmbmsbHWjbbs
dFTFCNfdjzjFjsMF
SgdffSTrnnqCgdqgcNrfSZqVvVLRDPJZQwJBLPQPtLZwJJ
HSzDQftHphTBHFhr
WMmJsMJNLWNPmmsncjMJcjtvwggVvhFFFhjrVwrjrjppvT
WWPsJJCWCtZZZRGC
SfFZQDRLgpLlRgQRRRFWTsbhBhgTjbWBjhshgw
tHVNGjtzzHvMMJJhrWJNrTrPbP
jvVVvGCGtCmjHtdHzQQfDpSSlDRnFfQFmR
ZBBPfVVPPrVmrWZJzNdPznbnbSzznP
gvgpGqFFMgMcGgwLwGpcJNZSTZbdbdzNNSlqbTnn
ssZLgsMLQvcFpVrhCsmtWHjrrW
nFvhRnWWzBRPHQqcqqCqmFbd
SJDJgVprLfDfbJmHmWWHQtJW
wVsgWVSTgLjfSsVjVBRvRNwwGGRhNZhRMZ
wTRrRBCTPTBPlgMqgHCqggHLgg
dmDzpQpBdmWmWzzzDFzjGNMSWLSgLVGGLVNSLgSg
JbFdmQQJpjpptQbdJJmDmdtnZhZRflTlnTrTlrhBwPPc
jwSwssQbwbStlhRgtsVstn
zPzFdFFZccPDgntzVHHgghRz
vVVdfFmZPDMWZZBmGQbwJJGCLwwMwJCS
PLLffLFqqNLwSffbnVzzRf
lsmgTggChrgDtZsZVblMVJMznVnwMBnb
hDZZTmZvhTgstvwNFdqpWQcqvP
mmWwpwqtmmHTqHpprRZQPPZLZWSFRFRB
gzcgscgbfvhRRNZQRRQPvr
JsjhcshCfJgrrpttTCTplH
TvNrvNrJfWWvtJLTHhvZZhQQwVGZZhbV
mFCPmBMPlPsPPBsMFPszbHQJwwHHhbZVQVzjhGHZ
qmlBsdCSmJBmsBBMnMMTDWDNcLrDprSNcWDNrW
HSnHCVqTddFHSVqFqdStSQGQwRzQCzCRzGRRGNPQwz
jhlBpgNvlfZjlfvmpgfgfBrMRRwMMPPLQMZRPMWMMZPQ
hflfpgjfBfDcpchlpvndbHFDdHqSqNVqNVdn
QBfhlVNfHSZHfVCVHSQfZfTCctdvdDTRtjDCtTRsjsvj
brrWWqzFWzwWbswDchhTRtDhjT
gbrFLnpzqrWPgqpLWrhnHGZlSfLfHfQBGVfHHNVG
hcFmVScmQBVhtcvfHLfvHSnbHRLn
lzQqlDqgpWPvJfRnlNJvww
PjCCCPgDgqGzmMtCQstZmBFs
GrnrHrmVVFMFhSSbSfhR
zjTqLtBjjdWdWTLshMZMDbPNRMSSqSPNfD
dTWjdtwWhjWTBzcnrpcwmQpCwcpw
BgtVBsgVVJhgGsSGJbghJqbsjLfZmLjmmtfZndNNZFFZNLdm
MHTlzlwHSvPvzMSPCTMQCNZdjjmnfQjdZfNLjF
HMDTwPDpzrTzpScBghDbVqRBgRBJsR
qjCsTmrrnnCmhcFrCjqmThRlbHGvJGvvvbRbbJRcQJRG
fVBBTfMdSZLNZgPdgglGRdbtbtJRllJWJtWb
TSZZSpNMPBLgpZLVgppBDFhzDmjrnzhjssFqDhzFnn
MDtDMWmMQmdzmMMqvlGfRcjzgpcPPjczPl
sZsHJWNJFJNbWFBhFBnnbVclbVVPglfcRggffGGpjl
srHWLNZZJdSLSdvDMw
BFqsPnsZcgnncggccqsqqpDPtDWPpPNTNSNThrWtSj
dQbfQQJJdwdmFRbJLRJdMrfDWrjpDrrprhDDDDNWWD
QGwdJmCFJZvGsvvncB
GRRNSjrffGTSPrNTffSgcJTwWJZbbZvwvwtVwWVJZv
CMcFsqmBQzMzshsBQBQvLWmJVwZtpJLJwJLvwt
qBzChnQlzMcRSnnRRjHGGg
dPPbPWNdTBbDpHPHpNsgzvFlglvHzvSFzCFF
fntqhGhRMhnnnGGCVMRhCVlSjswFvvjzjSzvQVSgsl
MMqqJJRCnMhZLCRhtPNrpZPDDWTDTrNBmD
VjVGNTNlNchVjNGRWrSWWtZtRrzncR
BTbbbwDmCDLTbDwfHmzZMmRrWtzPrZSZtrrz
qDLLqvwLBsfBbBdQFQTJhqThVTQJ
qBqPBGZflhrWznzZZdsnzv
FmHRcCCsCDwDbjtzdjWbdz
cTRwCCNHFNmwRgmFTNCFTJqqfqPJsPhPBlsrsfGf
JTNhhNrCTcWpJJcpWw
LLdLsfMsdStbtggLbnTpwfWDzpjvnnjzcz
MqSZsgbMbGFbZtgTSZSFSLhhmHlBQlmrmrPHHCPPZPBr
GgjjgpGvpJJtjgvPrJttsLjVwCsQsQNLsfLfMVCl
RddqZqzcZdSWcHdcqQfQLMwVflfNQNMQ
FncWTRcFlHWFmcFTgPJhGvDgpnnhhGtG
ZGPFJsPQCbZCCbgz
nrvrnGWTwwqTBRcpCRRg
DnGWDldNmSLSMdMQ
ScDmPPPmjmjjWgtdSmdmCnNqVQVVrNRTZTQTQDHHZGNH
wbbMhLvMJpRwJQrJGHqQGrQHqr
wzhspwpppswsMFLmtnzjdcmdPRWPtS
fPlLTtBlTjDbWcTMJcncWqss
LdvLrLpCRRQQmvhhVNpwRMWJZcFMZWJwJFFFwZsGcs
prrRVpvvRVNmRvvzHjHPlzPLSffbbPHS
bbCbzsQbBzbBFbFzFfJHfVJPfVPtzZttpm
hwvrjDDwjcDcvdnNvwdnwwDPpNtNMVtPpJpRmVMPfmtVZR
mmqDWjhcqhwvDDdTsSGGCbQGSBBLTGGl
wthtwrBQhhSrqJJVLMRPPtJLPF
vbmbZqfqgsfHmcllmLLJNLJMNFJNNvPGJn
jHlDscllClCCgbZzhWqBzBQzprWCqS
DwpDlwDwllhJwbDFNDwFPhDnQnZZzVVnnBrtNznzSSzZrr
MHPfWRTgWzTQmSTTZt
GdPjHLRMCfcGvwqDGbFq
NGdNpDPdNGLppLpwSNFFFDLwnnZbMnrHlHZQcHbcnHQcPcQM
jBgBsjssgjWJVGhBfhvJVnMlbnZQVrrrlHCcCZrl
sRBgvRffhhtvtBgvjgttWBJTLmFLLwdwzFdqLDDDqFGdLFTd
RBzRGRGBgnrPJrRGGWWbDggZTSTVZVFFSVZZdw
tfmLhjfshNNsqpppfjHdwVdQZbVbQFVVTmSVDV
jvqtwHqCNLNsNhNfjssLCzGJWcBRJRBCBBBrrWnGrG
cGDBdNFdNdDStNtGdGQGscDMvZjjZWMvMLjsjjLZjLsJLv
fbRnRzHVPClfRlbbmfHRlPvZvMLpqjvZJqZMpzMpZjBZ
gfbfBgCHCPVNhNGgTtFDcF
ljjvLZvvllFnlLJLJjLWFQrVssFpsGMFpNMGsr
qbHSqHTcHChqCmTSRqqBVpVdBQsVQQGHdMprWV
DbtcCqRhhTRmDnPMlLgfgztlZZ
QtMQzPZcbtGgTtLvtf
HwcDsdVVDnNSGLhwvffJvfTT
CSsdSHNmSDHcCqqcrrzQcC
nDNDfmMnmDJRNfJJdMDRBdwjcTtsSHvBTswTjwLtsCts
QcbQrZZggGWVVWbZZjStswCSCCttGCwLvC
ZgZgbzVglVbchVVrVhFWWpnnpNJmJMqDfMJnMRqNDDMD
WMfNvsjWGjsqFjqTRRQVJztDzVmJHbft
ZPhplcrLrmzQGzmz
ZPddLPlcSclhZChndMvgTjjWNGWMGWBj
nDLjMchghDcljfjffpfsqTmGCTGszGZVVzHV
wdFJPFrQRwSNbjVQCTGsHZHmHCHs
BRJJSddvdBrJwrBRNRFRSPRjvclLpWhpglgWpLplltnMgh
BbVRzMcpbMNMHMTJmWdljdlJjT
GtsqFnfvGSFqGfQvgnWWZlLlLjZWtWldPmlT
sSsFqsqsGghwQQmfGRHbbVczbwwBpBpHcw
BBFCBJCsGJBBgvgsvTlVhgNg
ZnLdjRQddLRnZrlScHRVTTSHhRvg
fnnjZLWdrnqdWrrPLddqVqBzGDJJFGCBDfJmbDzFMbmB
''')