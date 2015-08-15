import sys
import unittest
import inspect

def list_func():
    caller_file = inspect.getfile(sys._getframe(1))
    me = __import__(inspect.getmodulename(caller_file))
    for name in dir(me):
        obj = getattr(me, name)
        if inspect.isfunction(obj):
            yield obj

