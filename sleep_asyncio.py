import asyncio
from time import time


async def sleeper(name, delay):
    await asyncio.sleep(delay)
    print(f"[{name}] Woke up after {delay} seconds")


async def main():
    start_time = time()
    tasks = [
        asyncio.create_task(sleeper(f"Task-{i+1}", d))
        for i, d in enumerate([5, 3, 4, 2])
    ]

    print(f"Main coroutine is free to do other work. 5 + 6 is {5+6}")

    # Wait for all tasks to finish
    await asyncio.gather(*tasks)
    print(f"All tasks finished in {time() - start_time:.2f} seconds")


# Run the main coroutine
asyncio.run(main())
