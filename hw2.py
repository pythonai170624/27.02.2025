import numpy as np
import time
from memory_profiler import profile


def light_computation(size=1000):
    """This function doesn't use much memory."""
    result = 0
    for i in range(size):
        result += i * 2
    return result


def create_small_list(size=1000):
    """This function creates a reasonably small list."""
    return [i ** 2 for i in range(size)]


def calc_log_function(size=100000000):
    """This function creates a large NumPy array in memory."""
    # Create a large array
    large_array = np.random.random((size,))
    # Do some operations on it
    processed = large_array * 2
    transformed = np.log(processed + 1)
    # Simulate some processing time
    time.sleep(1)
    return transformed


def another_function(n=10):
    """Another function that doesn't use much memory."""
    return {i: i ** 3 for i in range(n)}