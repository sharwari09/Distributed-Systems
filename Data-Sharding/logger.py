DEBUG = True

LOG_ERR = 1
LOG_INFO = 2
LOG_DEBUG = 3


def log(LOG_LEVEL, logmsg):
    if DEBUG is False:
        if LOG_LEVEL < LOG_DEBUG:
            print("{}".format(logmsg))
    else:
        print("{}".format(logmsg))