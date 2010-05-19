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
        headerdata = urllib.urlencode(parameters)
        try:
            request = urllib2.Request(self.addurl, headerdata)
            response = urllib2.urlopen(request).read()
            status = int(response)
            return (status, self.add_status_codes[status])
        except IOError:
            return (-1, "Connection failed.")


    def set_username(self, user):
        """ set username"""
        self.user = user

    def set_password(self, password):
        """ set password """
        self.password = password
