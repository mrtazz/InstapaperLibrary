# encoding: utf-8

from instapaperlib import Instapaper

__author__ = "Daniel Schauenberg"
__version__ = "0.2.0"
__license__ = "MIT"

def auth(user='', password=''):
    return Instapaper(user, password).auth()

def add_item(user='', password='', url,
             title=None, selection=None,
             response_header=False):
    return Instapaper(user, password).add_item(url,title,
                                               selection,response_header)
