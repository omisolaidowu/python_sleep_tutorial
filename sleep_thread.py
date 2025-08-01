import threading
from time import sleep, time


def sleeper(name, delay):
    sleep(delay)
    print(f"[{name}] Woke up after {delay} seconds")


threads = [
    threading.Thread(target=sleeper, args=(f"Thread-{i+1}", d))
    for i, d in enumerate([5, 3, 4, 2])
]

start_time = time()
for t in threads:
    t.start()

print(f"Main thread is free to do other work. 5 + 6 is {5+6}")


# Wait for threads to finish, if needed
for t in threads:
    t.join()

print(f"All threads finished in {time() - start_time:.2f} seconds")
