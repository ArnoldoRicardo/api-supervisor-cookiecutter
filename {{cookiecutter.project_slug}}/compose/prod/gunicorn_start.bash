#!/bin/bash

NAME="api"                               # Name of the application
DJANGODIR=/web                           # Django project directory
SOCKFILE=/web/run/gunicorn.sock          # we will communicate using this unix socket
USER=root                                   # the user to run as
GROUP=root                                  # the group to run as
NUM_WORKERS=3                               # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings      # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi              # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=/var/log/web/access.log \
  --timeout 120 \
  -k gevent
