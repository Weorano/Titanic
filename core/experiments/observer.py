from functools import wraps


def record(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        name = func.__name__

        checkpoint = self.collector.load_checkpoint(name)

        if checkpoint is not None:
            self.collector.add(checkpoint)
            return checkpoint

        result = func(self, *args, **kwargs)

        self.collector.add(result)

        return result

    return wrapper