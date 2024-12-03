import importlib
from time import perf_counter


NUM_DAYS = 14

day_info = {}

for i in range(1, NUM_DAYS + 1):
	print(f"~~~~~Day {i}~~~~~")
	start = perf_counter()
	importlib.import_module(f"day{i}")
	elapsed = perf_counter() - start

	print(f"Day {i} time(s): {elapsed:.9f}")
	day_info[i] = {
		'time': elapsed
	}
	print("~~~~~~~~")
total_time = sum(d['time'] for d in day_info.values())

print("Advent of Code 2022 Summarized Results!")
print("Day    Time(s)")
for i in range(1, NUM_DAYS + 1):
	print(f"{str(i).zfill(2)}     {day_info[i]['time']:.9f}")

print(f"Total time(s): {total_time: .9f}" )
