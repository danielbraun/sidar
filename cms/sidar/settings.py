import socket
import os

if os.environ.get('LD_LIBRARY_PATH'):
    if 'heroku' in os.environ.get('LD_LIBRARY_PATH'):
        from sidar.settings_heroku import *
elif socket.gethostname() == "design25":
    from sidar.settings_staging import *
elif socket.gethostname() == "ubuntu":
    from sidar.settings_shenkar import *
else:
    from sidar.settings_development import *
