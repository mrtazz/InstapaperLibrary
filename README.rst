instapaperlib.py
================

Python library for the instapaper.com API.

http://instapaper.com

Usage:
-------

Use the library directly:

::
    import instapaperlib

    instapaperlib.auth("username", "password")
    instapaperlib.add_item("username", "password", "URL", "title")

Create an instance to work with:

::
    from instapaperlib import Instapaper

    i = Instapaper("username", "password")
    i.auth()

Catch the return codes to work with:

::
    from instapaperlib import Instapaper

    i = Instapaper("username", "password")
    (statuscode, statusmessage) = i.add_item("URL", "title")

Or use the cli client:

    instapaper.py -u user -p password -t title URL

If you have set your username:password in ~/.instapaperrc:

    instapaper.py URL

Installation
------------

  pip install instapaperlib

Or, if you must:

  easy_install instapaperlib

Coming next
------------
* Parse and return response header
