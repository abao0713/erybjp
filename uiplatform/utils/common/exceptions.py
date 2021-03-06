# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         exceptions.py
# Description:  
# Author:       yuanbaojun
# Date:         2021/5/12
#----------------------------


class PoiumException(Exception):
    """
    exception.
    """

    def __init__(self, msg=None, screen=None, stacktrace=None):
        self.msg = msg
        self.screen = screen
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.screen is not None:
            exception_msg += "Screenshot: available via screen\n"
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class PageSelectException(PoiumException):
    """
    Thrown when using a select box error
    """
    pass


class PageElementError(PoiumException):
    """
    Raises an error using the PagElement class
    """
    pass


class FindElementTypesError(PoiumException):
    """
    Find element types Error
    """
    pass


class CSSFindElementError(PoiumException):
    """
    Find element types Error
    """
    pass
