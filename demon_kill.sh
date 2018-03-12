celery multi stopwait worker --pidfile="pid/%n.pid"
#ps auxww | grep 'celeryd' | awk {'print $2'} | xargs kill -9