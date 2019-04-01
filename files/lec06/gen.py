from memory_profiler import profile

@profile
def my_func():
    total_sum = 0
    for v in range(10 ** 6):
        total_sum += v
    return total_sum

if __name__ == '__main__':
    my_func()
