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

"""Get app info by calling ActiveApp CLI program."""


import os
import subprocess
import time
import unicodedata

PROG = os.path.join(os.path.dirname(os.path.dirname(
                    os.path.abspath(__file__))),
                    'src',
                    'ActiveApp')


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
    cmd = [PROG]
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    output, err = proc.communicate()

    output = decode(output)
    err = decode(err).strip()

    if proc.returncode != 0:
        raise RuntimeError('Could not get frontmost application.')

    output = decode(output)

    app_name, bundle_id, app_path = [s.strip() for s in output.split('\n')]

    return (app_name, bundle_id, app_path)


if __name__ == '__main__':
    s = time.time()
    get_frontmost_app()
    d = time.time() - s
