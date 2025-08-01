import random
import time


# Simulate dynamic content that loads randomly between 1-4 seconds
def content_ready():
    return time.time() - start_time >= load_time


# Hard wait with time.sleep()
print("HARD WAIT")
start_time = time.time()
load_time = random.uniform(1, 4)

print("Waiting 5 seconds for content...")
# Always waits 5 seconds
time.sleep(5)
print(f"Content loaded! (It took {load_time:.1f}s)")
