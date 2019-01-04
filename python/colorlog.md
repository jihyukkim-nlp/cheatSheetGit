~~~python
import colorlog, logging

# INFO (green)
colorlog.basicConfig(
			filename=None,
			level=logging.INFO,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.info(print_str)

# DEBUG (grey)
colorlog.basicConfig(
			filename=None,
			level=logging.DEBUG,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.debug(print_str)

# CRITICAL (red)
colorlog.basicConfig(
			filename=None,
			level=logging.CRITICAL,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.critical(print_str)

# ERROR (dark red)
colorlog.basicConfig(
			filename=None,
			level=logging.ERROR,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.error(print_str)

# WARN (yellow)
colorlog.basicConfig(
			filename=None,
			level=logging.WARN,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.warning(print_str)

# ANYTHING
colorlog.basicConfig(
			filename=None,
			level=logging.NOTSET,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.info(print_str)
colorlog.debug(print_str)
colorlog.critical(print_str)
colorlog.error(print_str)
colorlog.warning(print_str)
~~~


~~~python
>>> import colorlog, logging
>>> dir(logging)
['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'FileHandler', 'Filter', 'Filterer', 'Formatter', 'Handler', 'INFO', 'LogRecord', 'Logger', 'LoggerAdapter', 'Manager', 'NOTSET', 'NullHandler', 'PercentStyle', 'PlaceHolder', 'RootLogger', 'StrFormatStyle', 'StreamHandler', 'StringTemplateStyle', 'Template', 'WARN', 'WARNING', '_STYLES', '_StderrHandler', '__all__', '__author__', '__builtins__', '__cached__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__status__', '__version__', '_acquireLock', '_addHandlerRef', '_checkLevel', '_defaultFormatter', '_defaultLastResort', '_handlerList', '_handlers', '_levelToName', '_lock', '_logRecordFactory', '_loggerClass', '_nameToLevel', '_releaseLock', '_removeHandlerRef', '_showwarning', '_srcfile', '_startTime', '_warnings_showwarning', 'addLevelName', 'atexit', 'basicConfig', 'captureWarnings', 'collections', 'critical', 'currentframe', 'debug', 'disable', 'error', 'exception', 'fatal', 'getLevelName', 'getLogRecordFactory', 'getLogger', 'getLoggerClass', 'info', 'io', 'lastResort', 'log', 'logMultiprocessing', 'logProcesses', 'logThreads', 'makeLogRecord', 'os', 'raiseExceptions', 'root', 'setLogRecordFactory', 'setLoggerClass', 'shutdown', 'sys', 'threading', 'time', 'traceback', 'warn', 'warning', 'warnings', 'weakref']
>>> dir(colorlog)
['ColoredFormatter', 'LevelFormatter', 'StreamHandler', 'TTYColoredFormatter', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'absolute_import', 'basicConfig', 'colorlog', 'critical', 'debug', 'default_log_colors', 'error', 'escape_codes', 'exception', 'getLogger', 'info', 'log', 'logging', 'root', 'warning']
~~~
