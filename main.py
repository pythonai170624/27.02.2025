# Garbage collector
# Managed
################################## 1
import sys

def getcount(z):
    pass
z = []  # 100
getcount(z)  # 100

print('1' * 100)
a = [1] * 100  # create an empty list
# Note: getrefcount returns one extra count because the argument is passed as a temporary reference.
print("Reference count for a:", sys.getrefcount(a))
b = a
print('id a = ', id(a))
print('id b = ', id(b))
print("Reference count for a:", sys.getrefcount(a))
del a
print("Reference count for b:", sys.getrefcount(b))
del b


################################## 3
print('3' * 100)
import gc


def do_work(list1):
    # [2]
    print(len(list1))

l1 = [1] * 10_000_000  # [1]
do_work(l1)
# [1]
del l1  # [0]
x = 12
print("Garbage Collector counts:", gc.get_count())
gc.collect()
print("Garbage Collector counts:", gc.get_count())

print(gc.get_threshold())
#   0    1   2
# 700 , 10, 10
class A:
    def __init__(self):
        self.ref = None

a1 = A()
a2 = A()
a1.ref = a2  # Create a cycle
a2.ref = a1

del a1, a2  # Remove external references, but the cycle remains


l2 = [1] * 1000
print(gc.get_count())
print("Before GC:", gc.get_count())  # Creates new Gen 0 objects
print("After One More Print:", gc.get_count())  # Number in Gen 0 increased
collected = gc.collect()  # Run GC
print("After GC:", gc.get_count(), collected)  # Now should be (0,0,0)

#print(l2)
# print("gc.get_objects()", gc.get_objects())

tracked_objects = gc.get_referents(l2)

# Count them
print(f"Number of tracked objects: {tracked_objects}")


# gc.set_threshold(1500, 5, 5)