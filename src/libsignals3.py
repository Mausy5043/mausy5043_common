#!/usr/bin/env python3

"""Provide a class to intercept signals."""

import signal


class GracefulKiller:
    """Class to intercept kill signals."""
    kill_now = False

    def __init__(self):
        """Set-up signals to intercept"""
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):  # noqa
        """Intercept signals and set the state appropriately.

        Args:
            signum: n/a
            frame: n/a
        """
        self.kill_now = True
