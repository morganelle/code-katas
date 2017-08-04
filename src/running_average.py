"""Callable that keeps a running average up to 2 decimal places."""


def running_average_class():
    """Instantiate a callable that returns a running average."""
    class Avg(object):
        def __init__(self):
            self.total = 0
            self.count = 0

        def __call__(self, num):
            if type(num) not in [int, float]:
                return TypeError('Please enter an int or float.')
            self.total += float(num)
            self.count += 1
            return round(self.total / self.count, 2)
    return Avg()


def running_average():
    """Instantiate a callable that returns a running average."""
    data = []

    def avg(num):
        if type(num) not in [int, float]:
            return TypeError('Please enter an int or float.')
        data.append(num)
        return round(sum(data, 0.0) / len(data), 2)
    return avg
