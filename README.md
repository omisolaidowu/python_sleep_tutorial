# Python `time.sleep()` Tutorial

This project is a hands-on tutorial demonstrating various use cases of Python's `time.sleep()` function. Each script showcases a different scenario where introducing delays is useful, such as simulating user wait times, handling dynamic content, rate-limiting API calls, and synchronizing with external resources.

## Project Structure

## Scripts Overview

- **delaying_between_steps.py**: Demonstrates adding delays between Selenium automation steps.
- **delaying_script_execution.py**: Waits for external scripts/resources to load before interacting with elements.
- **dynamic_content.py**: Simulates waiting for dynamic content with a hard-coded sleep.
- **rate_limited_api_calls.py**: Implements exponential backoff for retrying API calls.
- **real_time_data_processing.py**: Mimics real-time data arrival with random delays.
- **simulating_user_wait.py**: Adds random delays to simulate human interaction.
- **sleep_asyncion.py**: Shows how to use `asyncio.sleep()` for asynchronous tasks.
- **sleep_thread.py**: Demonstrates sleeping in multiple threads.
- **system_resource.py**: Periodically checks and prints system resource usage.
- **test_behavior.py**: Observes page transitions and delays in Selenium.
- **waiting_for_external_resources.py**: Waits for a file to be created before proceeding.

## How to Use

Each script is self-contained and can be run independently. Make sure you have the required dependencies installed (e.g., `selenium`, `psutil`, `requests`). Run any script using:

```sh
python <script_name>.py
```
