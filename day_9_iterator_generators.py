# difference between iterator and iterables
# Iterables? which can be looped list will have __iter__. Can be looped infinite amount of times. Doesn't know where I am in loop
# Iterator will have __next__ and __iter__. Can only be looped once. They know where they are in the loop


nums = [5, 10, 20]


# there is a dunder method called __iter__

print(nums)
print(dir(nums))  # gives all methods including dunder
nums_iter = nums.__iter__()  # convert to iterator but this way is frowned upon.
nums_iter1 = iter(nums)  # this is a better way

print(nums_iter)
print(nums_iter1)
print(dir(nums_iter1))  # __next__ & __iter__

# conclusion
# All iterators are iterables but not the other way around

# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter)) # Can't have more coz you can only loop an iterable once
# print(next(nums_iter))

# Create an iterator and loop it with while loop


def main():
    try:
        names = ["alex", "gemma", "caleb"]
        name_iter = iter(names)
        while True:
            print(next(name_iter))
    except StopIteration:
        print("Iterator is completed")

    nums_iter2 = iter([80, 90, 100])
    for num in nums_iter2:
        print(num)

    # range(0, 100_000_000, 1)    #(start, end, skip) List with 100 000 000 values it'll occupy a lot in memory. but iterators wont take a lot of memory because it remembers one thing at a time
    # Create own iterator
    class MyRange:
        def __init__(self, start, end):
            self.current = start
            self.end = end

        def __iter__(self):  # just returning self because its already an iterator
            return self

        def __next__(self):
            if self.current > self.end:
                raise StopIteration
            self.current += 1
            return self.current - 1

    for n in MyRange(1, 5):
        print(n)

    ##ORRRR you can use generators


# Generator - clean | infinite_integers() -> iterator. It is an easier way to create iterator. Yield-> pauses. nex-> continue
def infinite_integers():
    n = 0
    while True:
        yield n  # You are generating values. Pause execution until next is called again. You are returning the value n then pause. The calculation is always after pause
        n += 1


# fib() must be generator function
#  for num in fib(10)
# 0 1 1 2 3 5 8


def fib(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        c = a + b
        a = b
        b = c


if __name__ == "__main__":
    # main()
    # integers = infinite_integers()  # its an iterator coz you are using next
    # print(next(integers))  # 0
    # print(next(integers))  # 1
    # print(next(integers))  # 2

    for num in fib(10):
        print(num)

    # for m in range(10):
    #     print(next(integers))
