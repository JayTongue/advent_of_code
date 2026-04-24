import inspect
import re

def dprint(*args):
    frame = inspect.currentframe().f_back
    source = inspect.getframeinfo(frame).code_context[0].strip()
    names = re.search(r'dprint\((.*)\)', source).group(1)
    names = [n.strip() for n in names.split(',')]
    for name, val in zip(names, args):
        print(f"{name}: {val}")