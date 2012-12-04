import socket

if socket.gethostname() is "design25":
    from sidar.settings_staging import *
    print "Using staging server settings."
else:
    from sidar.settings_development import *
    print "Using development settings."
print "DEBUG = %s" % DEBUG
