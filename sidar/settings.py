import socket
import os

if 'heroku' in os.environ['PATH']:
    from sidar.settings_heroku import *
    print "Using heroku server settings."
elif socket.gethostname() == "design25":
    from sidar.settings_staging import *
    print "Using staging server settings."
else:
    from sidar.settings_development import *
    print "Using development settings."
print "DEBUG = %s" % DEBUG
print "Host name = %s" % socket.gethostname()
