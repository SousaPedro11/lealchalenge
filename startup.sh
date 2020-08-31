#!/bin/sh
# gunicorn --workers=5 --reload --access-logfile - --error-logfile - 'run:app'
gunicorn run:app
