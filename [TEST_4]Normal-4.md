# Python Test Set 4 - Normal

**Time: 30 minutes**  
**Total Questions: 20**

---

## Question 1
What will be the output of this code?
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

f = outer()
print(f())
```

## Question 2
Write a function that takes a string and returns a dictionary with character counts (e.g., "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}).

## Question 3
Explain the difference between shallow copy and deep copy in Python.

## Question 4
Write a class that uses `@dataclass` to create a simple data structure with automatic `__init__`, `__repr__`, and equality methods.

## Question 5
What is the purpose of `__slots__` in a class? Write an example class using `__slots__`.

## Question 6
Write a function that demonstrates the use of `enumerate()` to iterate over a list with indices.

## Question 7
Create a custom iterator for the Fibonacci sequence that implements `__iter__` and `__next__`.

## Question 8
Write a function that uses `collections.namedtuple` to create a Point class with x and y coordinates.

## Question 9
Explain the difference between instance methods, class methods, and static methods with examples.

## Question 10
Write a function that uses `functools.partial` to create a specialized version of an existing function.

## Question 11
What are closures? Write a closure example that maintains state between calls.

## Question 12
Write a function that demonstrates the use of `*args` with default parameters.

## Question 13
Create a class that implements the iterator protocol for a custom range-like object.

## Question 14
Write a function that uses `itertools.chain` to flatten a list of lists.

## Question 15
Explain what descriptors are and write a simple descriptor example.

## Question 16
Write a function that demonstrates the use of `yield from` for delegating to another generator.

## Question 17
What is the difference between `staticmethod` and `classmethod`? Provide examples of both.

## Question 18
Write a function that uses `abc.ABC` to create an abstract base class with an abstract method.

## Question 19
Create a function that demonstrates the use of `vars()` and `dir()` to inspect object attributes.

## Question 20
Write a class that demonstrates method resolution order (MRO) using multiple inheritance.

---

**End of Test Set 4**