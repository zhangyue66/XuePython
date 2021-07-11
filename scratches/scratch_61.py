a = {}


a = {'rusage': {'inblock': 0, 'maxrss': 70880, 'nsignals': 0, 'utime': 2073.072, 'msgsnd': 0, 'ixrss': 0, 'msgrcv': 0, 'nivcsw': 753981, 'nvcsw': 42557925, 'oublock': 400, 'isrss': 0, 'stime': 447.352, 'minflt': 62535, 'nswap': 0, 'majflt': 0, 'idrss': 0}, 'prefetch_count': 20, 'clock': '3689273', 'pool': {'writes': {'strategy': None, 'all': '20.00%, 22.00%, 20.00%, 22.00%, 16.00%', 'avg': '20.00%', 'total': 50, 'inqueues': {'active': 0, 'total': 5}, 'raw': '10, 11, 10, 11, 8'}, 'put-guarded-by-semaphore': False, 'timeouts': [0, 0], 'max-concurrency': 5, 'max-tasks-per-child': 'N/A', 'processes': [23975, 23976, 23977, 23978, 23979]}, 'pid': 23877, 'total': {}, 'broker': {'connect_timeout': 4, 'transport_options': {}, 'insist': False, 'transport': 'amqp', 'alternates': ['amqp://ateuser:d3aeec875c479e55d1cdeea161842ec6@155.165.157.57:5672/celery', 'amqp://ateuser:d3aeec875c479e55d1cdeea161842ec6@155.165.157.58:5672/celery', 'amqp://ateuser:d3aeec875c479e55d1cdeea161842ec6@155.165.157.59:5672/celery'], 'virtual_host': 'celery', 'ssl': False, 'uri_prefix': None, 'userid': 'ateuser', 'failover_strategy': 'round-robin', 'heartbeat': 120.0, 'port': 5672, 'hostname': '155.165.157.57', 'login_method': 'AMQPLAIN'}, 'autoscaler': {'current': 5, 'max': 8, 'qty': 0, 'min': 5}}


worker_value = a["total"]

if worker_value == 5:
    print("yz is good !")
print(worker_value)