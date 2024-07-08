"""Module to handle views.
"""

import asyncio
import curses
from curses import panel
import os

from .widgets import Logo


class SignIn(LinearLayout):
    """Sign in class.
    """
    def __init__(self, **kwargs):
        """Initialize self. See help(type(self)) for accurate signature.
        """

        master = self
        size = 3, 20
        anchor = 1, 1

        logo = Logo(master, size=size, multiline=True, anchor=anchor)

    def signin(self):
        pass


class SignUp:
    """Sign up class.
    """


class Auth:
    """Authentication class.
    """
