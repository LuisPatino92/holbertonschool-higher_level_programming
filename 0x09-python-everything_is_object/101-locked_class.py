#!/usr/bin/python3
"""This module has a weird class"""


class LockedClass:
    """ Class that do'nt accept new attributes but first_name"""
    __slots__ = ['first_name']
