# encoding: utf-8
'''
 instapaperlib.py -- brief simple library to use instapaper
'''

import urllib
import urllib2

class Instapaper:
    """ This class provides the structure for the connection object """

    def __init__(self, user, password, https=True):
        self.user = user
        self.password = password
        if https:
            self.authurl = "https://www.instapaper.com/api/authenticate"
            self.addurl = "https://www.instapaper.com/api/add"
        else:
            self.authurl = "http://www.instapaper.com/api/authenticate"
            self.addurl = "http://www.instapaper.com/api/add"

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

    def add_item(self, url, title=None, selection=None, response_info=False):
        """ Method to add a new item to a instapaper account

            Parameters: url -> URL to add
                        title -> optional title for the URL
            Returns: (status as int, status error message)
        """
        parameters = {
                      'username' : self.user,
                      'password' : self.password,
                      'url' : url,
                     }
        # look for optional parameters title and selection
        if title is not None:
            parameters['title'] = title
        else:
            parameters['auto-title'] = 1
        if selection is not None:
            parameters['selection'] = selection

        # make query with the chosen parameters
        status, headers = self._query(self.addurl, parameters)
        statustxt = self.add_status_codes[status]
        # if response headers are desired, return them also
        if response_info:
            return (status, statustxt, headers['title'], headers['location'])
        else:
            return (status, statustxt)

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
        parameters = {
                      'username' : self.user,
                      'password' : self.password
                     }
        status, headers = self._query(self.authurl, parameters)
        return (status, self.auth_status_codes[status])

    def _query(self, url=None, params=""):
        """ method to query a URL with the given parameters

            Parameters:
                url -> URL to query
                params -> dictionary with parameter values

            Returns: HTTP response code, headers
                     If an exception occurred, headers fields are None
        """
        if url is None:
            raise NoUrlError("No URL was provided.")
        # return values
        headers = {'location': None, 'title': None}
        headerdata = urllib.urlencode(params)
        try:
            request = urllib2.Request(url, headerdata)
            response = urllib2.urlopen(request)
            status = response.read()
            info = response.info()
            headers['location'] = info['Content-Location']
            headers['title'] = info['X-Instapaper-Title']
            return (int(status), headers)
        except IOError, exception:
            return (exception.code, headers)

# instapaper specific exceptions
class NoUrlError(Exception):
    """ exception to raise if no URL is given.
    """
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return repr(self.arg)


