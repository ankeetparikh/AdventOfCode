import re
import numpy as np
def solve(a):
	a = a.strip().split("\n")
	a.sort()
	g, t = -1, -1
	z = {}
	for rec in a:
		if "begins shift" in rec:
			g = int(re.findall("#(\d+)", rec)[0])
			if g not in z:
				z[g] = np.zeros(60)
		if "falls asleep" in rec:
			t = int(re.findall("00:(\d+)", rec)[0])
		if "wakes up" in rec:
			nt = int(re.findall("00:(\d+)", rec)[0])
			z[g][t:nt] += np.ones(nt - t)
	gb, sl = -1, -1
	for k,v in z.items():
		if sum(v) > sl: gb, sl = k, sum(v)
	print("Part 1:", int(gb) * np.argmax(z[gb]));

	gb, sl = -1, -1
	for k, v in z.items():
		if v.max() > sl: gb, sl = k, v.max()
	print("Part 2:", int(gb) * np.argmax(z[gb]));

solve(
'''
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
'''
)

solve(
'''
[1518-08-06 00:13] falls asleep
[1518-06-10 00:37] wakes up
[1518-07-08 00:20] wakes up
[1518-05-13 00:24] falls asleep
[1518-11-07 00:32] falls asleep
[1518-11-21 00:01] Guard #641 begins shift
[1518-05-29 00:31] falls asleep
[1518-09-28 23:59] Guard #3023 begins shift
[1518-02-20 00:40] wakes up
[1518-08-17 00:38] falls asleep
[1518-09-16 00:28] wakes up
[1518-03-13 00:55] wakes up
[1518-10-07 00:02] Guard #2969 begins shift
[1518-04-01 00:28] falls asleep
[1518-05-28 00:02] falls asleep
[1518-10-03 00:28] wakes up
[1518-08-21 00:00] Guard #1613 begins shift
[1518-08-31 00:00] Guard #1973 begins shift
[1518-05-06 00:07] falls asleep
[1518-09-23 00:02] Guard #2437 begins shift
[1518-07-06 00:32] wakes up
[1518-06-12 00:02] Guard #619 begins shift
[1518-07-24 00:29] falls asleep
[1518-08-06 00:59] wakes up
[1518-03-08 00:24] falls asleep
[1518-09-26 00:15] falls asleep
[1518-02-26 00:52] falls asleep
[1518-06-23 00:03] Guard #641 begins shift
[1518-02-18 00:04] Guard #131 begins shift
[1518-04-01 00:24] wakes up
[1518-10-27 00:46] wakes up
[1518-04-26 00:50] wakes up
[1518-03-23 00:55] wakes up
[1518-06-16 00:30] falls asleep
[1518-08-20 00:48] wakes up
[1518-05-18 00:01] falls asleep
[1518-04-19 00:57] wakes up
[1518-06-01 00:04] Guard #641 begins shift
[1518-07-11 00:37] wakes up
[1518-05-04 00:15] falls asleep
[1518-07-04 00:02] Guard #619 begins shift
[1518-10-09 00:32] falls asleep
[1518-08-02 00:48] falls asleep
[1518-04-23 00:23] falls asleep
[1518-07-09 00:04] falls asleep
[1518-04-29 00:29] falls asleep
[1518-10-19 00:57] wakes up
[1518-08-19 00:20] falls asleep
[1518-11-14 00:32] falls asleep
[1518-09-04 00:52] falls asleep
[1518-08-28 00:03] Guard #619 begins shift
[1518-06-05 00:24] falls asleep
[1518-02-16 00:01] Guard #3253 begins shift
[1518-03-10 00:46] wakes up
[1518-10-20 23:58] Guard #2437 begins shift
[1518-07-31 00:42] wakes up
[1518-06-25 23:58] Guard #3023 begins shift
[1518-08-22 00:47] wakes up
[1518-08-05 23:59] Guard #2437 begins shift
[1518-09-02 23:57] Guard #2969 begins shift
[1518-11-16 00:42] wakes up
[1518-08-03 00:14] falls asleep
[1518-02-27 00:04] falls asleep
[1518-06-29 00:38] wakes up
[1518-06-06 00:12] falls asleep
[1518-04-10 00:38] falls asleep
[1518-04-25 00:02] falls asleep
[1518-08-02 00:03] Guard #103 begins shift
[1518-11-05 00:58] wakes up
[1518-08-05 00:04] Guard #1493 begins shift
[1518-06-09 23:49] Guard #1373 begins shift
[1518-04-07 00:13] falls asleep
[1518-04-01 00:00] Guard #1613 begins shift
[1518-05-05 23:57] Guard #131 begins shift
[1518-02-27 00:38] wakes up
[1518-03-24 00:50] wakes up
[1518-05-29 00:55] wakes up
[1518-04-15 00:48] wakes up
[1518-04-13 00:43] wakes up
[1518-06-17 00:19] falls asleep
[1518-10-08 00:52] wakes up
[1518-06-13 00:04] falls asleep
[1518-10-26 00:57] wakes up
[1518-02-19 00:02] Guard #2797 begins shift
[1518-02-26 00:37] wakes up
[1518-06-01 00:55] wakes up
[1518-05-09 00:29] falls asleep
[1518-09-09 00:42] wakes up
[1518-11-03 00:49] falls asleep
[1518-08-14 00:26] falls asleep
[1518-04-04 00:58] wakes up
[1518-03-17 00:00] Guard #1487 begins shift
[1518-09-12 23:56] Guard #1613 begins shift
[1518-08-01 00:18] wakes up
[1518-08-21 00:35] falls asleep
[1518-11-18 00:03] falls asleep
[1518-06-04 00:48] falls asleep
[1518-07-18 00:51] wakes up
[1518-03-29 00:00] Guard #2089 begins shift
[1518-06-07 00:33] wakes up
[1518-10-31 23:51] Guard #3023 begins shift
[1518-07-26 00:20] falls asleep
[1518-04-03 00:10] falls asleep
[1518-04-28 00:59] wakes up
[1518-05-23 00:52] wakes up
[1518-08-01 00:45] wakes up
[1518-09-27 00:40] falls asleep
[1518-02-12 23:57] Guard #103 begins shift
[1518-10-21 00:32] falls asleep
[1518-07-02 00:56] wakes up
[1518-05-17 00:38] wakes up
[1518-11-17 00:59] wakes up
[1518-07-31 00:19] falls asleep
[1518-07-23 23:58] Guard #2089 begins shift
[1518-09-04 23:48] Guard #2389 begins shift
[1518-10-13 00:13] wakes up
[1518-02-19 00:51] wakes up
[1518-04-23 00:56] wakes up
[1518-05-10 00:00] Guard #443 begins shift
[1518-05-09 00:02] Guard #2437 begins shift
[1518-03-19 00:02] falls asleep
[1518-05-19 00:55] wakes up
[1518-05-20 00:03] falls asleep
[1518-10-24 23:56] Guard #2389 begins shift
[1518-09-03 00:14] falls asleep
[1518-09-25 00:05] falls asleep
[1518-09-28 00:01] falls asleep
[1518-07-06 00:23] falls asleep
[1518-04-08 23:57] Guard #1033 begins shift
[1518-08-11 00:45] falls asleep
[1518-06-26 00:37] wakes up
[1518-05-12 23:57] Guard #131 begins shift
[1518-02-14 00:49] falls asleep
[1518-06-08 00:07] falls asleep
[1518-10-28 00:01] Guard #1493 begins shift
[1518-10-20 00:58] wakes up
[1518-04-14 00:42] falls asleep
[1518-09-05 23:56] Guard #1613 begins shift
[1518-04-25 23:59] Guard #2797 begins shift
[1518-07-07 00:18] falls asleep
[1518-06-20 00:36] falls asleep
[1518-04-12 00:13] wakes up
[1518-05-18 23:59] Guard #1033 begins shift
[1518-05-02 00:17] falls asleep
[1518-09-26 00:02] Guard #3391 begins shift
[1518-08-23 00:58] wakes up
[1518-10-12 23:50] Guard #3023 begins shift
[1518-09-24 00:33] wakes up
[1518-09-13 00:59] wakes up
[1518-04-20 00:00] Guard #2389 begins shift
[1518-11-05 00:05] falls asleep
[1518-02-16 00:29] falls asleep
[1518-03-29 00:14] falls asleep
[1518-07-12 00:34] wakes up
[1518-09-20 00:04] Guard #1487 begins shift
[1518-07-29 00:03] Guard #2447 begins shift
[1518-03-21 00:31] falls asleep
[1518-04-06 00:46] falls asleep
[1518-04-10 23:59] Guard #2683 begins shift
[1518-03-30 23:59] Guard #131 begins shift
[1518-09-28 00:51] wakes up
[1518-05-21 00:51] wakes up
[1518-06-12 00:53] falls asleep
[1518-10-30 00:48] falls asleep
[1518-05-17 00:54] falls asleep
[1518-04-30 00:51] falls asleep
[1518-07-26 00:40] wakes up
[1518-10-15 00:03] Guard #1033 begins shift
[1518-06-17 00:50] wakes up
[1518-10-24 00:57] wakes up
[1518-03-03 00:58] wakes up
[1518-06-03 00:03] Guard #641 begins shift
[1518-05-03 00:24] falls asleep
[1518-08-03 00:51] falls asleep
[1518-09-12 00:01] Guard #443 begins shift
[1518-10-29 00:23] wakes up
[1518-08-26 00:50] wakes up
[1518-09-18 00:41] wakes up
[1518-03-15 00:45] wakes up
[1518-09-24 23:53] Guard #1493 begins shift
[1518-03-16 00:42] wakes up
[1518-09-24 00:44] falls asleep
[1518-06-29 23:59] Guard #2389 begins shift
[1518-08-08 00:24] wakes up
[1518-05-26 00:49] wakes up
[1518-07-20 00:58] wakes up
[1518-05-10 00:51] wakes up
[1518-03-30 00:55] falls asleep
[1518-08-23 00:24] falls asleep
[1518-07-16 00:00] Guard #2437 begins shift
[1518-03-29 00:41] wakes up
[1518-03-12 00:59] wakes up
[1518-11-10 00:48] wakes up
[1518-10-14 00:49] falls asleep
[1518-04-15 23:59] Guard #1373 begins shift
[1518-06-25 00:04] falls asleep
[1518-05-25 00:01] Guard #1373 begins shift
[1518-10-19 23:56] Guard #443 begins shift
[1518-10-04 00:34] falls asleep
[1518-08-28 00:29] wakes up
[1518-02-12 00:05] wakes up
[1518-08-03 23:50] Guard #1487 begins shift
[1518-09-15 00:44] wakes up
[1518-09-11 00:00] Guard #443 begins shift
[1518-06-28 00:28] wakes up
[1518-03-01 23:58] Guard #1033 begins shift
[1518-09-01 00:12] falls asleep
[1518-03-08 00:50] wakes up
[1518-08-16 00:36] falls asleep
[1518-09-27 00:09] falls asleep
[1518-05-25 00:57] wakes up
[1518-07-27 23:56] Guard #131 begins shift
[1518-03-12 00:20] falls asleep
[1518-08-10 00:21] falls asleep
[1518-06-08 00:56] wakes up
[1518-11-20 00:40] wakes up
[1518-11-16 00:57] wakes up
[1518-06-07 00:58] wakes up
[1518-02-26 00:18] falls asleep
[1518-09-11 00:45] falls asleep
[1518-05-29 00:01] Guard #2969 begins shift
[1518-06-15 00:27] wakes up
[1518-02-23 00:23] falls asleep
[1518-09-01 00:02] Guard #3253 begins shift
[1518-11-10 00:54] falls asleep
[1518-06-24 23:51] Guard #2447 begins shift
[1518-10-13 00:05] falls asleep
[1518-02-12 00:22] falls asleep
[1518-10-08 00:47] falls asleep
[1518-11-04 00:16] falls asleep
[1518-02-22 00:04] Guard #641 begins shift
[1518-10-19 00:45] falls asleep
[1518-07-21 00:29] wakes up
[1518-09-29 00:12] falls asleep
[1518-03-26 00:52] falls asleep
[1518-04-12 00:03] falls asleep
[1518-10-11 00:55] falls asleep
[1518-04-19 00:13] falls asleep
[1518-04-07 00:03] Guard #3391 begins shift
[1518-04-26 00:14] falls asleep
[1518-03-13 00:12] falls asleep
[1518-10-18 00:58] wakes up
[1518-09-16 00:11] falls asleep
[1518-07-22 00:43] falls asleep
[1518-07-21 00:00] falls asleep
[1518-06-27 00:59] wakes up
[1518-07-14 23:58] Guard #443 begins shift
[1518-09-20 00:49] wakes up
[1518-09-19 00:04] Guard #3253 begins shift
[1518-03-31 00:43] wakes up
[1518-06-27 00:19] falls asleep
[1518-07-14 00:43] falls asleep
[1518-03-18 00:34] wakes up
[1518-03-27 00:38] falls asleep
[1518-05-16 00:23] falls asleep
[1518-03-02 23:59] Guard #131 begins shift
[1518-05-01 00:52] wakes up
[1518-06-15 00:11] falls asleep
[1518-05-23 00:25] falls asleep
[1518-05-03 23:59] Guard #2389 begins shift
[1518-03-03 00:40] wakes up
[1518-11-05 00:56] falls asleep
[1518-10-06 00:39] falls asleep
[1518-03-03 23:48] Guard #2969 begins shift
[1518-10-20 00:50] falls asleep
[1518-08-02 00:52] wakes up
[1518-04-14 00:54] falls asleep
[1518-03-21 00:21] wakes up
[1518-08-27 00:59] wakes up
[1518-10-03 00:36] falls asleep
[1518-11-05 00:13] wakes up
[1518-11-20 00:12] falls asleep
[1518-06-23 00:07] falls asleep
[1518-05-26 00:28] falls asleep
[1518-03-11 00:56] wakes up
[1518-07-28 00:37] wakes up
[1518-09-22 00:52] falls asleep
[1518-03-25 00:30] wakes up
[1518-06-22 00:15] falls asleep
[1518-11-08 00:44] wakes up
[1518-09-06 00:31] falls asleep
[1518-04-06 00:56] wakes up
[1518-11-16 00:03] falls asleep
[1518-07-06 00:01] Guard #2417 begins shift
[1518-10-12 00:53] falls asleep
[1518-09-17 00:01] falls asleep
[1518-05-20 00:13] wakes up
[1518-06-24 00:04] Guard #2447 begins shift
[1518-08-18 00:02] Guard #1913 begins shift
[1518-08-12 00:00] Guard #3391 begins shift
[1518-03-27 00:56] wakes up
[1518-10-05 00:00] Guard #2447 begins shift
[1518-11-08 00:31] falls asleep
[1518-07-22 00:39] wakes up
[1518-06-09 00:43] falls asleep
[1518-03-12 00:38] falls asleep
[1518-06-24 00:38] wakes up
[1518-03-07 00:20] falls asleep
[1518-07-13 00:56] wakes up
[1518-03-20 00:35] wakes up
[1518-04-13 00:26] falls asleep
[1518-09-27 00:53] wakes up
[1518-09-23 00:51] wakes up
[1518-10-15 00:49] wakes up
[1518-07-04 00:36] falls asleep
[1518-09-26 00:23] falls asleep
[1518-03-21 00:59] wakes up
[1518-10-28 23:51] Guard #103 begins shift
[1518-06-22 00:00] Guard #443 begins shift
[1518-06-13 00:49] wakes up
[1518-06-20 00:47] falls asleep
[1518-05-14 00:31] wakes up
[1518-11-09 00:59] wakes up
[1518-05-02 00:46] wakes up
[1518-08-16 00:50] wakes up
[1518-06-20 00:57] falls asleep
[1518-07-14 00:01] Guard #619 begins shift
[1518-11-02 00:26] wakes up
[1518-09-19 00:20] falls asleep
[1518-10-27 00:58] wakes up
[1518-06-02 00:34] wakes up
[1518-03-05 00:00] Guard #2969 begins shift
[1518-05-16 00:33] wakes up
[1518-08-14 00:51] wakes up
[1518-09-08 00:25] falls asleep
[1518-02-23 00:17] falls asleep
[1518-02-18 00:29] wakes up
[1518-06-12 00:15] falls asleep
[1518-08-11 00:42] wakes up
[1518-06-02 00:38] falls asleep
[1518-04-28 23:56] Guard #619 begins shift
[1518-08-27 00:36] wakes up
[1518-11-18 00:53] wakes up
[1518-10-13 00:27] wakes up
[1518-09-05 00:05] falls asleep
[1518-11-15 23:47] Guard #2417 begins shift
[1518-08-27 00:35] falls asleep
[1518-11-06 00:46] falls asleep
[1518-02-22 00:42] wakes up
[1518-10-16 00:02] falls asleep
[1518-03-18 00:51] falls asleep
[1518-05-02 23:57] Guard #1487 begins shift
[1518-08-17 00:19] wakes up
[1518-03-11 00:55] falls asleep
[1518-07-20 00:11] falls asleep
[1518-04-27 00:45] falls asleep
[1518-03-10 00:41] falls asleep
[1518-05-17 23:49] Guard #2969 begins shift
[1518-10-07 23:58] Guard #2389 begins shift
[1518-08-12 23:56] Guard #2389 begins shift
[1518-02-15 00:00] falls asleep
[1518-03-28 00:56] falls asleep
[1518-10-09 23:53] Guard #2797 begins shift
[1518-02-17 00:32] wakes up
[1518-02-15 00:05] wakes up
[1518-05-12 00:21] falls asleep
[1518-06-04 00:54] wakes up
[1518-08-11 00:02] falls asleep
[1518-08-29 00:05] falls asleep
[1518-07-10 00:59] wakes up
[1518-06-21 00:30] wakes up
[1518-07-25 00:02] Guard #2447 begins shift
[1518-04-22 00:45] wakes up
[1518-02-16 23:59] Guard #641 begins shift
[1518-06-27 00:47] wakes up
[1518-06-02 00:29] falls asleep
[1518-02-14 00:44] wakes up
[1518-11-10 00:39] falls asleep
[1518-10-24 00:38] falls asleep
[1518-05-28 00:54] wakes up
[1518-08-08 23:49] Guard #1493 begins shift
[1518-05-02 00:00] Guard #2417 begins shift
[1518-08-24 00:04] falls asleep
[1518-06-21 00:41] falls asleep
[1518-08-19 23:59] Guard #2797 begins shift
[1518-05-02 00:50] falls asleep
[1518-08-04 00:01] falls asleep
[1518-09-11 00:34] falls asleep
[1518-10-15 23:49] Guard #641 begins shift
[1518-07-25 00:14] falls asleep
[1518-04-20 00:28] falls asleep
[1518-02-25 00:41] wakes up
[1518-08-10 00:55] falls asleep
[1518-08-15 00:40] wakes up
[1518-09-21 00:56] wakes up
[1518-08-26 00:27] falls asleep
[1518-07-30 00:59] wakes up
[1518-07-18 00:04] Guard #2389 begins shift
[1518-08-07 00:57] falls asleep
[1518-06-25 00:17] wakes up
[1518-03-23 00:44] wakes up
[1518-06-09 00:36] falls asleep
[1518-10-09 00:40] wakes up
[1518-04-14 00:50] wakes up
[1518-11-14 00:35] wakes up
[1518-05-17 00:30] falls asleep
[1518-03-26 00:43] falls asleep
[1518-10-22 00:53] wakes up
[1518-02-15 00:36] wakes up
[1518-08-21 00:46] wakes up
[1518-07-08 00:03] Guard #2797 begins shift
[1518-10-20 00:46] wakes up
[1518-03-17 00:53] wakes up
[1518-03-27 00:05] falls asleep
[1518-05-04 00:46] wakes up
[1518-03-15 00:30] falls asleep
[1518-10-29 00:00] falls asleep
[1518-05-04 23:59] Guard #1613 begins shift
[1518-04-02 00:07] falls asleep
[1518-06-06 23:59] Guard #2417 begins shift
[1518-04-02 00:51] wakes up
[1518-10-14 00:04] Guard #2389 begins shift
[1518-06-19 00:48] falls asleep
[1518-08-27 00:41] falls asleep
[1518-04-16 00:40] wakes up
[1518-08-11 00:47] wakes up
[1518-03-10 00:13] falls asleep
[1518-10-22 00:04] Guard #1033 begins shift
[1518-05-29 00:42] wakes up
[1518-03-05 00:26] falls asleep
[1518-05-07 00:44] wakes up
[1518-10-25 00:42] falls asleep
[1518-08-13 00:48] falls asleep
[1518-05-18 00:29] falls asleep
[1518-06-01 23:59] Guard #641 begins shift
[1518-08-22 00:00] Guard #641 begins shift
[1518-10-10 00:04] falls asleep
[1518-07-23 00:04] Guard #3253 begins shift
[1518-04-24 23:52] Guard #2797 begins shift
[1518-07-23 00:57] wakes up
[1518-08-07 00:54] wakes up
[1518-03-09 23:56] Guard #1613 begins shift
[1518-09-16 00:00] Guard #1493 begins shift
[1518-06-16 00:07] falls asleep
[1518-03-29 00:24] falls asleep
[1518-05-25 00:48] falls asleep
[1518-09-20 00:13] falls asleep
[1518-08-16 00:14] wakes up
[1518-10-29 00:31] falls asleep
[1518-06-05 00:03] Guard #3253 begins shift
[1518-06-30 00:25] falls asleep
[1518-06-19 00:56] wakes up
[1518-11-21 00:57] wakes up
[1518-09-04 00:35] wakes up
[1518-10-23 23:59] Guard #1487 begins shift
[1518-09-11 00:53] wakes up
[1518-08-01 00:29] falls asleep
[1518-04-04 00:13] falls asleep
[1518-05-24 00:50] wakes up
[1518-04-26 00:42] falls asleep
[1518-03-26 00:29] falls asleep
[1518-02-14 00:56] wakes up
[1518-04-13 00:33] wakes up
[1518-09-23 00:34] falls asleep
[1518-04-03 00:00] Guard #2389 begins shift
[1518-10-09 00:24] wakes up
[1518-03-24 00:00] Guard #2417 begins shift
[1518-11-14 23:57] Guard #1973 begins shift
[1518-11-22 00:55] wakes up
[1518-02-16 00:57] wakes up
[1518-10-01 00:52] wakes up
[1518-11-13 00:13] falls asleep
[1518-06-19 00:03] Guard #1487 begins shift
[1518-10-30 00:10] falls asleep
[1518-03-15 00:51] falls asleep
[1518-08-07 00:42] wakes up
[1518-09-11 00:42] wakes up
[1518-02-11 00:14] falls asleep
[1518-09-30 00:55] wakes up
[1518-06-20 00:59] wakes up
[1518-06-04 00:45] wakes up
[1518-07-24 00:57] wakes up
[1518-06-13 00:20] wakes up
[1518-02-25 23:57] Guard #131 begins shift
[1518-11-14 00:02] Guard #1373 begins shift
[1518-07-05 00:01] falls asleep
[1518-10-03 00:11] falls asleep
[1518-07-16 00:21] falls asleep
[1518-06-11 00:52] wakes up
[1518-06-30 23:56] Guard #2417 begins shift
[1518-11-07 00:35] wakes up
[1518-09-18 00:02] Guard #131 begins shift
[1518-06-12 23:47] Guard #131 begins shift
[1518-03-30 00:08] wakes up
[1518-04-19 00:41] falls asleep
[1518-06-20 00:51] wakes up
[1518-05-28 00:44] wakes up
[1518-07-17 00:56] wakes up
[1518-10-11 00:56] wakes up
[1518-04-14 00:39] wakes up
[1518-08-10 23:50] Guard #3391 begins shift
[1518-10-17 00:54] wakes up
[1518-04-07 00:41] wakes up
[1518-05-21 00:56] falls asleep
[1518-08-09 00:42] wakes up
[1518-11-21 00:23] falls asleep
[1518-04-05 00:16] falls asleep
[1518-07-08 00:19] falls asleep
[1518-02-26 00:53] wakes up
[1518-03-15 00:55] wakes up
[1518-04-02 00:32] falls asleep
[1518-09-08 00:45] wakes up
[1518-10-30 00:02] Guard #1487 begins shift
[1518-10-11 00:51] wakes up
[1518-05-02 00:51] wakes up
[1518-04-04 00:03] Guard #3391 begins shift
[1518-02-10 23:56] Guard #1487 begins shift
[1518-06-27 23:58] Guard #2447 begins shift
[1518-10-31 00:16] falls asleep
[1518-09-25 00:40] wakes up
[1518-09-05 00:37] wakes up
[1518-04-10 00:48] wakes up
[1518-10-04 00:37] wakes up
[1518-04-08 00:00] Guard #2089 begins shift
[1518-02-17 00:06] falls asleep
[1518-06-07 00:07] falls asleep
[1518-04-13 00:42] falls asleep
[1518-10-19 00:50] falls asleep
[1518-06-04 00:05] falls asleep
[1518-04-22 00:03] falls asleep
[1518-05-07 00:14] falls asleep
[1518-10-10 00:40] wakes up
[1518-10-03 00:46] wakes up
[1518-11-04 23:48] Guard #3253 begins shift
[1518-02-23 00:36] wakes up
[1518-10-01 00:57] falls asleep
[1518-03-26 23:50] Guard #2447 begins shift
[1518-08-01 00:17] falls asleep
[1518-06-19 00:19] falls asleep
[1518-10-24 00:42] falls asleep
[1518-07-23 00:54] falls asleep
[1518-04-18 23:56] Guard #619 begins shift
[1518-06-15 00:01] Guard #2089 begins shift
[1518-10-09 00:14] falls asleep
[1518-05-15 00:30] wakes up
[1518-07-05 00:56] wakes up
[1518-05-10 00:32] falls asleep
[1518-05-24 00:25] falls asleep
[1518-09-12 00:27] falls asleep
[1518-11-09 00:32] falls asleep
[1518-06-20 00:02] Guard #619 begins shift
[1518-05-21 23:46] Guard #2389 begins shift
[1518-07-26 23:57] Guard #3391 begins shift
[1518-09-16 23:50] Guard #103 begins shift
[1518-08-12 00:40] wakes up
[1518-04-30 00:00] Guard #3253 begins shift
[1518-02-27 00:59] wakes up
[1518-10-12 00:15] falls asleep
[1518-07-09 00:46] falls asleep
[1518-10-23 00:57] wakes up
[1518-08-17 00:17] falls asleep
[1518-08-16 23:58] Guard #2447 begins shift
[1518-10-22 23:57] Guard #103 begins shift
[1518-02-12 00:04] falls asleep
[1518-06-23 00:37] wakes up
[1518-09-03 00:54] wakes up
[1518-11-17 23:54] Guard #2089 begins shift
[1518-04-27 00:50] wakes up
[1518-09-20 23:52] Guard #103 begins shift
[1518-04-23 00:41] wakes up
[1518-03-20 00:17] falls asleep
[1518-11-12 00:57] wakes up
[1518-07-29 00:47] wakes up
[1518-05-28 00:57] falls asleep
[1518-04-23 23:56] Guard #443 begins shift
[1518-10-15 00:19] falls asleep
[1518-07-14 00:22] wakes up
[1518-05-04 00:58] wakes up
[1518-03-01 00:36] falls asleep
[1518-05-22 00:45] falls asleep
[1518-06-09 00:37] wakes up
[1518-05-22 00:04] falls asleep
[1518-04-07 00:55] wakes up
[1518-06-10 00:40] falls asleep
[1518-03-22 23:56] Guard #1613 begins shift
[1518-05-18 00:10] wakes up
[1518-07-07 00:07] falls asleep
[1518-11-11 00:20] wakes up
[1518-03-30 00:59] wakes up
[1518-02-18 00:08] falls asleep
[1518-03-09 00:02] Guard #443 begins shift
[1518-03-18 00:56] wakes up
[1518-03-30 00:14] falls asleep
[1518-03-06 23:56] Guard #2797 begins shift
[1518-06-28 00:55] wakes up
[1518-08-03 00:04] Guard #443 begins shift
[1518-06-19 00:40] wakes up
[1518-03-14 00:04] Guard #1487 begins shift
[1518-02-21 00:50] wakes up
[1518-08-08 00:03] Guard #1487 begins shift
[1518-10-12 00:55] wakes up
[1518-07-11 00:35] falls asleep
[1518-07-30 00:00] Guard #1373 begins shift
[1518-03-03 00:52] falls asleep
[1518-07-29 00:32] falls asleep
[1518-07-12 00:38] falls asleep
[1518-04-25 00:24] wakes up
[1518-08-02 00:37] wakes up
[1518-10-16 00:56] wakes up
[1518-05-14 00:17] falls asleep
[1518-08-16 00:01] falls asleep
[1518-11-06 00:58] wakes up
[1518-09-15 00:01] Guard #3023 begins shift
[1518-02-11 23:53] Guard #1493 begins shift
[1518-06-02 00:55] wakes up
[1518-06-20 00:22] falls asleep
[1518-06-27 00:57] falls asleep
[1518-02-26 00:26] wakes up
[1518-06-01 00:23] falls asleep
[1518-05-15 00:12] falls asleep
[1518-02-23 00:20] wakes up
[1518-04-06 00:03] Guard #1487 begins shift
[1518-05-11 00:42] wakes up
[1518-04-18 00:01] Guard #2417 begins shift
[1518-06-09 00:02] Guard #641 begins shift
[1518-02-11 00:40] wakes up
[1518-07-12 00:16] falls asleep
[1518-03-09 00:40] falls asleep
[1518-07-01 23:56] Guard #2969 begins shift
[1518-06-26 00:49] falls asleep
[1518-08-19 00:00] Guard #2437 begins shift
[1518-07-27 00:24] wakes up
[1518-09-22 00:02] Guard #2089 begins shift
[1518-09-14 00:21] falls asleep
[1518-09-24 00:24] falls asleep
[1518-06-18 00:45] falls asleep
[1518-09-02 00:22] falls asleep
[1518-05-20 00:24] falls asleep
[1518-04-28 00:03] Guard #1493 begins shift
[1518-09-07 00:26] falls asleep
[1518-04-17 00:28] falls asleep
[1518-07-10 00:00] Guard #619 begins shift
[1518-07-28 00:19] falls asleep
[1518-05-06 23:59] Guard #2089 begins shift
[1518-10-06 00:00] Guard #619 begins shift
[1518-09-19 00:49] wakes up
[1518-09-05 00:48] falls asleep
[1518-10-03 23:57] Guard #641 begins shift
[1518-04-24 00:59] wakes up
[1518-11-17 00:31] falls asleep
[1518-10-02 00:36] wakes up
[1518-09-02 00:37] wakes up
[1518-06-20 00:44] wakes up
[1518-07-25 23:50] Guard #2447 begins shift
[1518-06-08 00:25] wakes up
[1518-04-19 00:26] wakes up
[1518-03-29 23:48] Guard #443 begins shift
[1518-03-11 23:59] Guard #2089 begins shift
[1518-11-01 00:01] falls asleep
[1518-04-24 00:31] falls asleep
[1518-07-07 00:13] wakes up
[1518-07-14 00:52] wakes up
[1518-10-02 00:03] falls asleep
[1518-11-11 00:04] falls asleep
[1518-04-14 00:11] falls asleep
[1518-07-07 00:38] wakes up
[1518-04-14 00:28] falls asleep
[1518-02-26 00:33] falls asleep
[1518-04-05 00:34] wakes up
[1518-02-20 00:15] wakes up
[1518-04-02 00:00] Guard #131 begins shift
[1518-05-23 23:56] Guard #2447 begins shift
[1518-05-25 00:50] wakes up
[1518-10-01 00:04] Guard #1373 begins shift
[1518-03-14 00:41] falls asleep
[1518-07-03 00:46] wakes up
[1518-04-10 00:01] Guard #1487 begins shift
[1518-09-08 00:01] Guard #2797 begins shift
[1518-09-27 23:53] Guard #2447 begins shift
[1518-05-06 00:21] wakes up
[1518-05-24 00:21] wakes up
[1518-07-15 00:48] wakes up
[1518-06-27 00:02] Guard #619 begins shift
[1518-03-18 00:01] falls asleep
[1518-11-10 23:51] Guard #1373 begins shift
[1518-09-14 00:48] wakes up
[1518-05-09 00:58] wakes up
[1518-06-20 00:33] wakes up
[1518-08-19 00:46] wakes up
[1518-02-20 23:49] Guard #2437 begins shift
[1518-05-26 23:56] Guard #1487 begins shift
[1518-08-22 00:13] falls asleep
[1518-06-25 00:55] wakes up
[1518-11-14 00:53] wakes up
[1518-07-12 00:57] wakes up
[1518-09-30 00:34] falls asleep
[1518-08-09 00:00] falls asleep
[1518-04-13 23:57] Guard #619 begins shift
[1518-08-15 23:50] Guard #3391 begins shift
[1518-06-26 00:33] falls asleep
[1518-08-07 00:00] Guard #1613 begins shift
[1518-04-08 00:49] wakes up
[1518-06-07 23:56] Guard #2417 begins shift
[1518-05-12 00:59] wakes up
[1518-03-14 00:30] falls asleep
[1518-02-27 00:48] falls asleep
[1518-09-03 23:53] Guard #2417 begins shift
[1518-04-20 00:53] wakes up
[1518-09-29 00:46] wakes up
[1518-09-10 00:30] falls asleep
[1518-09-01 23:57] Guard #103 begins shift
[1518-10-09 00:00] Guard #1487 begins shift
[1518-08-29 00:57] wakes up
[1518-04-16 00:17] falls asleep
[1518-03-12 00:22] wakes up
[1518-06-10 00:01] falls asleep
[1518-05-21 00:02] Guard #2417 begins shift
[1518-03-30 00:21] wakes up
[1518-05-17 00:00] Guard #1373 begins shift
[1518-08-28 23:50] Guard #1613 begins shift
[1518-06-17 00:01] Guard #2417 begins shift
[1518-04-04 23:58] Guard #641 begins shift
[1518-09-04 00:53] wakes up
[1518-10-11 00:35] wakes up
[1518-10-30 23:57] Guard #103 begins shift
[1518-06-03 00:38] wakes up
[1518-11-03 23:59] Guard #2417 begins shift
[1518-03-21 23:58] Guard #2797 begins shift
[1518-08-10 00:48] wakes up
[1518-03-03 00:36] falls asleep
[1518-10-18 00:09] falls asleep
[1518-05-14 23:56] Guard #641 begins shift
[1518-03-06 00:43] wakes up
[1518-02-25 00:00] Guard #2389 begins shift
[1518-02-21 00:03] falls asleep
[1518-08-03 00:42] wakes up
[1518-11-05 00:42] falls asleep
[1518-08-28 00:21] falls asleep
[1518-11-02 00:00] Guard #131 begins shift
[1518-11-12 00:50] falls asleep
[1518-02-28 00:57] wakes up
[1518-07-16 00:51] wakes up
[1518-02-26 23:54] Guard #619 begins shift
[1518-05-31 00:15] falls asleep
[1518-02-24 00:05] falls asleep
[1518-09-30 00:52] falls asleep
[1518-08-30 00:34] falls asleep
[1518-03-18 23:47] Guard #641 begins shift
[1518-05-27 00:32] falls asleep
[1518-07-27 00:10] falls asleep
[1518-06-17 00:43] falls asleep
[1518-08-29 00:41] falls asleep
[1518-07-22 00:34] falls asleep
[1518-07-16 00:46] falls asleep
[1518-06-28 23:59] Guard #1613 begins shift
[1518-10-12 00:49] wakes up
[1518-04-07 00:45] falls asleep
[1518-04-12 00:58] wakes up
[1518-04-09 00:56] wakes up
[1518-07-03 00:20] falls asleep
[1518-04-12 00:18] falls asleep
[1518-07-11 23:58] Guard #1493 begins shift
[1518-11-13 00:59] wakes up
[1518-02-24 00:42] wakes up
[1518-02-13 00:52] falls asleep
[1518-07-21 00:41] falls asleep
[1518-08-23 00:02] Guard #619 begins shift
[1518-04-15 00:04] Guard #641 begins shift
[1518-09-16 00:54] wakes up
[1518-07-20 23:48] Guard #2089 begins shift
[1518-05-31 00:51] falls asleep
[1518-07-04 00:51] wakes up
[1518-03-12 00:47] falls asleep
[1518-06-12 00:55] wakes up
[1518-05-05 00:40] falls asleep
[1518-09-08 00:35] wakes up
[1518-05-04 00:50] falls asleep
[1518-06-21 00:13] falls asleep
[1518-11-06 00:03] Guard #2389 begins shift
[1518-09-07 00:00] Guard #1033 begins shift
[1518-06-25 00:46] falls asleep
[1518-05-11 00:00] Guard #2437 begins shift
[1518-05-01 00:36] falls asleep
[1518-03-04 00:38] wakes up
[1518-10-27 00:55] falls asleep
[1518-04-14 00:16] wakes up
[1518-02-14 00:36] falls asleep
[1518-07-09 00:51] wakes up
[1518-10-01 00:15] falls asleep
[1518-03-16 00:23] falls asleep
[1518-05-30 00:59] wakes up
[1518-03-25 00:56] wakes up
[1518-05-12 00:49] falls asleep
[1518-05-22 00:58] wakes up
[1518-04-01 00:09] falls asleep
[1518-08-07 00:58] wakes up
[1518-09-13 00:49] falls asleep
[1518-05-13 23:59] Guard #131 begins shift
[1518-09-16 00:46] falls asleep
[1518-11-11 00:58] wakes up
[1518-06-13 00:23] falls asleep
[1518-03-25 00:03] Guard #1487 begins shift
[1518-08-13 00:53] wakes up
[1518-09-07 00:53] wakes up
[1518-07-10 00:32] falls asleep
[1518-03-25 23:57] Guard #3023 begins shift
[1518-10-25 00:57] wakes up
[1518-08-26 00:00] Guard #2089 begins shift
[1518-03-06 00:38] wakes up
[1518-02-12 00:43] wakes up
[1518-03-21 00:18] falls asleep
[1518-06-21 00:00] Guard #2437 begins shift
[1518-10-01 23:49] Guard #2797 begins shift
[1518-09-13 23:56] Guard #1033 begins shift
[1518-07-14 00:07] falls asleep
[1518-09-26 00:56] wakes up
[1518-05-17 00:55] wakes up
[1518-09-12 00:41] wakes up
[1518-03-15 00:15] wakes up
[1518-03-01 00:04] Guard #3253 begins shift
[1518-03-28 00:57] wakes up
[1518-04-02 00:16] wakes up
[1518-07-20 00:00] Guard #131 begins shift
[1518-04-09 00:42] falls asleep
[1518-09-18 00:06] falls asleep
[1518-04-11 23:54] Guard #2089 begins shift
[1518-04-20 23:56] Guard #3253 begins shift
[1518-06-16 00:00] Guard #131 begins shift
[1518-05-21 00:18] falls asleep
[1518-09-01 00:51] wakes up
[1518-05-12 00:34] wakes up
[1518-06-24 00:09] falls asleep
[1518-02-27 23:59] Guard #1613 begins shift
[1518-02-25 00:11] falls asleep
[1518-03-14 00:45] wakes up
[1518-09-21 00:00] falls asleep
[1518-05-20 00:37] wakes up
[1518-05-27 23:47] Guard #1373 begins shift
[1518-04-17 00:46] wakes up
[1518-10-11 00:02] Guard #1033 begins shift
[1518-11-09 23:56] Guard #1487 begins shift
[1518-03-27 00:16] wakes up
[1518-03-07 00:53] wakes up
[1518-04-01 00:45] wakes up
[1518-09-24 00:02] Guard #1033 begins shift
[1518-08-17 00:47] wakes up
[1518-03-14 00:37] wakes up
[1518-05-30 00:13] falls asleep
[1518-02-19 23:50] Guard #3391 begins shift
[1518-08-17 00:58] wakes up
[1518-05-22 00:28] wakes up
[1518-05-29 00:54] falls asleep
[1518-03-13 00:03] Guard #131 begins shift
[1518-07-26 00:06] wakes up
[1518-11-10 00:56] wakes up
[1518-06-17 00:24] wakes up
[1518-09-27 00:37] wakes up
[1518-05-05 00:57] wakes up
[1518-05-29 23:56] Guard #2089 begins shift
[1518-04-15 00:31] falls asleep
[1518-09-04 00:01] falls asleep
[1518-03-30 00:25] falls asleep
[1518-06-14 00:55] wakes up
[1518-07-31 00:01] Guard #1493 begins shift
[1518-06-10 00:57] wakes up
[1518-02-13 00:58] wakes up
[1518-04-21 00:36] falls asleep
[1518-02-23 00:02] Guard #1493 begins shift
[1518-10-19 00:46] wakes up
[1518-04-18 00:53] wakes up
[1518-03-15 23:58] Guard #1493 begins shift
[1518-02-20 00:01] falls asleep
[1518-04-21 23:51] Guard #3391 begins shift
[1518-03-08 00:00] Guard #1487 begins shift
[1518-08-02 00:21] falls asleep
[1518-08-09 23:58] Guard #1613 begins shift
[1518-03-11 00:01] Guard #3253 begins shift
[1518-03-06 00:42] falls asleep
[1518-02-13 00:47] wakes up
[1518-07-08 23:53] Guard #103 begins shift
[1518-09-27 00:01] Guard #1493 begins shift
[1518-11-02 23:56] Guard #2447 begins shift
[1518-06-14 00:02] Guard #3023 begins shift
[1518-03-05 00:29] wakes up
[1518-07-08 00:29] falls asleep
[1518-03-02 00:31] falls asleep
[1518-07-27 00:38] falls asleep
[1518-05-21 00:59] wakes up
[1518-05-11 00:10] falls asleep
[1518-03-26 00:45] wakes up
[1518-07-18 23:59] Guard #1973 begins shift
[1518-04-26 23:57] Guard #2389 begins shift
[1518-11-04 00:54] wakes up
[1518-03-14 23:57] Guard #1033 begins shift
[1518-07-17 00:19] falls asleep
[1518-10-05 00:55] wakes up
[1518-03-22 00:58] wakes up
[1518-09-30 00:00] Guard #2417 begins shift
[1518-07-02 00:53] falls asleep
[1518-10-01 00:59] wakes up
[1518-05-01 00:04] Guard #3253 begins shift
[1518-07-22 00:47] wakes up
[1518-06-18 00:04] Guard #619 begins shift
[1518-10-19 00:01] Guard #1487 begins shift
[1518-11-23 00:36] wakes up
[1518-06-06 00:56] wakes up
[1518-11-20 00:04] Guard #2389 begins shift
[1518-06-28 00:35] falls asleep
[1518-10-18 00:02] Guard #2447 begins shift
[1518-10-26 00:28] falls asleep
[1518-02-28 00:50] falls asleep
[1518-11-07 23:56] Guard #1373 begins shift
[1518-05-15 23:59] Guard #443 begins shift
[1518-08-03 00:57] wakes up
[1518-07-04 00:55] falls asleep
[1518-07-27 00:41] wakes up
[1518-03-12 00:43] wakes up
[1518-03-26 00:55] wakes up
[1518-02-14 00:01] Guard #2389 begins shift
[1518-10-23 00:25] falls asleep
[1518-07-16 00:38] wakes up
[1518-08-06 00:36] wakes up
[1518-06-03 00:30] falls asleep
[1518-07-25 00:56] wakes up
[1518-03-19 00:42] wakes up
[1518-05-26 00:02] Guard #641 begins shift
[1518-10-28 00:42] wakes up
[1518-07-18 00:46] falls asleep
[1518-02-20 00:25] falls asleep
[1518-07-01 00:58] wakes up
[1518-04-14 00:57] wakes up
[1518-10-20 00:20] falls asleep
[1518-05-08 00:00] Guard #2683 begins shift
[1518-07-15 00:31] falls asleep
[1518-09-06 00:42] wakes up
[1518-06-11 00:37] falls asleep
[1518-09-08 00:38] falls asleep
[1518-08-08 00:37] falls asleep
[1518-03-29 00:18] wakes up
[1518-03-31 00:15] falls asleep
[1518-06-03 23:51] Guard #2417 begins shift
[1518-07-12 23:48] Guard #443 begins shift
[1518-06-26 00:58] wakes up
[1518-10-17 00:35] falls asleep
[1518-07-21 00:46] wakes up
[1518-08-14 23:58] Guard #1373 begins shift
[1518-05-31 00:54] wakes up
[1518-10-11 00:43] falls asleep
[1518-07-13 00:03] falls asleep
[1518-05-13 00:37] wakes up
[1518-04-28 00:12] falls asleep
[1518-02-22 00:23] falls asleep
[1518-08-24 23:49] Guard #1487 begins shift
[1518-04-13 00:01] Guard #1493 begins shift
[1518-06-05 23:56] Guard #2437 begins shift
[1518-08-25 00:04] falls asleep
[1518-04-18 00:24] falls asleep
[1518-11-05 00:48] wakes up
[1518-10-22 00:26] falls asleep
[1518-10-31 00:41] wakes up
[1518-10-30 00:41] wakes up
[1518-06-05 00:56] wakes up
[1518-11-17 00:01] Guard #2437 begins shift
[1518-11-13 00:02] Guard #2389 begins shift
[1518-11-11 00:37] falls asleep
[1518-05-03 00:59] wakes up
[1518-07-09 00:11] wakes up
[1518-10-21 00:36] wakes up
[1518-02-14 23:52] Guard #3391 begins shift
[1518-10-13 00:21] falls asleep
[1518-04-23 00:04] Guard #3253 begins shift
[1518-10-29 00:53] wakes up
[1518-03-27 23:59] Guard #3253 begins shift
[1518-09-15 00:31] falls asleep
[1518-03-02 00:44] wakes up
[1518-10-07 00:52] wakes up
[1518-06-16 00:50] wakes up
[1518-03-20 23:57] Guard #1033 begins shift
[1518-06-28 00:18] falls asleep
[1518-09-10 00:03] Guard #1613 begins shift
[1518-08-01 00:04] Guard #3391 begins shift
[1518-04-03 00:48] wakes up
[1518-06-21 00:42] wakes up
[1518-08-07 00:11] falls asleep
[1518-03-25 00:21] falls asleep
[1518-08-17 00:56] falls asleep
[1518-08-14 00:04] Guard #1373 begins shift
[1518-10-05 00:09] falls asleep
[1518-06-09 00:50] wakes up
[1518-04-16 23:56] Guard #3391 begins shift
[1518-10-16 23:59] Guard #2437 begins shift
[1518-08-10 00:59] wakes up
[1518-03-22 00:23] falls asleep
[1518-11-03 00:54] wakes up
[1518-08-27 00:01] Guard #1373 begins shift
[1518-05-28 00:53] falls asleep
[1518-08-15 00:30] falls asleep
[1518-08-25 00:52] wakes up
[1518-11-07 00:00] Guard #1493 begins shift
[1518-07-03 00:00] Guard #443 begins shift
[1518-11-14 00:38] falls asleep
[1518-05-31 00:00] Guard #2437 begins shift
[1518-08-04 00:24] wakes up
[1518-09-22 00:55] wakes up
[1518-04-17 00:21] wakes up
[1518-05-27 00:58] wakes up
[1518-11-22 00:05] falls asleep
[1518-05-24 00:08] falls asleep
[1518-11-19 00:00] Guard #1613 begins shift
[1518-05-18 00:57] falls asleep
[1518-03-17 23:50] Guard #1373 begins shift
[1518-03-01 00:41] falls asleep
[1518-08-30 00:00] Guard #103 begins shift
[1518-07-25 00:27] wakes up
[1518-05-18 00:58] wakes up
[1518-04-30 00:59] wakes up
[1518-10-24 00:39] wakes up
[1518-03-26 00:35] wakes up
[1518-02-23 23:53] Guard #2447 begins shift
[1518-11-12 00:00] Guard #1033 begins shift
[1518-07-21 23:58] Guard #1493 begins shift
[1518-11-23 00:04] Guard #2969 begins shift
[1518-06-18 00:54] wakes up
[1518-08-08 00:18] falls asleep
[1518-04-08 00:39] falls asleep
[1518-08-06 00:42] falls asleep
[1518-02-15 00:20] falls asleep
[1518-10-07 00:28] falls asleep
[1518-08-24 00:25] wakes up
[1518-04-26 00:24] wakes up
[1518-06-22 00:44] wakes up
[1518-03-30 00:41] wakes up
[1518-04-04 00:42] falls asleep
[1518-07-08 00:56] wakes up
[1518-10-28 00:17] falls asleep
[1518-10-30 00:53] wakes up
[1518-08-08 00:57] wakes up
[1518-11-09 00:00] Guard #2389 begins shift
[1518-08-29 00:09] wakes up
[1518-03-06 00:00] Guard #1613 begins shift
[1518-03-01 00:37] wakes up
[1518-05-22 23:57] Guard #131 begins shift
[1518-03-06 00:11] falls asleep
[1518-08-30 00:49] wakes up
[1518-04-17 00:17] falls asleep
[1518-06-30 00:50] wakes up
[1518-09-24 00:51] wakes up
[1518-10-12 00:02] Guard #619 begins shift
[1518-06-10 23:58] Guard #619 begins shift
[1518-05-11 23:56] Guard #2389 begins shift
[1518-08-07 00:52] falls asleep
[1518-07-16 23:58] Guard #1493 begins shift
[1518-07-01 00:17] falls asleep
[1518-04-23 00:46] falls asleep
[1518-08-12 00:33] falls asleep
[1518-10-26 00:04] Guard #131 begins shift
[1518-11-23 00:30] falls asleep
[1518-10-02 23:59] Guard #2969 begins shift
[1518-09-30 00:49] wakes up
[1518-03-24 00:30] falls asleep
[1518-03-10 00:29] wakes up
[1518-02-19 00:09] falls asleep
[1518-09-05 00:58] wakes up
[1518-03-17 00:08] falls asleep
[1518-11-19 00:59] wakes up
[1518-06-08 00:36] falls asleep
[1518-03-30 00:02] falls asleep
[1518-03-01 00:51] wakes up
[1518-05-18 00:52] wakes up
[1518-09-08 23:53] Guard #131 begins shift
[1518-07-25 00:32] falls asleep
[1518-11-02 00:13] falls asleep
[1518-11-21 23:46] Guard #2969 begins shift
[1518-07-30 00:26] falls asleep
[1518-10-14 00:54] wakes up
[1518-08-20 00:18] falls asleep
[1518-11-16 00:56] falls asleep
[1518-04-21 00:53] wakes up
[1518-03-09 00:57] wakes up
[1518-09-17 00:42] wakes up
[1518-05-25 00:54] falls asleep
[1518-05-19 00:28] falls asleep
[1518-06-29 00:13] falls asleep
[1518-11-19 00:07] falls asleep
[1518-04-29 00:55] wakes up
[1518-07-11 00:03] Guard #103 begins shift
[1518-11-01 00:47] wakes up
[1518-07-04 23:53] Guard #2797 begins shift
[1518-02-13 00:25] falls asleep
[1518-10-06 00:41] wakes up
[1518-04-04 00:39] wakes up
[1518-06-16 00:18] wakes up
[1518-06-12 00:35] wakes up
[1518-05-31 00:44] wakes up
[1518-08-05 00:14] falls asleep
[1518-09-09 00:00] falls asleep
[1518-03-23 00:35] falls asleep
[1518-07-04 00:56] wakes up
[1518-05-19 23:50] Guard #2447 begins shift
[1518-08-23 23:48] Guard #131 begins shift
[1518-10-11 00:33] falls asleep
[1518-03-25 00:44] falls asleep
[1518-10-27 00:08] falls asleep
[1518-03-15 00:12] falls asleep
[1518-06-14 00:36] falls asleep
[1518-09-26 00:18] wakes up
[1518-08-05 00:54] wakes up
[1518-05-28 00:59] wakes up
[1518-07-26 00:01] falls asleep
[1518-09-10 00:53] wakes up
[1518-03-04 00:01] falls asleep
[1518-03-20 00:00] Guard #641 begins shift
[1518-10-27 00:00] Guard #443 begins shift
[1518-03-23 00:52] falls asleep
[1518-07-06 23:57] Guard #3391 begins shift
[1518-06-07 00:44] falls asleep
'''
)