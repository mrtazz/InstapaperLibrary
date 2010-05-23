# encoding: utf-8
'''
 instapaperlib.py -- brief simple library to use instapaper
'''

import urllib
import urllib2

class Instapaper:
    """ This class provides the structure for the connection object """

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.authurl = "https://www.instapaper.com/api/authenticate"
        self.addurl = "https://www.instapaper.com/api/add"

        self.add_status_codes = {
                                      201 : "URL successfully added.",
                                      400 : "Bad Request.",
                                      403 : "Invalid username or password.",
                                      500 : "Service error. Try again later."
                                }

        self.auth_status_codes = {
                                      200 : "OK.",
                                      403 : "Invalid username or password.",
                                      500 : "Service error. Try again later."
                                 }

    def add_item(self, url, title=""):
        """ Method to add a new item to a instapaper account

            Parameters: url -> URL to add
                        title -> optional title for the URL
            Returns: (status as int, status error message)
        """
        parameters = {'username' : self.user,'password' : self.password,
                      'url' : url, 'title' : title}
        status = self._query(self.addurl, parameters)
        return (status, self.add_status_codes[status])

    def auth(self, user=None, password=None):
        """ authenticate with the instapaper.com service

            Parameters: user -> username
                        password -> password
            Returns: (status as int, status error message)
        """
        if not user:
            user = self.user
        if not password:
            password = self.password
        parameters = {'username' : self.user, 'password' : self.password}
        status = self._query(self.authurl, parameters)
        return (status, self.auth_status_codes[status])

    def _query(self, url, params):
        """ method to query a URL with the given parameters

            Parameters:
                url -> URL to query
                params -> dictionary with parameter values

            Returns: HTTP response code
        """
        headerdata = urllib.urlencode(params)
        try:
            request = urllib2.Request(url, headerdata)
            response = urllib2.urlopen(request)
            status = response.read()
            info = response.info()
            return int(status)
        except IOError, exception:
            return exception.code

