"""General utility functions."""
from typing import Optional


class Func:
    """Function abstraction

    A class that represents a function."""

    def __init__(self, method: str, payload: Optional[dict] = None):
        """
        :param str method:
        :param str payload:
        """
        if payload is None:
            payload = {}
        self.method = method
        self.payload = payload
