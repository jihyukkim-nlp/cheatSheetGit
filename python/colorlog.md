~~~python
import colorlog, logging
colorlog.basicConfig(
			filename=None,
			level=logging.INFO,
			format="%(log_color)s[%(levelname)s:%(asctime)s]%(reset)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S"
		)
print_str = "some string"
colorlog.info(print_str)
~~~
