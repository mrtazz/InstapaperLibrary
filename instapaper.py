##
# @file instapaper.py
# @brief simple library to use instapaper

import urllib
import urllib2

class Instapaper:
    """ This class provides the structure for the connection object """

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.authurl = "https://www.instapaper.com/api/authenticate"
        self.addurl = "https://www.instapaper.com/api/add"

    def add_item(self, url, title=""):
        """ Method to add a new item to a instapaper account
            Returns 0 on success and -1 if something went wrong
        """
        parameters = {'username' : self.user,'password' : self.password,
                      'url' : url, 'title' : title}
        headerdata = urllib.urlencode(parameters)
        try:
            request = urllib2.Request(self.addurl, headerdata)
            response = urllib2.urlopen(request).read()
            if (int(response) == 201):
                return 0
            else:
                return -1
        except IOError:
            return -1

    def set_username(self, user):
        """ set username"""
        self.user = user

    def set_password(self, password):
        """ set password """
        self.password = password
