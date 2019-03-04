DEBUG = False

LOG_ERR   = 1
LOG_INFO  = 2
LOG_DEBUG = 3

def _GetLogLevelStr(loglevel):
    strs = { LOG_ERR: "ERROR",
             LOG_INFO: "INFO",
             LOG_DEBUG: "DEBUG"
           }
    return strs.get(loglevel, "LOG")

def LOG(LOG_LEVEL, logmsg):
    loglevel = _GetLogLevelStr(LOG_LEVEL)
    if DEBUG is False:
        if LOG_LEVEL < LOG_DEBUG:
            print("{}: {}".format(loglevel, logmsg))
    else:
        print("{}: {}".format(loglevel, logmsg))

