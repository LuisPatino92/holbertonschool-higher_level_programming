#!/usr/bin/python3
"""This module has MyInt Class"""


class MyInt(int):
    """Clas derived from int with a different behavior in == and != ops"""

    def __eq__(self, other):
        """Method equals checks for equality beetwen two MyInts"""
        val = super().__ne__(other)
        return val

    def __ne__(self, other):
        """Method equals checks for equality beetwen two MyInts"""
        val = super().__eq__(other)
        return val
