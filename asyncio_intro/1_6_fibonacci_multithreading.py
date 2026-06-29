import threading
import time

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

def fib_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))
   
    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()

if __name__ == "__main__":
    start_threads = time.time()

    fib_with_threads()

    end_threads = time.time()

    print(f'Threads took {end_threads - start_threads:.4f} seconds.')
