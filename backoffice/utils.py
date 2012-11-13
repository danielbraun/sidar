# -*- coding: utf-8 -*-


def nullify(str):
    if str == "":
        str = None
    return str


def emptify(str):
    if str is None:
        str = ""
    return str


def has_hebrew_chars(str):
    """
    >>> has_hebrew_chars(u'shdfgshjdf')
    False
    >>> has_hebrew_chars(u'sjkdfhsdjkfhצ')
    True
    """
    return any(u"\u0590" <= c <= u"\u05EA" for c in str)
