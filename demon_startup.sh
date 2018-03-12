celery multi start worker\
    -A iapp \
    --pidfile="pid/%n.pid" \
    --logfile="log/%n%I.log" \
    -l info