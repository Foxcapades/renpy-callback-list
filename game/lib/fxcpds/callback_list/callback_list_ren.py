"""renpy
init python:
"""
from typing import Any, Protocol


class CallbackListCallable(Protocol):
    def __call__(self, name: str, interact: bool, **kwargs: Any) -> None:
        pass


class CallbackList(object):
    def __init__(self, *callbacks: CallbackListCallable) -> None:
        self._callbacks = [ *callbacks ]

    def __call__(self, event: str, interact=True, **kwargs: Any) -> None:
        for cb in self._callbacks:
            cb(event, interact, **kwargs)

    def add(self, callback: CallbackListCallable) -> None:
        self._callbacks.append(callback)
