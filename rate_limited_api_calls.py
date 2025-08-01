import requests
import time

url = "https://ecommerce-playground.lambdatest.io/index.php?route=common/home"
max_retries = 5
backoff = 1  # initial wait in seconds

for attempt in range(1, max_retries + 1):
    try:
        print(f"Attempt {attempt}...")
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("Request successful!")
            break
        else:
            print(f"Failed with status: {response.status_code}")
            raise Exception("Non-200 status")

    except Exception as e:
        print(f"Error: {e}")

        if attempt < max_retries:
            wait_time = backoff * (2 ** (attempt - 1))
            print(f"Retrying in {wait_time} seconds...\n")
            time.sleep(wait_time)
        else:
            print("Max retries reached. Giving up.")
