import os
import time

file_path = "output.csv"
timeout = 30
start_time = time.time()

while not os.path.exists(file_path):
    if time.time() - start_time > timeout:
        print("Timeout reached. File not found.")
        break
    print("Waiting for file to be created...")
    time.sleep(2)

if os.path.exists(file_path):
    print("File is now available!")
    # Take further actions
