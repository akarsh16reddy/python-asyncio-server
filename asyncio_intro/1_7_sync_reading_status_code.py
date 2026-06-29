import requests
import time

# Output:
# 200
# 200
# Running synchronously took 0.2621 seconds.

def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)

sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Running synchronously took {sync_end - sync_start:.4f} seconds.')
