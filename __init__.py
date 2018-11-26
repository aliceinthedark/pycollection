#!/usr/bin/env python

from functools import reduce
from itertools import takewhile, dropwhile, starmap

class Collection(object):
    def __init__(self, s):
        self.__s = s

    def __iter__(self):
        return iter(self.__s)

    def __getitem__(self, x):
        if type(x) is not slice:
            return self.__s[x]
        else:
            return Collection(self.__s[x])

    def index(self, val):
        return self.__s.index(val)

    def append(self, val):
        return Collection(self.__s + [val,])

    def extend(self, seq):
        return Collection(self.__s + seq)

    def repeat(self, count):
        return Collection(list(self.__s) * count)

    def any(self, fun):
        return reduce(self.__s, lambda a, b: a or fun(b), False)

    def all(self, fun):
        return reduce(self.__s, lambda a, b: a and fun(b), True)

    def filter(self, fun):
        return Collection(filter(fun, self.__s))

    def filterfalse(self, fun):
        return Collection(filter(lambda x: not fun(x), self.__s))

    def map(self, fun):
        return Collection(map(fun, self.__s))

    def starmap(self, fun):
        return Collection(starmap(fun, self.__s))

    def fold(self, fun, *args, **kwargs):
        return reduce(self.__s, fun, *args, **kwargs)

    def sorted(self, **kwargs):
        return Collection(sorted(self.__s, *args, **kwargs))

    def reversed(self):
        if type(self.__s) is filter or type(self.__s) is map:
            self.__s = list(self.__s)
        return Collection(reversed(self.__s))

    def zip(self, seq):
        return Collection(zip(self.__s, seq))

    def take(self, count):
        return Collection(self.__s[count:])

    def drop(self, count):
        return Collection(self.__s[:-count])

    def takewhile(self, pred):
        return Collection(takewhile(pred, self.__s))

    def dropwhile(self, pred):
        return Collection(dropwhile(pred, self.__s))

    def length(self):
        return len(self.__s)

    def sum(self):
        return sum(self.__s)

    def mul(self):
        return reduce(lambda a, b: a * b, self.__s, 1)

    def collection(self):
        return Collection(list(self.__s))

    def raw(self):
        return self.__s

    def list(self):
        return list(self.__s)
