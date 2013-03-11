## @package tracing
# The tracing module for debug-purpose.

log = None

## Setup the debug traces.
# The traces can be logged to console and/or file.
# When logged to file a logrotate is used.
# @param enabled When True traces are enabled.
# @param path The path for the trace-file.
# @param fileName The trace-file-name.
# @param toConsole When True show traces to console.
# @param debugOn When True show debug-traces.
def setupTraces(enabled, path, fileName, toConsole, debugOn):
	global log

	if enabled:
		import logging
		import logging.handlers

		log = logging.getLogger("localsettings_app")
		if debugOn == True:
			level = logging.DEBUG
		else:
			level = logging.INFO
		log.setLevel(level)
		log.disabled = not enabled
		if toConsole == True:
			sth = logging.StreamHandler()
			sth.setLevel(level)
			log.addHandler(sth)
		fd = logging.handlers.RotatingFileHandler(path + fileName, maxBytes=1048576, backupCount=5)
		fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		fd.setFormatter(fmt)
		fd.setLevel(level)
		log.addHandler(fd)
	else:
		log = LogDummy()

class LogDummy(object):
	def __init__(self):
		self._str = ''
		
	def info(self, str, *args):
		self._str = str
		
	def debug(self, str, *args):
		self._str = str