=================
instapaperlib.py
=================

.. image:: https://travis-ci.org/mrtazz/InstapaperLibrary.svg?branch=master
    :target: https://travis-ci.org/mrtazz/InstapaperLibrary
    
Overview
---------

Python library for the instapaper.com API. http://instapaper.com

Usage
------

Use the library directly::

    import instapaperlib

    instapaperlib.auth("username", "password")
    instapaperlib.add_item("username", "password", "URL", "title")
    # with selection test set
    instapaperlib.add_item("username", "password", "URL", "title", "selection")

Create an instance to work with::

    from instapaperlib import Instapaper

    i = Instapaper("username", "password")
    i.auth()

Catch the return codes to work with::

    from instapaperlib import Instapaper

    i = Instapaper("username", "password")
    (statuscode, statusmessage) = i.add_item("URL", "title")

Also catch the response header::

    from instapaperlib import Instapaper

    i = Instapaper("username", "password")
    (statuscode, statusmessage, title, location) = i.add_item("URL", "title", response_info=True)

Or use the cli client::

    instapaper.py -u user -p password -t title URL

If you have set your username:password in ~/.instapaperrc::

    instapaper.py URL

Installation
-------------
Install via pip::

    pip install instapaperlib

Or, if you must::

    easy_install instapaperlib
    
Contributing
-------------
- fork the repo
- add your changes and tests so I don't accidentally break anything in the future
- run the tests: :code:`python instapaperlib/instapaperlib.py`
- open a pull request (also runs the tests via Travis CI)
- high-five yourself, you're awesome

Meta
-----
:Project: http://github.com/mrtazz/InstapaperLibrary

:Issues: http://github.com/mrtazz/InstapaperLibrary/issues

