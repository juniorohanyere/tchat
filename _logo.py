"""Logo module.
"""

import asyncio
from tgui.views.widgets import Label


class Logo(Label):
    def __init__(self, master, **kwargs):
        super(Logo, self).__init__(master, kwargs)

        self.logo()

    def logo(self):
        """tchat logo.

        Args:
            master (obj): layout object on which to create the logo
        """

        y, x = 0, 0     # TODO: to be modified

        # supposed to use the <text + multiline + align> parameter
        # and it should be handled in create_label method
        r0 = '▀█▀ █▀▀ █░█ █▀█ ▀█▀'
        r1 = '░█░ █▄▄ █▀█ █▀█ ░█░'

        text = r0 + '\n' + r1

        self._win.addstr(y, x, r0)
        self._win.addstr(y + 1, x, r1)

    def show(self):
        self._pan.show()

    def hide(self):
        self._pan.hide()
