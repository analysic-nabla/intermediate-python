from memory_profiler import profile

@profile
def sum_10_10():
    val = sum(list(range(10 ** 10)))
    return val

if __name__ == "__main__":
    sum_10_10()
