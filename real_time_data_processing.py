import time
import random

for i in range(10):
    # Random temperature
    temp = round(random.uniform(20.0, 30.0), 2)
    print(f"Reading {i + 1}: {temp}\u00b0C")
    # Random delays to simulate real-time data arrival
    time.sleep(random.uniform(1.5, 4))
