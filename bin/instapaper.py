#!/usr/bin/env python
# encoding: utf-8
"""
    instapaper.com cli client
"""

import urllib
import urllib2
import re
import sys
import os
import instapaperlib
from optparse import OptionParser
from getpass import getpass

def main():
    """
        main method
    """
    # initialize parser
    usage = "usage: %prog [-u USER] [-p PASSWORD] [-t TITLE] url"
    parser = OptionParser(usage, version="%prog "+instapaperlib.__version__)
    parser.add_option("-u", "--user", action="store", dest="user",
                      metavar="USER", help="instapaper username")
    parser.add_option("-p", "--password", action="store", dest="password",
                      metavar="USER", help="instapaper password")
    parser.add_option("-t", "--title", action="store", dest="title",
                      metavar="TITLE", help="title of the link to add")

    (options, args) = parser.parse_args()

    if not options.title:
        title = ""
    else:
        title = options.title
    if not len(args) > 0:
        parser.error("What do you want to read later?")

    if not options.user:
        # auth regex
        login = re.compile("(.+?):(.+)")
        try:
            config = open(os.path.expanduser("~") + "/.instapaperrc")
            for line in config:
                matches = login.match(line)
                if matches:
                    user = matches.group(1).strip()
                    password = matches.group(2).strip()
        except IOError:
            parser.error("No login information present.")
            sys.exit(-1)
    else:
        user = options.user
        # make sure all parameters are present
        if not options.password:
            password = getpass()
        else:
            password = options.password

    (status, text) = instapaperlib.add_item(user, password, args[0], title)
    print text

if __name__ == "__main__":
    main()
