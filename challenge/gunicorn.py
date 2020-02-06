import multiprocessing

# run with
# gunicorn -c challenge/gunicorn.py challenge.wsgi

#
# Worker processes
#
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1 

# use gevent for improved performance
worker_class = 'gevent'
timeout = 30
keepalive = 2

# reload when config file changes
reload = True

#
#   Logging
#
errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(T)s"'
