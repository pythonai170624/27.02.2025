################################## 1
import sys

print('1' * 100)
a = []  # create an empty list
# Note: getrefcount returns one extra count because the argument is passed as a temporary reference.
print("Reference count for a:", sys.getrefcount(a))
b = a
print('id a = ', id(a))
print('id b = ', id(b))
print("Reference count for a:", sys.getrefcount(a))
del a
print("Reference count for b:", sys.getrefcount(b))


################################## 2
print('2' * 100)
import sys

a = [1, 2, 3, 4, 5]
print("Size of a:", sys.getsizeof(a), "bytes")
# Explanation:
# This code shows the size (in bytes) of a list.
# Note that the size reported is for the list container itself (the pointers)
# and not for the objects contained within.

import sys

a = [1, 2, 3, 4, [1] * 100000]

# Size of the list container (just the pointers, not the objects)
container_size = sys.getsizeof(a)

# Size of the individual elements (the objects in the list)

elements_sizes = [sys.getsizeof(item) for item in a]
total_elements_size = sum(elements_sizes)

print("Container size of 'a':", container_size, "bytes")
print("Sizes of individual elements:", elements_sizes)
print("Total size of all elements:", total_elements_size, "bytes")
print("Approximate total size (container + elements):", container_size + total_elements_size, "bytes")


################################## 3
print('3' * 100)
import gc

print("Garbage Collector counts:", gc.get_count())
gc.collect()
print("Garbage Collector counts:", gc.get_count())



# Explanation:
# This gives you a tuple showing the number of objects in each generation.
# The GC uses these counts to decide when to run a collection cycle.

# In summary, the 533 objects in generation 0 are created by Python itself
# during initialization and module loading, not necessarily by your explicit code.


################################## 4
print('4' * 100)
import gc

class A:
    pass

class B:
    pass

def fun1():
    a = A()
    b = B()
    a.next = a
    b.next = b

fun1()

print("Forcing garbage collection...")
unreachable = gc.collect()
print("Unreachable objects collected:", unreachable)
print("Garbage Collector counts after collection:", gc.get_count())


################################## 5
print('5' * 100)

import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.other = None

# Create a circular reference:
a = Node(1)
b = Node(2)
a.other = b
b.other = a

# Remove external references:
del a, b

print("Forcing garbage collection on circular references...")
print("Garbage Collector counts before collection:", gc.get_count())
circlue = gc.collect()
print("Circular references collected:", circlue)
print("Garbage Collector counts after collection:", gc.get_count())

# Explanation:
# This example creates two objects that reference each other.
# Even though they form a cycle, Python’s GC can eventually collect them when forced.


######################## 6
print('6' * 100)
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.other = None

a = Node(1)
b = Node(2)
# Use weak references to avoid strong circular reference:
a.other = weakref.ref(b)
b.other = weakref.ref(a)

# Accessing the weakly-referenced object:
print("b via a.other:", a.other())
print("a via b.other:", b.other())

# In summary, while the GC is effective at cleaning up cycles,
# weak references give you an explicit way to manage object lifetimes
# and dependencies, reducing the risk of accidental
# memory retention and addressing cases


######################## 7
print('7' * 100)

leak_list = []

class Leaky:
    def __init__(self, value):
        self.value = value

def create_leak():
    for i in range(10000):
        leak_list.append(Leaky(i))

print("Starting memory leak demonstration...")
create_leak()
print("Number of leaked objects:", len(leak_list))

print(len(gc.get_referents(leak_list)))
print(gc.get_count())
gc.collect()
print(gc.get_count())
print(len(gc.get_referents(leak_list)))


# Explanation:
# The global list leak_list holds references to many Leaky objects,
# preventing them from being garbage collected and simulating a memory leak.


################## 8
print('8' * 100)

from memory_profiler import profile

# Run this example with: mprof run memory_example.py
@profile
def create_large_list():
    a = [i for i in range(1000)]  # this is 4MB, increase to 20000 and see 8MB
  # this is 4MB, increase to 20000 and see 8MB
    print(4)
    return a

b = create_large_list()


################################## 9
import sys

def x():
    pass
print('9' * 100)
import objgraph

# Create some objects and relationships:
a = [1, 2, 3]
b = {'key': [1]*1_000_00000}
c = [a, 1]

# Show the most common types in memory:
import objgraph
objgraph.show_most_common_types(limit=10)

# Explanation:
# This code uses objgraph to display the five most common
# types of objects currently in memory.
# It’s a good way to start exploring where your objects
# are and if unexpected objects are hanging around.


# gen 1


print('*' * 200)

import gc

# Make sure garbage collection is enabled
gc.enable()

# Create a circular reference that will need the GC
def create_cycle():
    x = {}
    x['self'] = x  # circular reference
    return x

# Force all existing tracked objects to be collected
# to start with a clean state
gc.collect()
print("After initial collection:", gc.get_count())

# Create some cycles that will be tracked by the GC
cycles = [create_cycle() for _ in range(10)]
print("After creating cycles:", gc.get_count())

# Collect only generation 0
# This will move surviving objects to generation 1
gc.collect(0)  # Only collect generation 0
print("After gen 0 collection:", gc.get_count())

# Create some more cycles
more_cycles = [create_cycle() for _ in range(5)]
print("After creating more cycles:", gc.get_count())

# Full collection to see final state
full_collected = gc.collect()
print("After full collection:", gc.get_count(), "collected:", full_collected)