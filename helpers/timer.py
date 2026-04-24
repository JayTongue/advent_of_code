from time import time
def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        diff = float(t2-t1)
        if diff < 60:
            message = 'Great!'
        if 60 < diff < 300:
            message = 'Needs work...'
        elif diff > 300:
            message = 'You solution is bad and you should feel bad.'
        print(f'-------- | Function {func.__name__!r} executed in {diff:.4f}s. | {message} | ------------')
        return result
    return wrap_func