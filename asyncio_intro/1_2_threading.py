import os
import threading

print(f'Python process running with pid: {os.getpid()}')

total_thread_count = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python is currently running {total_thread_count} thread(s)')
print(f'The current thread is {thread_name}')

