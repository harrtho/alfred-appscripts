#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2022 Thomas Harr <xDevThomas@gmail.com>
# Copyright (c) 2015 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-11-23
#

"""Get app info with AppKit via objc bridge."""


import time
import unicodedata

from AppKit import NSWorkspace


def decode(s):
    """Decode bytestring to str."""
    if isinstance(s, bytes):
        s = str(s, 'utf-8')
    elif not isinstance(s, str):
        raise TypeError("str or bytes required, not {}".format(type(s)))
    return unicodedata.normalize('NFC', s)


def get_frontmost_app():
    """Return (name, bundle_id and path) of frontmost application.

    Raise a `RuntimeError` if frontmost application cannot be
    determined.

    """
    for app in NSWorkspace.sharedWorkspace().runningApplications():
        if app.isActive():
            app_name = app.localizedName()
            bundle_id = app.bundleIdentifier()
            app_path = app.bundleURL().fileSystemRepresentation()

            return (app_name, bundle_id, app_path)

    else:
        raise RuntimeError("Couldn't get frontmost application.")


if __name__ == '__main__':
    s = time.time()
    get_frontmost_app()
    d = time.time() - s
