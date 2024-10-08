# coding=utf-8
"""
Collection of handlers
"""

__author__ = 'av.smirnov'

from dataclasses import dataclass, field
from typing import List, Callable, Union
from .handler import Handler


@dataclass
class Handlers:
    """
    Collection of handlers.
    Handler would be any callable object or Handler class instance.
    """
    before: List[Union[Callable, Handler]] = field(default_factory=list)
    at_time: List[Union[Callable, Handler]] = field(default_factory=list)
    after: List[Union[Callable, Handler]] = field(default_factory=list)

    def __bool__(self):
        return bool(self.before or self.at_time or self.after)

    def __add__(self, other):
        new_handlers = Handlers()
        for handlers in (self, other):
            for attr in ('before', 'after', 'at_time'):
                getattr(new_handlers, attr).extend(getattr(handlers, attr))
        return new_handlers
