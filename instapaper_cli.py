#!/opt/local/bin/python2.6

from instapaper import Instapaper
from optparse import OptionParser
from getpass import getpass

def usage():
    print "Usage: instapaper.py [-h] username password url"
    print "Options:"
    print "-h   Print this help"

def main():

    # initialize parser
    usage = "usage: %prog -u USER [-t TITLE] url"
    parser = OptionParser(usage)
    parser.add_option("-u", "--user", action="store", dest="user",metavar="USER",
                      help="instapaper username")
    parser.add_option("-t", "--title", action="store", dest="title",metavar="TITLE",
                      help="title of the link to add")

    (options, args) = parser.parse_args()

    if not options.user:
        parser.error("No instapaper user given.")
    else:
        title = ""
        if options.title:
            title = options.title
        pw = getpass()
        inst = Instapaper(options.user,pw)
        result = inst.addItem(args[0],title)
        if (result == -1):
            print "Uh-Oh, something went wrong."

if __name__ == "__main__":
    main()
