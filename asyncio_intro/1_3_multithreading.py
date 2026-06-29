import threading

# Methods covered
# 1. active_count
# 2. current_thread().name
# 3. join
# 4. start

def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}!')

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python is currently running {total_threads} threads(s)')
print(f'The current thread is {thread_name}')

hello_thread.join()
