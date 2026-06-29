import requests
import threading
import time

# Output:
# All threads running!
# 200
# 200
# Running through threads took 0.1426 seconds.

def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)

thread_start = time.time()

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_1.start()
thread_2.start()

print('All threads running!')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f'Running through threads took {thread_end - thread_start:.4f} seconds.')
