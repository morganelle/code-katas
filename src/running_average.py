"""Callable that keeps a running average."""


def running_average():
    """Instantiate a callable that returns a running average."""
    class Avg(object):
        def __init__(self):
            self.total = 0
            self.count = 0

        def __call__(self, num):
            if type(num) not in [int, float]:
                return TypeError('Please enter an int or float.')
            self.total += num
            self.count += 1
            return self.total / self.count
    return Avg()
