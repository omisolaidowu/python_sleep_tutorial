import time
import psutil
import os

# Monitor current Python process
pid = os.getpid()
process = psutil.Process(pid)

# Calculation code
a = 4 + 8
print(a)

# Check memory after calculation
memory_info = process.memory_info()
memory_mb = memory_info.rss / 1024 / 1024
print(f"Memory after calculation: {memory_mb:.2f} MB")

# Continue monitoring
for i in range(5):
    memory_info = process.memory_info()
    # Convert to MB
    memory_mb = memory_info.rss / 1024 / 1024
    print(f"Memory Usage: {memory_mb:.2f} MB")
    # Check every 2 seconds
    time.sleep(2)
