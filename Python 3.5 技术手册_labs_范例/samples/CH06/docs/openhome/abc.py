# Copyright 2016 openhome.cc. All Rights Reserved.
# Permission to use, copy, modify, and distribute this code and its
# documentation for educational purpose.

"""
Abstract Base Classes (ABCs) for Python Tutorial

Just a demo for DocStrings.
"""

from abc import ABCMeta, abstractmethod

class Ordering(metaclass=ABCMeta):
    '''
    A abc for implementing rich comparison methods.

    The class must define __gt__() and  __eq__() methods.
    '''
    @abstractmethod
    def __eq__(self, other):
        '''Return a == b'''
        pass

    @abstractmethod
    def __gt__(self, other):
        '''Return a > b'''
        pass

    def __ge__(self, other):
        '''Return a >= b'''
        return self > other or self == other

    def __lt__(self, other):
        '''Return a < b'''
        return not (self > other and self == other)

    def __le__(self, other):
        '''Return a <= b'''
        return (not self >= other) or self == other

    def __ne__(self, other):
        '''Return a != b'''
        return not self == other

