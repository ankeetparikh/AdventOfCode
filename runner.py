import subprocess, resource
print("Hello! This is a program for running my advent of code solutions!")

def run_and_get_stats(day):

  filename = f"2015/python/day{i:02d}.py"

  usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
  subprocess.run([
    "python3", 
    filename, 
    f"--input-location=2015/inputs/day{i:02d}input.txt"
  ])

  usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)
  cpu_time = usage_end.ru_utime - usage_start.ru_utime

  return {
    "filename": filename,
    "duration": cpu_time
  }

readme = """
| Day      | Python |
| -------- | -------|"""

for i in range(1, 26):
  print("doing day", i)
  stats = run_and_get_stats(i)
  readme += f"\n| {i} | [{stats['duration']:0.2f} s]({stats['filename']}) |"

print(readme)