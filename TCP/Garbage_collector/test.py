# import sys

# referbence count
# x = [1, 2, 3]
# print(sys.getrefcount(x))
# y = x
# print(sys.getrefcount(x))
# y = None
# print(sys.getrefcount(x))
# print(sys.getrefcount(y))

# circular_ref
# x = [1, 2, 3]
# y = [4, 5, 6]
# x.append(y)
# y.append(x)
# print()
# print(sys.getrefcount(x))
# print(sys.getrefcount(y))

# generations
# import gc
# print(gc.get_threshold())
# print(gc.get_count())

# MARK and sweep method for garbage collection algo
import gc
gc.disable()
print(gc.collect(generation=0))
print(gc.get_threshold())
print(gc.get_count())
